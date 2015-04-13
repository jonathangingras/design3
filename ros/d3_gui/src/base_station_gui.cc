#include <ros/ros.h>
#include <std_msgs/String.h>
#include <tf/transform_listener.h>
#include <geometry_msgs/PointStamped.h>
#include <RosQtExitGuard.h>
#include <d3_table_transform/robotPose.h>
#include <d3_table_transform/robotPoseArray.h>
#include <common/common.h>

//Qt MUST BE included last because of some shit it does with signals in its
//immensely giant unintuitive crappy API
//otherwise it wont compile interring in conflcit with tf headers using boost signals
#include <QtGui/QApplication>
#include <QPixmap>
#include <QDeclarativeProperty>
#include <QGraphicsPixmapItem>
#include <QmlApplicationViewer.h>
#include <QThread>
#include <QtDeclarative>
#include <QDeclarativeEngine>

namespace d3t12 {
  namespace tf = d3_table_transform;
}

struct UIPose {
  typedef boost::shared_ptr<UIPose> Ptr;
  int x, y;
  float angle;
  float scale;

  inline UIPose(int _x = 0, int _y = 0, float _yaw = 0, float _scale = 1):
    x(_x), y(_y), angle(_yaw), scale(_scale) {}
};

class UIPoseConverter {
private:
  float actualTableHeight;
  QDeclarativeView* view;
  const float robotHalfWidth;
  const int robotOriginalImageWidth;

  inline QObject* getGameBoard() {
    return view->rootObject()->findChild<QObject*>("gameBoard");
  }

  int getTableHeight() {
    QObject* gameBoard = getGameBoard();
    return gameBoard->property("height").toInt(); 
  }

  int getTableWidth() {
    QObject* gameBoard = getGameBoard();
    return gameBoard->property("width").toInt(); 
  }

  int getOriginX() {
    QObject* gameBoard = getGameBoard();
    QDeclarativeProperty leftMarginProperty(gameBoard, "anchors.leftMargin");
    QVariant leftMargin = leftMarginProperty.read();

    return leftMargin.toInt() + getTableWidth();
  }

  int getOriginY() {
    QObject* gameBoard = getGameBoard();
    QDeclarativeProperty topMarginProperty(gameBoard, "anchors.topMargin");
    QVariant topMargin = topMarginProperty.read();

    return topMargin.toInt() + getTableHeight();
  }

  inline float getScaleFactor() {
    return ((float)getTableHeight())/actualTableHeight;
  }

  inline float getRobotImageScale() {
    float robotOnTableFactor = (2*robotHalfWidth)/actualTableHeight;
    float robotWidthPixel = robotOnTableFactor*getTableHeight();
    return robotWidthPixel/robotOriginalImageWidth;
  }

public:
  inline UIPoseConverter(float _actualTableHeight, QDeclarativeView* _view):
    actualTableHeight(_actualTableHeight), view(_view), robotHalfWidth(0.1175), robotOriginalImageWidth(348) {}

  UIPose getUIPoseFromTfPose(float receivedX, float receivedY, float receivedYaw) {
    float scaleF = getScaleFactor();

    float x = (float)getOriginX() - (scaleF*receivedY);// - (scaleF*robotHalfWidth);
    float y = (float)getOriginY() - (scaleF*receivedX);// - (scaleF*robotHalfWidth);

    float angle = -((receivedYaw*180)/M_PI);

    return UIPose(x, y, angle, getRobotImageScale());
  }
};

class UIContentSetter : public d3t12::Updater {
private:
  QDeclarativeView* view;
  std::string flagsPath;
  boost::mutex* mutex;
  d3t12::UIEmitter* emitter;

  std::string currentCountry;

  inline QObject* getCountryTextInput() {
    return view->rootObject()->findChild<QObject*>("countryName");
  }

  inline QObject* getQuestionTextInput() {
    return view->rootObject()->findChild<QObject*>("questionText");
  }

  inline QObject* getFlagImage() {
    return view->rootObject()->findChild<QObject*>("flagImage");
  }

  void setCountryName(std::string countryNameStr) {
    QObject* countryTextInput = getCountryTextInput();
    QDeclarativeProperty countryTextProperty(countryTextInput, "text");
    countryTextProperty.write(QVariant(QString(countryNameStr.c_str())));
  }

  void setCountryFlag(std::string flagPath) {
    QObject* flagImage = getFlagImage();
    QDeclarativeProperty flagProperty(flagImage, "source");
    flagProperty.write(QVariant(QString(flagPath.c_str())));
  }

public:
  inline UIContentSetter(QDeclarativeView* _view, std::string _flagsPath, boost::mutex* _mutex, d3t12::UIEmitter* _emitter):
    view(_view), flagsPath(_flagsPath), mutex(_mutex), emitter(_emitter) {}

  void setAnswer(std::string countryName) {
    currentCountry = countryName;
    emitter->emitSignal();
  }

  void update() {
    if(currentCountry.empty()) return;
    mutex->lock();
    setCountryName(currentCountry);
    setCountryFlag(flagsPath + '/' + currentCountry + ".gif");
    mutex->unlock();
  }

  void setTimer(int secs) {
    QObject* timer = view->rootObject()->findChild<QObject*>("timer");
    QDeclarativeProperty secsProperty(timer, "secs");
    mutex->lock();
    secsProperty.write(QVariant(secs));
    mutex->unlock();
  }

  void setQuestion(std::string questionStr) {
    QObject* questionTextInput = getQuestionTextInput();
    QDeclarativeProperty questionTextProperty(questionTextInput, "text");
    mutex->lock();
    questionTextProperty.write(QVariant(QString(questionStr.c_str())));
    mutex->unlock();
  }

};

struct PoseListener {
  ros::NodeHandle& nodeHandle;
  boost::mutex& mutex;
  UIPose::Ptr uiPose;
  UIPoseConverter* poseConverter;
  
  inline PoseListener(ros::NodeHandle& _nodeHandle, boost::mutex& _mutex, UIPose::Ptr _uiPose, UIPoseConverter* _poseConverter):
    nodeHandle(_nodeHandle), mutex(_mutex), uiPose(_uiPose), poseConverter(_poseConverter) {}
  
  void operator()(const d3t12::tf::robotPose::ConstPtr& robotPose) {
    UIPose uiPoseNew = poseConverter->getUIPoseFromTfPose(robotPose->x, robotPose->y, robotPose->yaw);
        
    mutex.lock();
    *uiPose = uiPoseNew;
    mutex.unlock();
  }
  
  ros::Subscriber subscribe() {
    return nodeHandle.subscribe<d3t12::tf::robotPose>("/robot_positioner/robot_pose", 1, *this);
  }
};

struct PlannedPathDrawer {
  ros::NodeHandle& nodeHandle;
  boost::mutex& mutex;
  UIPoseConverter* poseConverter;

  QPen pen;
  QGraphicsScene* scene;
  std::vector<QGraphicsLineItem*> currentLines;

  inline PlannedPathDrawer(ros::NodeHandle& _nodeHandle, boost::mutex& _mutex, UIPoseConverter* _poseConverter, QGraphicsScene* _scene):
    nodeHandle(_nodeHandle), mutex(_mutex), poseConverter(_poseConverter), pen(QColor(255,0,0)), scene(_scene) {}

  void clearLines() {
    for(std::vector<QGraphicsLineItem*>::iterator it = currentLines.begin(); it != currentLines.end(); ++it) {
      scene->removeItem(*it);
    }
    currentLines.clear();
  }

  void updateLines(const d3t12::tf::robotPoseArray::ConstPtr& robotPoseArray) {
    std::vector<float> xs, ys;

    for(std::vector<d3t12::tf::robotPose>::const_iterator it = robotPoseArray->poses.begin(); it != robotPoseArray->poses.end(); ++it) {
      UIPose uiPose = poseConverter->getUIPoseFromTfPose(it->x, it->y, it->yaw);
      xs.push_back(uiPose.x);
      ys.push_back(uiPose.y);
    }

    clearLines();

    if(robotPoseArray->poses.size()) {
      for(std::vector<float>::const_iterator itx = xs.begin(), ity = ys.begin(); itx != xs.end() - 1 && ity != ys.end() - 1; ++itx, ++ity) {
        currentLines.push_back( scene->addLine(*itx, *ity, *(itx + 1), *(ity + 1), pen) );
      }
    }
  }

  void operator()(const d3t12::tf::robotPoseArray::ConstPtr& _robotPoseArray) {
    ROS_ERROR_STREAM("calling path drawer");
    if(!_robotPoseArray.get()) return;

    mutex.lock();
    updateLines(_robotPoseArray);
    mutex.unlock();
  }

  ros::Subscriber subscribe() {
    return nodeHandle.subscribe<d3t12::tf::robotPoseArray>("/d3_journey/robot_path", 1, *this);
  }
};

struct Timer {
private:
  typedef boost::shared_ptr<boost::thread> ThreadPtr;
  UIContentSetter* setter;
  boost::mutex timeLock;
  ThreadPtr thread;
  int secs;

  void time() {
    timeLock.lock();
    timeLock.unlock();
    setter->setTimer(++secs);
    d3t12::sleepSecondsNanoSeconds(1,0);
  }

  static void run(Timer* timer) {
    while(1) {
      timer->time();
    }
  }

public:
  void pause() {
    timeLock.lock();
  }

  void resume() {
    timeLock.unlock();
  }

  void reset() {
    timeLock.unlock();
    timeLock.lock();
    secs = 0;
    setter->setTimer(secs);
  }

  inline Timer(UIContentSetter* _setter):
    setter(_setter), secs(-1) {
      timeLock.lock();
      thread = ThreadPtr(new boost::thread(&this->run, this));
  }
};

void updateScene(d3t12::SignalFunctor* exitGuard, boost::mutex* mutex, QGraphicsScene* scene, QGraphicsPixmapItem* item, UIPose::Ptr uiPose) {
  while(exitGuard->good()) {
    mutex->lock();
    UIPose uiPoseCpy = *uiPose;
    mutex->unlock();

    item->setScale(uiPoseCpy.scale);
    item->setPos(uiPoseCpy.x, uiPoseCpy.y);
    item->setRotation(uiPoseCpy.angle);

    usleep(20000);
    mutex->lock();
    scene->update();
    mutex->unlock();
  }
}

void rosSpin() {
  ros::spin();
}

struct QuestionWritter {
  UIContentSetter* setter;

  inline QuestionWritter(UIContentSetter* _setter): setter(_setter) {}

  void operator()(const std_msgs::String::ConstPtr& question) {
    setter->setQuestion(question->data);
  }
};

struct AnswerWritter {
  UIContentSetter* setter;

  inline AnswerWritter(UIContentSetter* _setter): setter(_setter) {}

  void operator()(const std_msgs::String::ConstPtr& answer) {
    setter->setAnswer(answer->data);
  }
};

namespace d3t12 {

void StartButtonCallback(void* ptr) {
  ROS_ERROR_STREAM("StartButton");
  ((Timer*)ptr)->resume();
}

void CountryOkButtonCallback(void* ptr) {
  ROS_ERROR_STREAM("CountryOkButton: " << *(int*)ptr);
}

void BadCountryButtonCallback(void* ptr) {
  ROS_ERROR_STREAM("BadCountryButton: " << *(int*)ptr);
}

} //d3t12


Q_DECL_EXPORT 
int main(int argc, char** argv) {
		QApplication app(argc, argv);
    ros::init(argc, argv, "d3_base_station_gui");
    ros::NodeHandle node;
    d3t12::SignalFunctor::Ptr exitGuard(new d3t12::RosQtExitGuard(node, &app));
    d3t12::SIGINTHandler::getInstance().setSignalHandler(exitGuard);

    std::string qmlPath, imagePath, flagsPath;
    node.getParam("d3_base_station_gui/qmlPath", qmlPath);
    node.getParam("d3_base_station_gui/imagePath", imagePath);
    node.getParam("d3_base_station_gui/flagsPath", flagsPath);


    qmlRegisterType<d3t12::StartButton>("com.d3t12.button", 1, 0, "D3T12StartButton");
    int i = 9;
    d3t12::StartButton::callback = &d3t12::StartButtonCallback;

    qmlRegisterType<d3t12::CountryOkButton>("com.d3t12.button", 1, 0, "D3T12CountryOkButton");
    d3t12::CountryOkButton::ptr = &i;
    d3t12::CountryOkButton::callback = &d3t12::CountryOkButtonCallback;

    qmlRegisterType<d3t12::BadCountryButton>("com.d3t12.button", 1, 0, "D3T12BadCountryButton");
    d3t12::BadCountryButton::ptr = &i;
    d3t12::BadCountryButton::callback = &d3t12::BadCountryButtonCallback;


    d3t12::UIEmitter emitter;
    QmlApplicationViewer viewer(&emitter);
    viewer.setSource(QUrl(qmlPath.c_str()));
    viewer.show();

    QPixmap pixmap(imagePath.c_str());
    QGraphicsPixmapItem item(pixmap);
    viewer.scene()->addItem(&item);
    item.setOffset( -0.5 * QPointF( item.pixmap().width(), item.pixmap().height() ) );
    
    UIPoseConverter poseConverter(2.305, &viewer);
    UIPose::Ptr uiPose(new UIPose);
    boost::mutex mutex;
    
    PoseListener poseListener(node, mutex, uiPose, &poseConverter);
    ros::Subscriber poseSubscriber = poseListener.subscribe();

    PlannedPathDrawer pathDrawer(node, mutex, &poseConverter, viewer.scene());
    ros::Subscriber plannedPathSubscriber = pathDrawer.subscribe();

    //threads
    boost::thread rosSpinner(rosSpin);
    boost::thread sceneUpdaterThread(updateScene, exitGuard.get(), &mutex, viewer.scene(), &item, uiPose);

    //TODO add a subscription to atlas asker so it can change when sent
    UIContentSetter setter(&viewer, flagsPath, &mutex, &emitter);
    AnswerWritter answerWritter(&setter);
    QuestionWritter questionWritter(&setter);
    ros::Subscriber quSub = node.subscribe<std_msgs::String>("/robot_journey/question", 1, questionWritter);
    ros::Subscriber anSub = node.subscribe<std_msgs::String>("/robot_journey/answer", 1, answerWritter);

    viewer.setUpdater(&setter);
    Timer timer(&setter);
    d3t12::StartButton::ptr = &timer;
    
    return app.exec();
}
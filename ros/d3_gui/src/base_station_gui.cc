#include <ros/ros.h>
#include <tf/transform_listener.h>
#include <geometry_msgs/PointStamped.h>
#include <RosQtExitGuard.h>
#include <d3_table_transform/robotPose.h>

//Qt MUST BE included last because of some shit it does with signals in its
//immensely giant unintuitive crappy API
//otherwise it wont compile interring in conflcit with tf headers using boost signals
#include <QtGui/QApplication>
#include <QPixmap>
#include <QDeclarativeProperty>
#include <QGraphicsPixmapItem>
#include <QmlApplicationViewer.h>

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

class UIContentSetter {
private:
  QDeclarativeView* view;
  std::string flagsPath;

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
  inline UIContentSetter(QDeclarativeView* _view, std::string _flagsPath): view(_view), flagsPath(_flagsPath) {}

  void setAnswer(std::string countryName) {
    setCountryName(countryName);
    setCountryFlag(flagsPath + '/' + countryName + ".gif");
  }

  void setQuestion(std::string questionStr) {
    QObject* questionTextInput = getQuestionTextInput();
    QDeclarativeProperty questionTextProperty(questionTextInput, "text");
    questionTextProperty.write(QVariant(QString(questionStr.c_str())));
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

void updateScene(d3t12::SignalFunctor* exitGuard, boost::mutex* mutex, QGraphicsScene* scene, QGraphicsPixmapItem* item, UIPose::Ptr uiPose) {
  while(exitGuard->good()) {
    mutex->lock();
    UIPose uiPoseCpy = *uiPose;
    mutex->unlock();

    item->setScale(uiPoseCpy.scale);
    item->setPos(uiPoseCpy.x, uiPoseCpy.y);
    item->setRotation(uiPoseCpy.angle);

    usleep(20000);
    scene->update();
  }
}

void rosSpin() {
  ros::spin();
}

Q_DECL_EXPORT 
int main(int argc, char** argv) {
		QApplication app(argc, argv);
    ros::init(argc, argv, "d3_base_station_gui");
    ros::NodeHandle handle;
    d3t12::SignalFunctor::Ptr exitGuard(new d3t12::RosQtExitGuard(handle, &app));
    d3t12::SIGINTHandler::getInstance().setSignalHandler(exitGuard);

    std::string qmlPath, imagePath, flagsPath;
    handle.getParam("d3_base_station_gui/qmlPath", qmlPath);
    handle.getParam("d3_base_station_gui/imagePath", imagePath);
    handle.getParam("d3_base_station_gui/flagsPath", flagsPath);

    QmlApplicationViewer viewer;
    viewer.setSource(QUrl(qmlPath.c_str()));
    viewer.show();

    QPixmap pixmap(imagePath.c_str());
    QGraphicsPixmapItem item(pixmap);
    viewer.scene()->addItem(&item);
    item.setOffset( -0.5 * QPointF( item.pixmap().width(), item.pixmap().height() ) );
    
    UIPoseConverter poseConverter(2.305, &viewer);
    UIPose::Ptr uiPose(new UIPose);
    boost::mutex mutex;
    PoseListener poseListener(handle, mutex, uiPose, &poseConverter);
    ros::Subscriber poseSubscriber = poseListener.subscribe();
    //threads
    boost::thread rosSpinner(rosSpin);
    boost::thread sceneUpdaterThread(updateScene, exitGuard.get(), &mutex, viewer.scene(), &item, uiPose);

    //TODO add a subscription to atlas asker so it can change when sent
    //next 3 lines are examples
    UIContentSetter setter(&viewer, flagsPath);
    setter.setAnswer("Germany");
    setter.setQuestion("Who likes sausage?");
    
    return app.exec();
}
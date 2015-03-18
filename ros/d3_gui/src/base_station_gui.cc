#include <ros/ros.h>
#include <tf/transform_listener.h>
#include <geometry_msgs/PointStamped.h>
#include <RosQtExitGuard.h>

//Qt MUST BE included last because of some shit it does with signals in its
//immensely giant unintuitive crappy API
//otherwise it wont compile interring in conflcit with tf headers using boost signals
#include <QtGui/QApplication>
#include <QPixmap>
#include <QDeclarativeProperty>
#include <QGraphicsPixmapItem>
#include <QmlApplicationViewer.h>

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

  void setCountry(std::string countryName) {
    setCountryName(countryName);
    setCountryFlag(flagsPath + '/' + countryName + ".gif");
  }

  void setQuestion(std::string questionStr) {
    QObject* questionTextInput = getQuestionTextInput();
    QDeclarativeProperty questionTextProperty(questionTextInput, "text");
    questionTextProperty.write(QVariant(QString(questionStr.c_str())));
  }

};

inline geometry_msgs::PoseStamped robotZero() {
  geometry_msgs::PoseStamped robotPoseOnRobot;
  robotPoseOnRobot.header.frame_id = "robot_center";
  robotPoseOnRobot.header.stamp = ros::Time();

  robotPoseOnRobot.pose.position.x = 0;
  robotPoseOnRobot.pose.position.y = 0;
  robotPoseOnRobot.pose.position.z = 0;
  robotPoseOnRobot.pose.orientation = tf::createQuaternionMsgFromYaw(0);
  return robotPoseOnRobot;
}

void listenTf(d3t12::SignalFunctor* exitGuard, boost::mutex* mutex, UIPoseConverter* poseConverter, UIPose::Ptr uiPose) {  
  tf::TransformListener listener(ros::Duration(10));

  while(exitGuard->good()) {
    try {
      geometry_msgs::PoseStamped robotPoseOnTable;
      listener.transformPose("d3_table_origin", robotZero(), robotPoseOnTable);

      tf::Quaternion q;
      tf::quaternionMsgToTF(robotPoseOnTable.pose.orientation, q);
      
      UIPose uiPoseNew = poseConverter->getUIPoseFromTfPose(robotPoseOnTable.pose.position.x, robotPoseOnTable.pose.position.y, tf::getYaw(q));
      mutex->lock();
      *uiPose = uiPoseNew;
      mutex->unlock();
    } catch(tf::TransformException& ex) {
      ROS_ERROR_STREAM("could not transform robot position: " << ex.what());
    }
  }
}

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
    QUrl qmlFilePath(qmlPath.c_str());
    viewer.setSource(qmlFilePath);
    viewer.show();

    QString filepath(imagePath.c_str());
    QPixmap pixmap(filepath);
    QGraphicsPixmapItem item(pixmap);
    viewer.scene()->addItem(&item);
    item.setOffset( -0.5 * QPointF( item.pixmap().width(), item.pixmap().height() ) );
    
    UIPoseConverter poseConverter(2.305, &viewer);
    UIPose::Ptr uiPose(new UIPose);

    //TODO add a subscription to atlas asker so it can change when sent
    UIContentSetter setter(&viewer, flagsPath);
    setter.setCountry("Flag_Allemagne");
    setter.setQuestion("Who likes sausage?");
    viewer.scene()->update();

    //threads
    boost::mutex mutex;
    boost::thread tfListenerThread(listenTf, exitGuard.get(), &mutex, &poseConverter, uiPose);
    boost::thread sceneUpdaterThread(updateScene, exitGuard.get(), &mutex, viewer.scene(), &item, uiPose);

    return app.exec();
}
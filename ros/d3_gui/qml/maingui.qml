import QtQuick 1.1
import com.d3t12.button 1.0

Rectangle {

    id: rectangle2
    width: 800
    height: 480
    radius: 0
    scale: 1
    clip: false
    smooth: true
    border.width: 5
    border.color: "#171f51"
    opacity: 1
    visible: true

    Rectangle {
        objectName: "gameBoard"
        id: basePlancheJeu

        color: "#ffffff"
        anchors.top: parent.top
        anchors.topMargin: 35
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 15
        anchors.left: parent.left
        anchors.leftMargin: 30
        border.width: 4
        border.color: "#000000"
        width: height / 2.058

        Rectangle {
            id: zoneDrapeau
            y: 269

            color: "#ffffff"
            anchors.left: parent.left
            anchors.leftMargin: parent.width/5
            anchors.right: parent.right
            anchors.rightMargin: parent.width/5
            anchors.bottom: parent.bottom
            anchors.bottomMargin: parent.width/5
            border.width: 9
            border.color: "#3dd120"
            height: width

            Rectangle {
                id: cube1
                color: "#ffffff"
                border.width: 1
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 5 * (zoneDrapeau.width / 7)
                anchors.right: parent.right
                anchors.rightMargin: 5 * (zoneDrapeau.width / 7)
                border.color: "#000000"
                anchors.left: parent.left
                anchors.leftMargin: zoneDrapeau.width / 7
                anchors.top: parent.top
                anchors.topMargin: zoneDrapeau.width / 7
            }

            Rectangle {
                id: cube2
                color: "#ffffff"
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 5 * (zoneDrapeau.width / 7)
                anchors.right: parent.right
                anchors.rightMargin: 3 * (zoneDrapeau.width / 7)
                anchors.top: parent.top
                anchors.topMargin: zoneDrapeau.width / 7
                anchors.left: cube1.right
                anchors.leftMargin: zoneDrapeau.width / 7
                border.color: "#000000"
            }

            Rectangle {
                id: cube3
                color: "#ffffff"
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 5 * (zoneDrapeau.width / 7)
                border.color: "#000000"
                anchors.left: cube2.right
                anchors.leftMargin: zoneDrapeau.width / 7
                anchors.right: parent.right
                anchors.rightMargin: zoneDrapeau.width / 7
                anchors.top: parent.top
                anchors.topMargin: zoneDrapeau.width / 7
            }

            Rectangle {
                id: cube4
                color: "#ffffff"
                anchors.right: cube2.left
                anchors.rightMargin: zoneDrapeau.width / 7
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 3 * (zoneDrapeau.width / 7)
                anchors.left: parent.left
                anchors.leftMargin: zoneDrapeau.width / 7
                anchors.top: cube1.bottom
                anchors.topMargin: zoneDrapeau.width / 7
                border.color: "#000000"
            }

            Rectangle {
                id: cube5
                color: "#ffffff"
                anchors.right: cube3.left
                anchors.rightMargin: zoneDrapeau.width / 7
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 3 * (zoneDrapeau.width / 7)
                anchors.left: cube4.right
                anchors.leftMargin: zoneDrapeau.width / 7
                anchors.top: cube2.bottom
                anchors.topMargin: zoneDrapeau.width / 7
                border.color: "#000000"
            }

            Rectangle {
                id: cube6
                color: "#ffffff"
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 3 * (zoneDrapeau.width / 7)
                anchors.top: cube3.bottom
                anchors.topMargin: zoneDrapeau.width / 7
                anchors.left: cube5.right
                anchors.leftMargin: zoneDrapeau.width / 7
                anchors.right: parent.right
                anchors.rightMargin: zoneDrapeau.width / 7
                border.color: "#000000"
            }

            Rectangle {
                id: cube7
                color: "#ffffff"
                anchors.right: cube5.left
                anchors.rightMargin: zoneDrapeau.width / 7
                anchors.left: parent.left
                anchors.leftMargin: zoneDrapeau.width / 7
                anchors.bottom: parent.bottom
                anchors.bottomMargin: zoneDrapeau.width / 7
                anchors.top: cube4.bottom
                anchors.topMargin: zoneDrapeau.width / 7
                border.color: "#000000"
            }

            Rectangle {
                id: cube8
                color: "#ffffff"
                anchors.right: cube6.left
                anchors.rightMargin: zoneDrapeau.width / 7
                anchors.left: cube7.right
                anchors.leftMargin: zoneDrapeau.width / 7
                anchors.bottom: parent.bottom
                anchors.bottomMargin: zoneDrapeau.width / 7
                anchors.top: cube5.bottom
                anchors.topMargin: zoneDrapeau.width / 7
                border.color: "#000000"
            }

            Rectangle {
                id: cube9
                color: "#ffffff"
                anchors.right: parent.right
                anchors.rightMargin: zoneDrapeau.width / 7
                anchors.bottom: parent.bottom
                anchors.bottomMargin: zoneDrapeau.width / 7
                anchors.left: cube8.right
                anchors.leftMargin: zoneDrapeau.width / 7
                anchors.top: cube6.bottom
                anchors.topMargin: zoneDrapeau.width / 7
                border.color: "#000000"
            }
        }
    }

    /*Text {
        id: titrePlancheJeu
        x: 82
        y: 15
        text: qsTr("Game board")
        anchors.right: basePlancheJeu.right
        anchors.rightMargin: 60 * (basePlancheJeu.width / 208.9)
        anchors.left: basePlancheJeu.left
        anchors.leftMargin: 60 * (basePlancheJeu.width / 208.9)
        anchors.top: parent.top
        anchors.topMargin: 5 * (basePlancheJeu.width / 208.9)
        anchors.bottom: basePlancheJeu.top
        anchors.bottomMargin: 6 * (basePlancheJeu.width / 208.9)
        font.pointSize: (16 * (basePlancheJeu.width / 208.9) > 0 ? 16 * (basePlancheJeu.width / 208.9) : 16)
        font.family: "Ubuntu"
        horizontalAlignment: Text.AlignLeft
    }*/

    Rectangle {
        id: basePlancheJeuModifiable
        x: 7
        y: 35

        color: "#ffffff"
        anchors.top: parent.top
        anchors.topMargin: 35
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 15
        anchors.left: parent.left
        anchors.leftMargin: 30
        border.width: 4
        border.color: "#000000"
        width: height /2.058
        opacity: 0.2
    }
    Text {
        id: titreReponse
        x: 486
        y: 187
        width: 226
        height: titreQuestion.height
        text: qsTr("Questions's Answer")
        anchors.rightMargin: 88 * (basePlancheJeu.width / 208.9)
        anchors.leftMargin: 249 * (basePlancheJeu.width / 208.9)
        anchors.topMargin: 100 * (basePlancheJeu.width / 208.9)
        font.pointSize: (16 * (basePlancheJeu.width / 208.9) > 0 ? 16 * (basePlancheJeu.width / 208.9) : 16)
        anchors.right: parent.right
        anchors.left: basePlancheJeu.right
        anchors.top: titreQuestion.bottom

    }

    Text {
        id: titreQuestion
        height: 25
        text: qsTr("Atlas's Question")
        anchors.leftMargin: 249 * (basePlancheJeu.width / 208.9)
        anchors.top: parent.top
        anchors.topMargin: 35 * (basePlancheJeu.width / 208.9)
        anchors.right: parent.right
        anchors.rightMargin: 168 * (basePlancheJeu.width / 208.9)
        anchors.left: basePlancheJeu.right
        font.pointSize: (16 * (basePlancheJeu.width / 208.9) > 0 ? 16 * (basePlancheJeu.width / 208.9) : 16)
    }



    Rectangle {
        id: zoneQuestion
        x: 486
        y: 73
        color: "#ffffff"
        anchors.right: titreQuestion.left
        anchors.rightMargin: -254 * (basePlancheJeu.width / 230)
        anchors.left: titreQuestion.left
        anchors.leftMargin: 0
        anchors.bottom: titreReponse.top
        anchors.bottomMargin: 22 * (basePlancheJeu.width / 230)
        anchors.top: titreQuestion.bottom
        anchors.topMargin: 13 * (basePlancheJeu.width / 230)
        border.width: 1
        border.color: "#000000"

        TextInput {
            id: question
            objectName: "questionText"
            text: ""
            horizontalAlignment: TextInput.AlignHCenter
            anchors.fill: parent
            readOnly: true
            echoMode: TextInput.Normal
            font.pixelSize: 14
        }
    }

    Rectangle {
        id: zoneReponse
        y: 226
        color: "#ffffff"
        anchors.right: zoneQuestion.right
        anchors.rightMargin: 0
        anchors.left: titreReponse.left
        anchors.leftMargin: 0
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 256 * (basePlancheJeu.width / 208.9)
        anchors.top: titreReponse.bottom
        border.color: "#000000"
        anchors.topMargin: 13 * (basePlancheJeu.width / 208.9)
        TextInput {
            id: reponseDrapeau
            objectName: "countryName"
            x: 0
            y: 0
            text: ""
            horizontalAlignment: TextInput.AlignHCenter
            anchors.rightMargin: 0
            anchors.bottomMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0
            anchors.fill: parent
            font.pixelSize: 14
            echoMode: TextInput.Normal
            readOnly: true
        }
        border.width: 1
    }

    Text {
        id: titreDrapeau
        x: 465
        y: 238
        width: 226
        height: titreQuestion.height
        text: qsTr("Corresponding Flag")
        anchors.rightMargin: 88 * (basePlancheJeu.width / 208.9)
        anchors.leftMargin: 249 * (basePlancheJeu.width / 208.9)
        anchors.topMargin: 13 * (basePlancheJeu.width / 208.9)
        anchors.top: zoneReponse.bottom
        font.pointSize: (16 * (basePlancheJeu.width / 208.9) > 0 ? 16 * (basePlancheJeu.width / 208.9) : 16)
        anchors.right: parent.right
        anchors.left: basePlancheJeu.right
    }

    Image {
        id: imageDrapeau
        objectName: "flagImage"
        height: 100 * (basePlancheJeu.width / 208.9)
        fillMode: Image.PreserveAspectFit
        anchors.right: titreDrapeau.right
        anchors.rightMargin: 15 * (basePlancheJeu.width / 208.9)
        anchors.left: titreDrapeau.left
        anchors.leftMargin: 15 * (basePlancheJeu.width / 208.9)
        anchors.top: titreDrapeau.bottom
        anchors.topMargin: 13 * (basePlancheJeu.width / 208.9)
    }

    Rectangle {
        id: marginRect
        width: (300 * (basePlancheJeu.width / 208.9))
    }

    Text {
        id: timerTitle
        text: "Timer"
        font.pointSize: (16 * (basePlancheJeu.width / 208.9) > 0 ? 16 * (basePlancheJeu.width / 208.9) : 16)
        anchors.left: marginRect.right
        anchors.right: titreDrapeau.left
        anchors.top: zoneReponse.bottom
    }

    Item {
        Text {
            id: timer
            objectName: "timer"
            text: timer.secsToString()

            property int secs: 0

            function secsToString() {
                var minutes = Math.floor(secs/60)
                var seconds = secs % 60
                var secsStr = (minutes < 10 ? "0" : "" ) + minutes.toString()
                secsStr += ":"
                secsStr += (seconds < 10 ? "0" : "" ) + seconds.toString()
                return secsStr
            }

            font.pointSize: (16 * (basePlancheJeu.width / 208.9) > 0 ? 16 * (basePlancheJeu.width / 208.9) : 16)
        }

        anchors.right: timerTitle.right
        anchors.left: timerTitle.left
        anchors.top: timerTitle.bottom
        visible: true
        clip: false
        
        Rectangle {
            id: afterTimerRect
            anchors.top: timer.bottom
            height: (20 * (basePlancheJeu.width / 208.9))
        }
        Rectangle {
            id: startButtonRect
            color: "grey"
            width: 100; height: 30
            anchors.top: afterTimerRect.bottom

            D3T12StartButton {
                id: startButton
            }

            Text{
                text: "Start"
            }

            MouseArea{
                anchors.fill: parent
                onClicked: startButton.clickButton();

                hoverEnabled: true
                onEntered: parent.color = "blue"
                onExited:  parent.color = "grey"
            }
        }
        Rectangle {
            id: afterStartRect
            anchors.top: startButtonRect.bottom
            height: (20 * (basePlancheJeu.width / 208.9))
        }
        Rectangle {
            id: countryOkButtonRect
            color: "green"
            width: 100; height: 30
            anchors.top: afterStartRect.bottom

            D3T12CountryOkButton {
                id: countryOkButton
            }

            Text{
                text: "Country OK"
            }

            MouseArea{
                anchors.fill: parent
                onClicked: countryOkButton.clickButton();

                hoverEnabled: true
                onEntered: parent.color = "blue"
                onExited:  parent.color = "green"
            }
        }
        Rectangle {
            id: afterOkRect
            anchors.top: countryOkButtonRect.bottom
            height: (20 * (basePlancheJeu.width / 208.9))
        }
        Rectangle {
            color: "red"
            width: 100; height: 30
            anchors.top: afterOkRect.bottom

            D3T12BadCountryButton {
                id: badCountryButton
            }

            Text{
                text: "Bad Country"
            }

            MouseArea{
                anchors.fill: parent
                onClicked: badCountryButton.clickButton();

                hoverEnabled: true
                onEntered: parent.color = "blue"
                onExited:  parent.color = "red"
            }
        }
    }
}

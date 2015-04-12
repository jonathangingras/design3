// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

Rectangle {

    id: rectangle2
    width: 800
    height: 480
    radius: 0
    clip: false
    smooth: false
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
        anchors.leftMargin: 7
        border.width: 4
        border.color: "#000000"
        width: height /1.869

        Rectangle {
            id: zoneDrapeau
            y: 269

            color: "#ffffff"
            anchors.left: parent.left
            anchors.leftMargin: 43
            anchors.right: parent.right
            anchors.rightMargin: 45
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 43
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

    Text {
        id: titrePlancheJeu
        x: 82
        y: 15
        text: qsTr("Planche de jeu")
        anchors.right: basePlancheJeu.right
        anchors.rightMargin: 75
        anchors.left: basePlancheJeu.left
        anchors.leftMargin: 75
        anchors.top: basePlancheJeu.top
        anchors.topMargin: -20
        anchors.bottom: basePlancheJeu.top
        anchors.bottomMargin: 5
        font.pixelSize: 30 * (width / basePlancheJeu.width)

        font.family: "Ubuntu"
        horizontalAlignment: Text.AlignLeft
    }

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
        anchors.leftMargin: 7
        border.width: 4
        border.color: "#000000"
        width: height /1.869
        opacity: 0.2
    }
    Text {
        id: titreReponse
        x: 486
        y: 187
        width: 226
        height: 26
        text: qsTr("Réponse à la question :")
        anchors.rightMargin: 88 * (basePlancheJeu.width / 230)
        anchors.leftMargin: 249 * (basePlancheJeu.width / 230)
        anchors.bottomMargin: 267 * (basePlancheJeu.width / 230)
        anchors.topMargin: 127 * (basePlancheJeu.width / 230)
        font.pointSize: 16
        anchors.right: parent.right
        anchors.left: basePlancheJeu.right
        anchors.bottom: parent.bottom
        anchors.top: titreQuestion.bottom
    }

    Text {
        id: titreQuestion
        height: 25
        text: qsTr("Question d'Atlas : ")
        anchors.leftMargin: 249 * (basePlancheJeu.width / 230)
        anchors.top: parent.top
        anchors.topMargin: 35 * (basePlancheJeu.width / 230)
        anchors.right: parent.right
        anchors.rightMargin: 168 * (basePlancheJeu.width / 230)
        anchors.left: basePlancheJeu.right
        font.pointSize: 16
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
        anchors.bottomMargin: 22
        anchors.top: titreQuestion.bottom
        anchors.topMargin: 13
        border.width: 1
        border.color: "#000000"

        TextInput {
            id: question
            text: "La question de Atlas va là "
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
        anchors.bottomMargin: 206 * (basePlancheJeu.width / 230)
        anchors.top: titreReponse.bottom
        border.color: "#000000"
        anchors.topMargin: 13
        TextInput {
            id: reponseDrapeau
            x: 0
            y: 0
            text: "Le drapeau trouvé va là"
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
}

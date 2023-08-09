import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.14

ApplicationWindow {
    id: mainWindow

    signal upPressed()
    signal downPressed()
    signal leftPressed()
    signal rightPressed()
    signal spacePressed()

    function lset(i) {
        ltext.text = i;
    }

    function rset(i) {
        rtext.text = i;
    }

    visible: true

    Rectangle {
        x: 50
        y: 50
        width: 100
        height: 200
        color: "transparent"
        radius: 20
        border.color: "black"
        border.width: 4

        Label {
            id: ltext

            anchors.centerIn: parent
            font.pixelSize: 40
            text: "left"
        }

    }

    Rectangle {
        x: 250
        y: 50
        width: 100
        height: 200
        color: "transparent"
        radius: 20
        border.color: "black"
        border.width: 4

        Label {
            id: rtext

            anchors.centerIn: parent
            font.pixelSize: 40
            text: "right"
        }

    }

    Item {
        id: inner

        focus: true
        Keys.onUpPressed: {
            if (event.isAutoRepeat == false)
                mainWindow.upPressed();

        }
        Keys.onDownPressed: {
            if (event.isAutoRepeat == false)
                mainWindow.downPressed();

        }
        Keys.onLeftPressed: {
            if (event.isAutoRepeat == false)
                mainWindow.leftPressed();

        }
        Keys.onRightPressed: {
            if (event.isAutoRepeat == false)
                mainWindow.rightPressed();

        }
        Keys.onSpacePressed: {
            if (event.isAutoRepeat == false)
                mainWindow.spacePressed();

        }
    }

}

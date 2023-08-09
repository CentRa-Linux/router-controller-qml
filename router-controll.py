# -*- coding: utf-8 -*-
import sys
import subprocess
import requests
from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickItem
from PySide2.QtQml import QQmlApplicationEngine, QQmlComponent


def set():
    global lm, rm, obj
    obj.lset(lm)
    obj.rset(rm)


def req():
    global lm, rm
    item_data = {"left": lm, "right": rm}
    requests.post(url, headers={}, json=item_data)
    set()


def up():
    global lm, rm
    lm = min(200, max(rm, lm) + 50)
    rm = lm
    req()
    set()


def down():
    global lm, rm
    lm = max(-200, min(rm, lm) - 50)
    rm = lm
    req()
    set()


def left():
    global lm, rm
    lm = min(max(-200, lm - 50), 200)
    rm = min(max(-200, rm + 50), 200)
    req()
    set()


def right():
    global lm, rm
    lm = min(max(-200, lm + 50), 200)
    rm = min(max(-200, rm - 50), 200)
    req()
    set()


def space():
    global lm, rm
    rm = 0
    lm = 0
    req()
    set()


url = "http://192.168.8.1:8080/operation"
lm = 0
rm = 0

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
component = QQmlComponent(engine, "main.qml")
obj = component.create()
obj.upPressed.connect(up)
obj.downPressed.connect(down)
obj.leftPressed.connect(left)
obj.rightPressed.connect(right)
obj.spacePressed.connect(space)
sys.exit(app.exec_())

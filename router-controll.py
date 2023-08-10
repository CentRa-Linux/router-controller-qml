# -*- coding: utf-8 -*-
import sys
import subprocess
import requests
from PySide2.QtCore import QUrl
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
    session.post(url, headers={}, json=item_data)
    set()


def up():
    global lm, rm
    lm = min(250, max(rm, lm) + 50)
    rm = lm
    req()
    set()


def down():
    global lm, rm
    lm = max(-250, min(rm, lm) - 50)
    rm = lm
    req()
    set()


def left():
    global lm, rm
    lm = min(max(40, lm - 50), 250)
    rm = min(max(40, rm + 50), 250)
    req()
    set()


def right():
    global lm, rm
    lm = min(max(40, lm + 50), 250)
    rm = min(max(40, rm - 50), 250)
    req()
    set()


def space():
    global lm, rm
    rm = 0
    lm = 0
    req()
    set()


url = "http://172.17.0.153:8080/operation"
lm = 0
rm = 0

session = requests.Session()
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
component = QQmlComponent(engine, QUrl("main.qml"))
obj = component.create()
obj.upPressed.connect(up)
obj.downPressed.connect(down)
obj.leftPressed.connect(left)
obj.rightPressed.connect(right)
obj.spacePressed.connect(space)
sys.exit(app.exec_())

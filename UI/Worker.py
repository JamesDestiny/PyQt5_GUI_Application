# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Worker.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Worker(object):
    def setupUi(self, Worker):
        Worker.setObjectName("Worker")
        Worker.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        Worker.setFont(font)
        Worker.setStyleSheet("\n"
"border-top:0px solid #e8f3f9;\n"
"background-image: url(:/photo/561fadc8c3567.jpg);")
        self.label = QtWidgets.QLabel(Worker)
        self.label.setGeometry(QtCore.QRect(60, 50, 61, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-image: url(:/label/timg.jpg);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Worker)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 61, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-image: url(:/label/timg.jpg);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Worker)
        self.lineEdit.setGeometry(QtCore.QRect(140, 50, 151, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;\n"
"background:white;\n"
"selection-background-color:green;\n"
"")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Worker)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 100, 151, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;\n"
"background:white;\n"
"selection-background-color:green;\n"
"")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Worker)
        self.pushButton.setGeometry(QtCore.QRect(70, 200, 75, 23))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(0, 170, 255);border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Worker)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 200, 75, 23))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(0, 170, 255);border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Worker)
        self.graphicsView_2.setGeometry(QtCore.QRect(320, 50, 81, 121))
        self.graphicsView_2.setStyleSheet("border-image: url(:/photo/snap2018-05-21-16-52-17.png);")
        self.graphicsView_2.setObjectName("graphicsView_2")

        self.retranslateUi(Worker)
        QtCore.QMetaObject.connectSlotsByName(Worker)

    def retranslateUi(self, Worker):
        _translate = QtCore.QCoreApplication.translate
        Worker.setWindowTitle(_translate("Worker", "操作员登录"))
        self.label.setText(_translate("Worker", "账号"))
        self.label_2.setText(_translate("Worker", "密码"))
        self.pushButton.setText(_translate("Worker", "确认"))
        self.pushButton_2.setText(_translate("Worker", "取消"))

import qrc.plane_rc
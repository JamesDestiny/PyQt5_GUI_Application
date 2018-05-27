# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OrP_zc.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OrP_zc(object):
    def setupUi(self, OrP_zc):
        OrP_zc.setObjectName("OrP_zc")
        OrP_zc.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        OrP_zc.setFont(font)
        OrP_zc.setStyleSheet("\n"
"border-top:0px solid #e8f3f9;\n"
"background-image: url(:/photo/561fadc8c3567.jpg);")
        self.label = QtWidgets.QLabel(OrP_zc)
        self.label.setGeometry(QtCore.QRect(60, 50, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-image: url(:/label/timg.jpg);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(OrP_zc)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 81, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-image: url(:/label/timg.jpg);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(OrP_zc)
        self.lineEdit.setGeometry(QtCore.QRect(140, 60, 171, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;\n"
"background:white;\n"
"selection-background-color:green;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(OrP_zc)
        self.lineEdit_2.setGeometry(QtCore.QRect(142, 120, 171, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;\n"
"background:white;\n"
"selection-background-color:green;\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(OrP_zc)
        self.pushButton.setGeometry(QtCore.QRect(70, 200, 75, 23))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(0, 170, 255);border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(OrP_zc)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 200, 75, 23))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(0, 170, 255);border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(OrP_zc)
        self.graphicsView_2.setGeometry(QtCore.QRect(320, 30, 81, 121))
        self.graphicsView_2.setStyleSheet("border-image: url(:/photo/snap2018-05-21-16-52-17.png);")
        self.graphicsView_2.setObjectName("graphicsView_2")

        self.retranslateUi(OrP_zc)
        QtCore.QMetaObject.connectSlotsByName(OrP_zc)

    def retranslateUi(self, OrP_zc):
        _translate = QtCore.QCoreApplication.translate
        OrP_zc.setWindowTitle(_translate("OrP_zc", "普通用户注册"))
        self.label.setText(_translate("OrP_zc", "姓名"))
        self.label_2.setText(_translate("OrP_zc", "身份证号"))
        self.pushButton.setText(_translate("OrP_zc", "确认"))
        self.pushButton_2.setText(_translate("OrP_zc", "取消"))

import qrc.plane_rc

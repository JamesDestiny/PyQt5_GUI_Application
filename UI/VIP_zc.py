# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VIP_zc.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VIP_zc(object):
    def setupUi(self, VIP_zc):
        VIP_zc.setObjectName("VIP_zc")
        VIP_zc.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        VIP_zc.setFont(font)
        VIP_zc.setStyleSheet("\n"
"border-top:0px solid #e8f3f9;\n"
"background-image: url(:/photo/561fadc8c3567.jpg);")
        self.label = QtWidgets.QLabel(VIP_zc)
        self.label.setGeometry(QtCore.QRect(60, 50, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-image: url(:/label/timg.jpg);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(VIP_zc)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-image: url(:/label/timg.jpg);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(VIP_zc)
        self.lineEdit.setGeometry(QtCore.QRect(160, 60, 151, 20))
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
        self.lineEdit_2 = QtWidgets.QLineEdit(VIP_zc)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 120, 151, 20))
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
        self.label_3 = QtWidgets.QLabel(VIP_zc)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 71, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-image: url(:/label/timg.jpg);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(VIP_zc)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 180, 151, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;\n"
"background:white;\n"
"selection-background-color:green;\n"
"")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(VIP_zc)
        self.pushButton.setGeometry(QtCore.QRect(80, 240, 75, 23))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(0, 170, 255);border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(VIP_zc)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 240, 75, 23))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(0, 170, 255);border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView = QtWidgets.QGraphicsView(VIP_zc)
        self.graphicsView.setGeometry(QtCore.QRect(320, 50, 81, 121))
        self.graphicsView.setStyleSheet("border-image: url(:/photo/snap2018-05-21-16-52-17.png);")
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(VIP_zc)
        QtCore.QMetaObject.connectSlotsByName(VIP_zc)

    def retranslateUi(self, VIP_zc):
        _translate = QtCore.QCoreApplication.translate
        VIP_zc.setWindowTitle(_translate("VIP_zc", "VIP用户注册"))
        self.label.setText(_translate("VIP_zc", "姓名"))
        self.label_2.setText(_translate("VIP_zc", "身份证号"))
        self.label_3.setText(_translate("VIP_zc", "邀请码"))
        self.pushButton.setText(_translate("VIP_zc", "确认"))
        self.pushButton_2.setText(_translate("VIP_zc", "取消"))

import qrc.plane_rc

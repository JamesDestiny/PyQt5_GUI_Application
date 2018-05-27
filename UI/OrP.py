# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OrP.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OrP(object):
    def setupUi(self, OrP):
        OrP.setObjectName("OrP")
        OrP.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        OrP.setFont(font)
        OrP.setStyleSheet("\n"
"border-top:0px solid #e8f3f9;\n"
"background-image: url(:/photo/561fadc8c3567.jpg);")
        self.label = QtWidgets.QLabel(OrP)
        self.label.setGeometry(QtCore.QRect(50, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-image: url(:/label/timg.jpg);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(OrP)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 81, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-image: url(:/label/timg.jpg);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(OrP)
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
        self.lineEdit_2 = QtWidgets.QLineEdit(OrP)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 110, 171, 20))
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
        self.layoutWidget = QtWidgets.QWidget(OrP)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 190, 239, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(0, 170, 255);border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(0, 170, 255);border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:rgb(0, 170, 255);border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.graphicsView = QtWidgets.QGraphicsView(OrP)
        self.graphicsView.setGeometry(QtCore.QRect(320, 30, 81, 121))
        self.graphicsView.setStyleSheet("border-image: url(:/photo/snap2018-05-21-16-52-17.png);")
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(OrP)
        QtCore.QMetaObject.connectSlotsByName(OrP)

    def retranslateUi(self, OrP):
        _translate = QtCore.QCoreApplication.translate
        OrP.setWindowTitle(_translate("OrP", "普通用户登录"))
        self.label.setText(_translate("OrP", "姓名"))
        self.label_2.setText(_translate("OrP", "身份证号"))
        self.pushButton.setText(_translate("OrP", "确认"))
        self.pushButton_2.setText(_translate("OrP", "注册"))
        self.pushButton_3.setText(_translate("OrP", "取消"))

import qrc.plane_rc

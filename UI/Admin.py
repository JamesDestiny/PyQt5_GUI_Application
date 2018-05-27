# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        Admin.setFont(font)
        Admin.setStyleSheet("\n"
"border-top:0px solid #e8f3f9;\n"
"background-image: url(:/photo/561fadc8c3567.jpg);")
        self.label = QtWidgets.QLabel(Admin)
        self.label.setGeometry(QtCore.QRect(50, 50, 61, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/label/timg.jpg);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Admin)
        self.lineEdit.setGeometry(QtCore.QRect(130, 50, 151, 20))
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
        self.lineEdit_2 = QtWidgets.QLineEdit(Admin)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 100, 151, 20))
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
        self.pushButton = QtWidgets.QPushButton(Admin)
        self.pushButton.setGeometry(QtCore.QRect(70, 180, 75, 23))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(0, 170, 255);border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Admin)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 180, 75, 23))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(0, 170, 255);border: 2px solid rgb(41,57,85);\n"
"border-radius:6px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Admin)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-image: url(:/label/timg.jpg);")
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(Admin)
        self.graphicsView.setGeometry(QtCore.QRect(290, 30, 81, 121))
        self.graphicsView.setStyleSheet("border-image: url(:/photo/snap2018-05-21-16-52-17.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.label.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.graphicsView.raise_()

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "登录"))
        self.label.setText(_translate("Admin", "用户名"))
        self.pushButton.setText(_translate("Admin", "确认"))
        self.pushButton_2.setText(_translate("Admin", "取消"))
        self.label_2.setText(_translate("Admin", "密码"))
import qrc.plane_rc

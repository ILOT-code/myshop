# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectLogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SelectLogin(object):
    def setupUi(self, SelectLogin):
        SelectLogin.setObjectName("SelectLogin")
        SelectLogin.setEnabled(True)
        SelectLogin.resize(852, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dut.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SelectLogin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SelectLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 110, 531, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 211, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        SelectLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SelectLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 22))
        self.menubar.setObjectName("menubar")
        SelectLogin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SelectLogin)
        self.statusbar.setObjectName("statusbar")
        SelectLogin.setStatusBar(self.statusbar)

        self.retranslateUi(SelectLogin)
        QtCore.QMetaObject.connectSlotsByName(SelectLogin)

    def retranslateUi(self, SelectLogin):
        _translate = QtCore.QCoreApplication.translate
        SelectLogin.setWindowTitle(_translate("SelectLogin", "选择登录方式"))
        self.pushButton_2.setText(_translate("SelectLogin", "用户登录"))
        self.pushButton_4.setText(_translate("SelectLogin", "用户注册"))
        self.pushButton_3.setText(_translate("SelectLogin", "管理员登录"))
        self.pushButton.setText(_translate("SelectLogin", "退出"))
        self.label.setText(_translate("SelectLogin", "请选择登录方式"))

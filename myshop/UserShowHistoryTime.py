# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserShowHistoryTime.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserShowHistoryTime(object):
    def setupUi(self, UserShowHistoryTime):
        UserShowHistoryTime.setObjectName("UserShowHistoryTime")
        UserShowHistoryTime.resize(527, 407)
        self.label_3 = QtWidgets.QLabel(UserShowHistoryTime)
        self.label_3.setGeometry(QtCore.QRect(23, 10, 221, 71))
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(UserShowHistoryTime)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 90, 381, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 2)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 0, 1, 1, 3)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout.addWidget(self.dateTimeEdit_2, 1, 1, 1, 3)

        self.retranslateUi(UserShowHistoryTime)
        QtCore.QMetaObject.connectSlotsByName(UserShowHistoryTime)

    def retranslateUi(self, UserShowHistoryTime):
        _translate = QtCore.QCoreApplication.translate
        UserShowHistoryTime.setWindowTitle(_translate("UserShowHistoryTime", "Dialog"))
        self.label_3.setText(_translate("UserShowHistoryTime", "请选择时间区间"))
        self.label.setText(_translate("UserShowHistoryTime", "开始时间"))
        self.label_2.setText(_translate("UserShowHistoryTime", "截至时间"))
        self.pushButton.setText(_translate("UserShowHistoryTime", "确定"))

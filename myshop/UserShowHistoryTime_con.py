from PyQt5 import QtGui, QtWidgets, QtCore

from UserShowHistoryTime import Ui_UserShowHistoryTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QTableWidgetItem
from dbservice.service import query, query2, exec
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import Qt, pyqtSignal


class UserShowHistoryTime(QDialog, Ui_UserShowHistoryTime):
    def __init__(self, userid):
        super(UserShowHistoryTime, self).__init__()
        self.userid = userid
        self.setupUi(self)

        self.pushButton.clicked.connect(self.returntime)
        #设置dateEdit和dateEdit_2的时间范围为现在
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())


    def returntime(self):
        self.start_time = self.dateTimeEdit.dateTime()
        self.end_time = self.dateTimeEdit_2.dateTime()
        self.accept()

from PyQt5.QtCore import pyqtSignal

from SelectLogin import Ui_SelectLogin
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from UserLogin_con import UserLogin
from AdminLogin_con import AdminLogin
from UserRegister_con import UserRegister
from PyQt5 import QtCore, QtGui, QtWidgets


class SelectLogin(QMainWindow, Ui_SelectLogin):
    suclogin = pyqtSignal(str, int)
    def __init__(self, parent=None):
        super(SelectLogin, self).__init__(parent)
        self.idallow = None
        self.logtype = None


        self.setupUi(self)

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.Userlogin)
        self.pushButton_3.clicked.connect(self.Adminlogin)
        self.pushButton_4.clicked.connect(self.Userregister)

    def Userlogin(self):
        self.logtype = "Userlogin"
        self.userlogin = UserLogin()
        self.userlogin.show()
        if self.userlogin.exec_() == QDialog.Accepted:
            self.idallow = self.userlogin.idallow
            self.suclogin.emit(self.logtype, self.idallow)



    def Adminlogin(self):
        self.logtype = "Adminlogin"
        self.adminlogin = AdminLogin()
        self.adminlogin.show()
        if self.adminlogin.exec_() == QDialog.Accepted:
            self.idallow = self.adminlogin.idallow
            self.suclogin.emit(self.logtype, self.idallow)


    def Userregister(self):
        self.logtype = "Userregister"
        self.userregister = UserRegister()
        self.userregister.show()
        self.userregister.exec_()






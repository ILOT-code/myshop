from PyQt5 import QtCore, QtWidgets

from UserLogin import Ui_UserLogin
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QMessageBox
from dbservice.service import query


class UserLogin(QDialog, Ui_UserLogin):
    def __init__(self, parent=None):
        super(UserLogin, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.__check_in)
        self.checkBox.stateChanged.connect(self.Showpassword)

    def Showpassword(self, state):
        if state == QtCore.Qt.Checked:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def __check_in(self):
        # print("登录成功？")
        try:
            userid = int(self.lineEdit.text())
            password = self.lineEdit_2.text()
            # print(userid, password)

            sql = "select * from users where id = %s and password = %s"
            result = query(sql, userid, password)
            if result:
                QMessageBox.about(None, "提示:", "登录成功")
                self.idallow = userid
                self.accept()
            else:
                QMessageBox.about(None, "提示:", "账号或密码错误")

        except:
            QMessageBox.information(None, "提示:", "操作失败，请检查文本输入是否正确;")

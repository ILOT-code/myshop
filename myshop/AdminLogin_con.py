from AdminLogin import Ui_AdminLogin
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QMessageBox, QLineEdit

from dbservice.service import query


class AdminLogin(QDialog, Ui_AdminLogin):
    def __init__(self, parent=None):
        super(AdminLogin, self).__init__(parent)
        self.setupUi(self)

        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton_2.clicked.connect(self.__Login)
        self.checkBox.stateChanged.connect(self.__showpassword)

    def __Login(self):
        # printf("管理员登录")
        try:
            adminid = int(self.lineEdit.text())
            adminpassword = self.lineEdit_2.text()
            sql = "select * from admins where id = %s and password = %s"
            result = query(sql, adminid, adminpassword)

            if result:
                QMessageBox.about(None, "提示:", "登录成功")
                self.idallow = adminid
                self.accept()
            else:
                QMessageBox.about(None, "提示:", "账号或密码错误")

        except:
            QMessageBox.information(None, "提示:", "操作失败，请检查文本输入是否正确;")

    def __showpassword(self):
        if self.checkBox.isChecked():
            self.lineEdit_2.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_2.setEchoMode(QLineEdit.Password)

from UserRegister import Ui_UserRegister
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QMessageBox
from dbservice.service import query, query2, exec, exec_getid


class UserRegister(QDialog, Ui_UserRegister):
    def __init__(self, parent=None):
        super(UserRegister, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.__Register)

    def __Register(self):
        # printf("注册成功")
        try:
            username = self.lineEdit.text()
            userpassword = self.lineEdit_2.text()
            usergender = self.comboBox.currentText()
            userphone = self.lineEdit_4.text()
            useraddress = self.lineEdit_5.text()
            if username == "" or userpassword == "" or usergender == "" or userphone == "" or useraddress == "":
                QMessageBox.about(None, "提示:", "输入不能为空")
                return
            # print(username, userpassword, usergender, userphone, useraddress)
            sql = "insert into users (name,password,phone,address,gender) values (%s,%s,%s,%s,%s)"
            returnid = exec_getid(sql, (username, userpassword, userphone, useraddress, usergender))
            QMessageBox.about(None, "提示:", "注册成功，您的账号为：%d" % returnid)
            self.close()
        except:
            QMessageBox.about(None, "提示:", "操作失败，请检查文本输入是否正确;")

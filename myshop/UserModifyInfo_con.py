from PyQt5 import QtGui, QtWidgets

from UserModifyInfo import Ui_UserModifyInfo
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QTableWidgetItem
from dbservice.service import query, query2, exec, exec_getid
from PyQt5.QtWidgets import QAbstractItemView


class UserModifyInfo(QWidget, Ui_UserModifyInfo):
    def __init__(self, userid):
        super(UserModifyInfo, self).__init__()
        self.setupUi(self)
        self.userid = userid
        self.pushButton.clicked.connect(self.Modifyname)
        self.pushButton_2.clicked.connect(self.Modifypassward)
        self.pushButton_3.clicked.connect(self.Modifyphone)
        self.pushButton_4.clicked.connect(self.Modifyaddress)
        self.pushButton_5.clicked.connect(self.Modifygender)

    def Modifyname(self):
        newname = self.lineEdit.text()
        oldname = query("select name from users where id = %s", self.userid)[0][0]
        if newname == "":
            QtWidgets.QMessageBox.information(self, "提示", "新的用户名不能为空！")
            return
        if newname == oldname:
            QtWidgets.QMessageBox.information(self, "提示", "新的用户名不能与原用户名相同！")
            return
        sql = "update users set name = %s where id = %s"
        exec(sql, (newname, self.userid))
        QtWidgets.QMessageBox.information(self, "提示", "用户名修改成功！\n新的用户名为：%s" % newname)

    def Modifypassward(self):
        newpassward = self.lineEdit_2.text()
        oldpassward = query("select password from users where id = %s", self.userid)[0][0]
        if newpassward == "":
            QtWidgets.QMessageBox.information(self, "提示", "新的密码不能为空！")
            return
        if newpassward == oldpassward:
            QtWidgets.QMessageBox.information(self, "提示", "新的密码不能与原密码相同！")
            return
        sql = "update users set password = %s where id = %s"
        exec(sql, (newpassward, self.userid))
        QtWidgets.QMessageBox.information(self, "提示", "密码修改成功！\n新的密码为：%s" % newpassward)

    def Modifyphone(self):
        newphone = self.lineEdit_3.text()
        oldphone = query("select phone from users where id = %s", self.userid)[0][0]
        if newphone == "":
            QtWidgets.QMessageBox.information(self, "提示", "新的手机号不能为空！")
            return
        if newphone == oldphone:
            QtWidgets.QMessageBox.information(self, "提示", "新的手机号不能与原手机号相同！")
            return
        sql = "update users set phone = %s where id = %s"
        exec(sql, (newphone, self.userid))
        QtWidgets.QMessageBox.information(self, "提示", "手机号修改成功！\n新的手机号为：%s" % newphone)

    def Modifyaddress(self):
        newaddress = self.lineEdit_4.text()
        oldaddress = query("select address from users where id = %s", self.userid)[0][0]
        if newaddress == "":
            QtWidgets.QMessageBox.information(self, "提示", "新的地址不能为空！")
            return
        if newaddress == oldaddress:
            QtWidgets.QMessageBox.information(self, "提示", "新的地址不能与原地址相同！")
            return
        sql = "update users set address = %s where id = %s"
        exec(sql, (newaddress, self.userid))
        QtWidgets.QMessageBox.information(self, "提示", "地址修改成功！\n新的地址为：%s" % newaddress)


    def Modifygender(self):
        newgender = self.comboBox.currentText()
        oldgender = query("select gender from users where id = %s", self.userid)[0][0]
        if newgender == oldgender:
            QtWidgets.QMessageBox.information(self, "提示", "新的性别不能与原性别相同！")
            return
        sql = "update users set gender = %s where id = %s"
        exec(sql, (newgender, self.userid))
        QtWidgets.QMessageBox.information(self, "提示", "性别修改成功！\n新的性别为：%s" % newgender)

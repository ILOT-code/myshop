from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QTableWidgetItem, QAbstractItemView, \
    QMessageBox

from AdminMain import Ui_AdminMain
from AddProduct_con import AddProduct
from UserShowHistoryTime_con import UserShowHistoryTime
from dbservice.service import query, query2, exec, exec_getid


class AdminMain(QMainWindow, Ui_AdminMain):
    def __init__(self, adminid):
        super(AdminMain, self).__init__()
        self.adminid = adminid
        self.setupUi(self)
        self.setWindowTitle("管理员账号：%d" % adminid)
        self.tabWidget.setCurrentIndex(0)


        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setColumnWidth(5, 400)
        self.tableWidget.setHorizontalHeaderLabels(['ID', '名称', '余量', '原价', '折扣价', '折扣时截至时间'])
        self.tableWidget.cellClicked.connect(self.showmes)

        self.settable()

        self.pushButton_7.clicked.connect(self.searchbyname)
        self.pushButton_2.clicked.connect(self.addstock)
        self.pushButton_8.clicked.connect(self.modifyinfo)
        self.pushButton_9.clicked.connect(self.modifyname)
        self.pushButton_6.clicked.connect(self.setdiscounted)
        self.pushButton_4.clicked.connect(self.settable)
        self.pushButton_5.clicked.connect(self.addproduct)
        self.pushButton_3.clicked.connect(self.deleteproduct)

        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setColumnWidth(0, 150)
        self.tableWidget_2.setColumnWidth(1, 150)
        self.tableWidget_2.setColumnWidth(2, 250)
        self.tableWidget_2.setColumnWidth(3, 300)
        self.tableWidget_2.setHorizontalHeaderLabels(['订单编号', '用户编号', '总价', '下单时间'])
        self.tableWidget_2.cellClicked.connect(self.showitems)
        self.settable_2()
        self.spinBox.setRange(0, 1000000)

        self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setHorizontalHeaderLabels(['商品ID', '名称', '购入单价', '数量', '总价'])
        self.tableWidget_3.setColumnWidth(0, 150)
        self.tableWidget_3.setColumnWidth(1, 200)

        # 将combox的选项连接到相应的函数
        self.comboBox.currentIndexChanged.connect(self.sortby_2)
        self.pushButton_10.clicked.connect(self.searchbyuserid)
        self.pushButton_12.clicked.connect(self.settable_2)
        self.pushButton_11.clicked.connect(self.searchbytime)

        self.spinBox_2.setRange(0, 1000000)
        self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setHorizontalHeaderLabels(['用户ID', '名称', '性别', '电话', '地址'])
        self.tableWidget_4.setColumnWidth(0, 150)
        self.tableWidget_4.setColumnWidth(3, 300)
        self.tableWidget_4.setColumnWidth(4, 300)
        self.settable_3()

        self.pushButton_13.clicked.connect(self.searchbyuserid_2)
        self.pushButton_14.clicked.connect(self.deleteuser)
        self.pushButton_15.clicked.connect(self.adduser)
        self.pushButton_16.clicked.connect(self.settable_3)

        self.spinBox_3.setRange(0, 1000000)
        self.tableWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_5.verticalHeader().setVisible(False)
        self.tableWidget_5.setColumnCount(3)
        self.settable_4()

        self.pushButton_17.clicked.connect(self.searchbyadminid)
        self.pushButton_18.clicked.connect(self.settable_4)
        self.pushButton_19.clicked.connect(self.addadmin)
        self.pushButton_20.clicked.connect(self.deleteadmin)

    def settable(self):
        sql = "select * from product_discounts"
        self.result = query(sql)
        self.result = sorted(self.result, key=lambda x: x[0])
        self.tableWidget.setRowCount(len(self.result))
        for i in range(len(self.result)):
            for j in range(6):
                if j == 5 and self.result[i][j] is None:
                    item = QTableWidgetItem("无折扣")
                else:
                    item = QTableWidgetItem(str(self.result[i][j]))
                self.tableWidget.setItem(i, j, item)

    def settable_2(self):
        sql = "select * from orders"
        self.result2 = query(sql)
        self.result2 = sorted(self.result2, key=lambda x: x[0])
        self.tableWidget_2.setRowCount(len(self.result2))
        for i in range(len(self.result2)):
            for j in range(4):
                item = QTableWidgetItem(str(self.result2[i][j]))
                self.tableWidget_2.setItem(i, j, item)

    def settable_3(self):
        sql = "select id,name,gender,phone,address from users"
        self.result3 = query(sql)
        self.result3 = sorted(self.result3, key=lambda x: x[0])
        self.tableWidget_4.setRowCount(len(self.result3))
        for i in range(len(self.result3)):
            for j in range(5):
                item = QTableWidgetItem(str(self.result3[i][j]))
                self.tableWidget_4.setItem(i, j, item)

    def settable_4(self):
        sql = "select * from admins"
        self.result4 = query(sql)
        self.result4 = sorted(self.result4, key=lambda x: x[0])
        self.tableWidget_5.setRowCount(len(self.result4))
        for i in range(len(self.result4)):
            for j in range(3):
                item = QTableWidgetItem(str(self.result4[i][j]))
                self.tableWidget_5.setItem(i, j, item)

    def settable_nore(self):
        self.tableWidget.setRowCount(len(self.result))
        for i in range(len(self.result)):
            for j in range(6):
                if j == 5 and self.result[i][j] is None:
                    item = QTableWidgetItem("无折扣")
                else:
                    item = QTableWidgetItem(str(self.result[i][j]))
                self.tableWidget.setItem(i, j, item)

    def showmes(self, row, col):
        self.textEdit.clear()
        self.textEdit.append(self.result[row][6])
        self.lineEdit_2.setText(self.result[row][1])

        id = self.result[row][0]
        olddiscounted = query("select discount from discounts where product_id = %s", id)
        if len(olddiscounted) == 0:
            self.doubleSpinBox.setValue(0)
            self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        else:
            self.doubleSpinBox.setValue(olddiscounted[0][0])
            self.dateTimeEdit.setDateTime(self.result[row][5])

    def searchbyname(self):
        name = self.lineEdit.text()
        sql = "select * from product_discounts where name like '%%%s%%'" % name
        self.result = query2(sql)
        self.result = sorted(self.result, key=lambda x: x[0])
        self.settable_nore()

    def addstock(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            return
        id = self.result[row][0]
        sql = "update products set stock = stock + 1 where id = %s"
        exec(sql, (id))
        self.settable()

    def modifyinfo(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            return
        id = self.result[row][0]
        newtext = self.textEdit.toPlainText()
        oldtext = self.result[row][6]
        if newtext == oldtext:
            QtWidgets.QMessageBox.information(None, "提示", "信息不能相同")
            return
        sql = "update products set information = %s where id = %s"
        exec(sql, (newtext, id))
        QtWidgets.QMessageBox.information(None, "提示", "修改成功")
        self.settable()

    def modifyname(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            return
        id = self.result[row][0]
        newname = self.lineEdit_2.text()
        oldname = self.result[row][1]
        if newname == oldname:
            QtWidgets.QMessageBox.information(None, "提示", "名称不能相同")
            return
        sql = "update products set name = %s where id = %s"
        exec(sql, (newname, id))
        QtWidgets.QMessageBox.information(None, "提示", "修改成功")
        self.settable()

    def setdiscounted(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            return
        id = self.result[row][0]
        newend_time = self.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        newdiscounted = self.doubleSpinBox.value()
        olddiscounted = query("select discount from discounts where product_id = %s", id)
        if len(olddiscounted) == 0:
            sql = "insert into discounts (product_id,discount,end_time) values(%s, %s, \'%s\')" % (
                id, newdiscounted, newend_time)
            exec(sql, ())
            QtWidgets.QMessageBox.information(None, "提示", "设置成功")
            self.settable()
            return

        olddiscounted = olddiscounted[0][0]
        if newdiscounted == olddiscounted and newend_time == self.result[row][5]:
            QtWidgets.QMessageBox.information(None, "提示", "信息不能相同")
            return
        # 更新折扣和时间
        sql = "update discounts set discount = %s, end_time = \'%s\' where product_id = %s" % (
            newdiscounted, newend_time, id)
        exec(sql, ())
        QtWidgets.QMessageBox.information(None, "提示", "设置成功")
        self.settable()

    def addproduct(self):
        self.addproduct = AddProduct()
        self.addproduct.show()
        if self.addproduct.exec_() == QDialog.Accepted:
            self.settable()

    def deleteproduct(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            return
        id = self.result[row][0]
        sql = "delete from products where id = %s"
        returnflag = exec(sql, id)
        if returnflag == 0:
            QtWidgets.QMessageBox.information(None, "提示", "删除失败\n该商品已经有人购买而处于订单中")
            return
        QtWidgets.QMessageBox.information(None, "提示", "删除成功")
        self.settable()

    def sortby_2(self):
        # 按照选项索引来排序
        index = self.comboBox.currentIndex()
        if index == 0:
            self.result2 = sorted(self.result2, key=lambda x: x[0])
        elif index == 1:
            self.result2 = sorted(self.result2, key=lambda x: x[0], reverse=True)
        elif index == 2:
            self.result2 = sorted(self.result2, key=lambda x: x[2])
        elif index == 3:
            self.result2 = sorted(self.result2, key=lambda x: x[2], reverse=True)
        elif index == 4:
            self.result2 = sorted(self.result2, key=lambda x: x[1])

        self.tableWidget_2.setRowCount(len(self.result2))
        for i in range(len(self.result2)):
            for j in range(4):
                item = QTableWidgetItem(str(self.result2[i][j]))
                self.tableWidget_2.setItem(i, j, item)

    def searchbyuserid(self):
        userid = self.spinBox.value()
        sql = "select * from orders where user_id = %s" % userid
        self.result2 = query2(sql)
        self.tableWidget_2.setRowCount(len(self.result2))
        for i in range(len(self.result2)):
            for j in range(4):
                item = QTableWidgetItem(str(self.result2[i][j]))
                self.tableWidget_2.setItem(i, j, item)

    def searchbytime(self):
        self.settime = UserShowHistoryTime(self.adminid)
        self.settime.show()
        if self.settime.exec_() == QDialog.Accepted:
            start_time = self.settime.start_time.toString("yyyy-MM-dd hh:mm:ss")
            end_time = self.settime.end_time.toString("yyyy-MM-dd hh:mm:ss")
            sql = "select * from orders where order_time between \'%s\' and \'%s\'" % (start_time, end_time)
            self.result2 = query2(sql)
            self.tableWidget_2.setRowCount(len(self.result2))
            for i in range(len(self.result2)):
                for j in range(4):
                    item = QTableWidgetItem(str(self.result2[i][j]))
                    self.tableWidget_2.setItem(i, j, item)

    def showitems(self):
        row = self.tableWidget_2.currentRow()
        if row == -1:
            return
        order_id = self.result2[row][0]
        sql = "select product_id,name,discounted_price,quantity,total_price from orderitem_products where order_id = %s" % order_id
        result = query2(sql)
        self.tableWidget_3.setRowCount(len(result))
        for i in range(len(result)):
            for j in range(5):
                item = QTableWidgetItem(str(result[i][j]))
                self.tableWidget_3.setItem(i, j, item)

    def searchbyuserid_2(self):
        userid = self.spinBox_2.value()
        sql = "select id,name,gender,phone,address from users where id = %s" % userid
        self.result3 = query2(sql)
        self.tableWidget_4.setRowCount(len(self.result3))
        for i in range(len(self.result3)):
            for j in range(5):
                item = QTableWidgetItem(str(self.result3[i][j]))
                self.tableWidget_4.setItem(i, j, item)

    def deleteuser(self):
        row = self.tableWidget_4.currentRow()
        if row == -1:
            return
        id = self.result3[row][0]
        sql = "delete from users where id = %s"
        returnflag = exec(sql, id)
        if returnflag == 0:
            QtWidgets.QMessageBox.information(None, "提示", "删除失败\n该用户已购买商品而处于订单中")
            return
        QtWidgets.QMessageBox.information(None, "提示", "删除成功")
        self.settable_3()

    def adduser(self):
        name = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        gender = self.comboBox_2.currentText()
        phone = self.lineEdit_5.text()
        address = self.lineEdit_6.text()

        if name == "" or password == "" or gender == "" or phone == "" or address == "":
            QMessageBox.about(None, "提示:", "输入不能为空")
            return
        sql = "insert into users (name,password,phone,address,gender) values (%s,%s,%s,%s,%s)"
        returnid = exec_getid(sql, (name, password, phone, address, gender))
        QMessageBox.about(None, "提示:", "注册成功，账号为：%d" % returnid)
        self.settable_3()
    
    def searchbyadminid(self):
        id = self.spinBox_3.value()
        sql = "select * from admins where id = %s" % id
        self.result4 = query2(sql)
        self.tableWidget_5.setRowCount(len(self.result4))
        for i in range(len(self.result4)):
            for j in range(3):
                item = QTableWidgetItem(str(self.result4[i][j]))
                self.tableWidget_5.setItem(i, j, item)

    def addadmin(self):
        name = self.lineEdit_7.text()
        password = self.lineEdit_8.text()
        if name == "" or password == "":
            QMessageBox.about(None, "提示:", "输入不能为空")
            return
        sql = "insert into admins (name,password) values (%s,%s)"
        returnid = exec_getid(sql, (name, password))
        QMessageBox.about(None, "提示:", "添加成功，账号为：%d" % returnid)
        self.settable_4()
    
    def deleteadmin(self):
        row = self.tableWidget_5.currentRow()
        if row == -1:
            return
        id = self.result4[row][0]
        if id == self.adminid:
            QMessageBox.about(None, "提示:", "不能删除自己")
            return
        sql = "delete from admins where id = %s"
        exec(sql, id)
        QMessageBox.about(None, "提示:", "删除成功")
        self.settable_4()   

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = AdminMain(1002)
    ui.show()
    sys.exit(app.exec_())

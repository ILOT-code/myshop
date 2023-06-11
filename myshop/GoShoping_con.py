from PyQt5 import QtGui, QtWidgets

from GoShoping import Ui_GoShoping
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QTableWidgetItem
from dbservice.service import query, query2, exec
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import Qt


class GoShoping(QWidget, Ui_GoShoping):

    def __init__(self, userid):
        super(GoShoping, self).__init__()
        self.userid = userid
        self.setupUi(self)
        self.setWindowTitle("用户账号：%d" % userid)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setColumnWidth(5, 400)
        self.tableWidget.setHorizontalHeaderLabels(['ID', '名称', '余量', '原价', '折扣价', '折扣时截至时间'])

        sql = "select * from product_discounts"
        self.result = query(sql)
        self.result = sorted(self.result, key=lambda x: x[4])
        self.settable()

        self.tableWidget.cellClicked.connect(self.showmes)
        self.comboBox.currentIndexChanged.connect(self.sortbyprice)
        self.pushButton_4.clicked.connect(self.search)
        self.pushButton.clicked.connect(self.addtocar)

    def settable(self):
        self.tableWidget.setRowCount(len(self.result))

        for i in range(len(self.result)):
            for j in range(6):
                if j == 5 and self.result[i][j] == None:
                    item = QTableWidgetItem("无折扣")
                else:
                    item = QTableWidgetItem(str(self.result[i][j]))
                if j == 3:  # 如果是原价那一栏
                    font = QtGui.QFont()
                    font.setStrikeOut(True)  # 添加删除线
                    item.setFont(font)
                self.tableWidget.setItem(i, j, item)

    def showmes(self, row, col):
        self.textBrowser.clear()
        self.textBrowser.append(self.result[row][6])

    def sortbyprice(self, index):
        if index == 0:  # 价格升序
            self.result = sorted(self.result, key=lambda x: x[4])
        elif index == 1:  # 价格降序
            self.result = sorted(self.result, key=lambda x: x[4], reverse=True)
        elif index == 2:  # ID升序
            self.result = sorted(self.result, key=lambda x: x[0])
        elif index == 3:  # ID降序
            self.result = sorted(self.result, key=lambda x: x[0], reverse=True)
        self.settable()

    def search(self):
        name = self.lineEdit.text()
        sql = "select * from product_discounts where name like '%%%s%%'" % name
        self.result = query2(sql)
        self.settable()

    def addtocar(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            return

        if self.result[row][2] <= 0:
            QtWidgets.QMessageBox.information(self, "提示", "商品：%s \n已售空" % self.result[row][1])
            return

        product_id = self.result[row][0]
        sql = "select * from cart where user_id = %s and product_id = %s"
        result = query(sql, self.userid, product_id)

        if result:
            sql = "update cart set quantity = quantity + 1 where user_id = %s and product_id = %s"
            exec(sql, (self.userid, product_id))
        else:
            sql = "insert into cart (user_id, product_id, quantity) values(%s, %s, %s)"
            exec(sql, (self.userid, product_id, 1))

        QtWidgets.QMessageBox.information(self, "提示", "商品：%s \n添加成功" % self.result[row][1])
        self.settable()

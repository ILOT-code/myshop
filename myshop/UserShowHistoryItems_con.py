from PyQt5 import QtGui, QtWidgets, QtCore

from UserShowHistoryItems import Ui_UserShowHistoryItems
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QTableWidgetItem
from dbservice.service import query, query2, exec
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import Qt, pyqtSignal

class UserShowHistoryItems(QDialog,Ui_UserShowHistoryItems):
    def __init__(self,orderid):
        super(UserShowHistoryItems, self).__init__()
        self.orderid = orderid
        self.setupUi(self)
        self.setWindowTitle("订单编号：%d" % orderid)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['ID', '名称', '购入单价', '数量', '总价'])

        print(self.orderid)
        sql = "select product_id,name,discounted_price,quantity,total_price from orderitem_products where order_id = %s"
        self.result = query(sql, self.orderid)
        self.settable()

    def settable(self):
        self.tableWidget.setRowCount(len(self.result))

        for i in range(len(self.result)):
            for j in range(5):
                item = QTableWidgetItem(str(self.result[i][j]))
                self.tableWidget.setItem(i, j, item)


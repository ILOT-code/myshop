from PyQt5 import QtGui, QtWidgets

from UserShowHistory import Ui_UserShowHistory
from UserShowHistoryTime_con import UserShowHistoryTime
from UserShowHistoryItems_con import UserShowHistoryItems
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QTableWidgetItem
from dbservice.service import query, query2, exec
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import Qt

class UserShowHistory(QWidget,Ui_UserShowHistory):

    def __init__(self, userid):
        super(UserShowHistory, self).__init__()
        self.userid = userid
        self.setupUi(self)
        self.setWindowTitle("用户账号：%d" % userid)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnCount(3)
        #设置第三列的宽度为400
        self.tableWidget.setColumnWidth(2, 400)
        self.tableWidget.setHorizontalHeaderLabels(['订单编号', '总金额', '下单时间'])

        sql = "select order_id,total_price,order_time from orders where user_id = %s"
        self.result = query(sql, self.userid)
        self.result = sorted(self.result, key=lambda x: x[2])
        self.settable()

        self.pushButton.clicked.connect(self.searchfororder)
        self.pushButton_2.clicked.connect(self.searchbytime)
        self.pushButton_4.clicked.connect(self.reset)
        self.comboBox.currentIndexChanged.connect(self.sortby)




    def settable(self):
        self.tableWidget.setRowCount(len(self.result))

        for i in range(len(self.result)):
            for j in range(3):
                item = QTableWidgetItem(str(self.result[i][j]))
                self.tableWidget.setItem(i, j, item)

    #根据所选列的订单编号查订单详情
    def searchfororder(self):
        row = self.tableWidget.currentRow()
        order_id = self.result[row][0]
        self.usershowhistoryitem = UserShowHistoryItems(order_id)
        self.usershowhistoryitem.show()

    
    def searchbytime(self):
        self.usershowhistorytime = UserShowHistoryTime(self.userid)
        self.usershowhistorytime.show()
        if self.usershowhistorytime.exec_() == QDialog.Accepted:
            #查询时间在start_time和end_time之间的订单
            start_time = self.usershowhistorytime.start_time.toString("yyyy-MM-dd hh:mm:ss")
            end_time = self.usershowhistorytime.end_time.toString("yyyy-MM-dd hh:mm:ss")
            sql = "select order_id,total_price,order_time from orders where user_id = %s and order_time between %s and %s"
            self.result = query(sql, self.userid, start_time, end_time)
            self.settable()
        else:
            pass

    def reset(self):
        sql = "select order_id,total_price,order_time from orders where user_id = %s"
        self.result = query(sql, self.userid)
        self.result = sorted(self.result, key=lambda x: x[2])
        self.settable()

    # 利用comboBox的索引来写排序函数
    def sortby(self):
        index = self.comboBox.currentIndex()
        if index == 0:
            self.result = sorted(self.result, key=lambda x: x[2])
            self.settable()
        elif index == 1:
            self.result = sorted(self.result, key=lambda x: x[2],reverse=True)
            self.settable()
        elif index == 2:
            self.result = sorted(self.result, key=lambda x: x[1])
            self.settable()
        else:
            self.result = sorted(self.result, key=lambda x: x[1],reverse=True)
            self.settable()


            

        

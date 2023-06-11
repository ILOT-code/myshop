from PyQt5 import QtGui, QtWidgets

from GoCart import Ui_GoCart
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QTableWidgetItem
from dbservice.service import query, query2, exec, exec_getid
from PyQt5.QtWidgets import QAbstractItemView


class GoCart(QWidget, Ui_GoCart):
    def __init__(self, userid):
        super(GoCart, self).__init__()
        self.setupUi(self)
        self.userid = userid

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['ID', '名称', '单价', '数量', '存量', '总价', '已省'])
        self.settable_cart()

        self.pushButton.clicked.connect(self.sub)
        self.pushButton_2.clicked.connect(self.add)
        self.pushButton_3.clicked.connect(self.pay_all)

    def settable_cart(self):
        sql = "select product_id,name,discounted_price,quantity,stock,total_price,saved_solo from cart_products where user_id = %s"
        self.result = query(sql, self.userid)
        self.tableWidget.setRowCount(len(self.result))
        for i in range(len(self.result)):
            for j in range(7):
                item = QTableWidgetItem(str(self.result[i][j]))
                self.tableWidget.setItem(i, j, item)

    def sub(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            QtWidgets.QMessageBox.information(self, "提示", "请先选中一行！")
        if self.result[row][3] == 0:
            QtWidgets.QMessageBox.information(self, "提示", "数量已经为0，无法再减少！")
            return
        sql = "update cart set quantity = quantity - 1 where user_id = %s and product_id = %s"
        exec(sql, (self.userid, self.result[row][0]))
        self.settable_cart()

    def add(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            QtWidgets.QMessageBox.information(self, "提示", "请先选中一行！")
        if self.result[row][3] == self.result[row][4]:
            QtWidgets.QMessageBox.information(self, "提示", "数量已经达到库存上限，无法再增加！")
            return
        sql = "update cart set quantity = quantity + 1 where user_id = %s and product_id = %s"
        exec(sql, (self.userid, self.result[row][0]))
        self.settable_cart()

    def pay_all(self):
        print("pay")
        # 创建订单记录
        self.total_price = query("SELECT SUM(total_price) FROM cart_products WHERE user_id = %s", self.userid)[0][0]
        self.total_saved = query("SELECT SUM(saved_solo) FROM cart_products WHERE user_id = %s", self.userid)[0][0]
        print(self.total_price, self.total_saved)
        sql = "INSERT INTO orders (user_id, total_price) VALUES (%s, %s)"
        order_id = exec_getid(sql, (self.userid, self.total_price))


        # 获取购物车中的商品信息，并插入到订单项表中
        sql = "SELECT product_id, quantity FROM cart WHERE user_id = %s"
        result = query(sql, self.userid)
        # 检测是否超出库存
        for row in result:
            product_id, quantity = row
            stock = query("SELECT stock FROM products WHERE id = %s", product_id)[0][0]
            if stock < quantity:
                QtWidgets.QMessageBox.information(self, "提示", "商品%s库存不足！" % product_id)
                return

        for row in result:
            product_id, quantity = row
            sql = "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)"
            exec(sql, (order_id, product_id, quantity))

            # 更新商品库存信息
            sql = "UPDATE products SET stock = stock - %s WHERE id = %s"
            exec(sql, (quantity, product_id))

        # 清空购物车
        sql = "DELETE FROM cart WHERE user_id = %s"
        exec(sql, self.userid)
        QtWidgets.QMessageBox.information(self, "提示",
                                          "支付成功！\n总价：%s\n已省：%s" % (self.total_price, self.total_saved))

        # 更新购物车界面
        self.settable_cart()

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QMessageBox
from AddProduct import Ui_AddProduct
from dbservice.service import query, exec, exec_getid


class AddProduct(QDialog, Ui_AddProduct):
    def __init__(self, parent=None):
        super(AddProduct, self).__init__(parent)
        self.setupUi(self)
        self.doubleSpinBox.setRange(0, 10000000)
        self.spinBox.setRange(0, 1000000)

        self.pushButton.clicked.connect(self.__add_product)

    def __add_product(self):
        try:
            productname = self.lineEdit.text()
            productstock = self.spinBox.value()
            productprice = self.doubleSpinBox.value()
            productinfo = self.textEdit.toPlainText()
            print(productname, productstock, productprice, productinfo)
            print(type(productname), type(productstock), type(productprice), type(productinfo))

            sql = "insert into products (name,stock,product_price,information) values(%s,%s,%s,%s)"
            productid = exec_getid(sql, (productname, productstock, productprice, productinfo))
            QMessageBox.about(None, "提示:", "添加成功\n商品id为：" + str(productid))
            self.accept()
        except:
            QMessageBox.information(None, "提示:", "操作失败，请检查文本输入是否正确;")

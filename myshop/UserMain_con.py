from UserMain import Ui_UserMain
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from GoShoping_con import GoShoping
from GoCart_con import GoCart
from UserModifyInfo_con import UserModifyInfo
from UserShowHistory_con import UserShowHistory

class UserMain(QMainWindow, Ui_UserMain):

    def __init__(self,userid):
        super(UserMain, self).__init__()
        self.userid = userid
        self.setupUi(self)
        self.setWindowTitle("用户账号：%d" % userid)

        self.pushButton.clicked.connect(self.__Goshoping)
        self.pushButton_2.clicked.connect(self.__Modifymes)
        self.pushButton_3.clicked.connect(self.__Listhistory)
        self.pushButton_5.clicked.connect(self.__Gocart)
    

    def __Goshoping(self):
        self.goshoping = GoShoping(self.userid)
        self.goshoping.show()

    def __Modifymes(self):
        self.usermodifyinfo = UserModifyInfo(self.userid)
        self.usermodifyinfo.show()

    def __Listhistory(self):
        self.usershowhistory = UserShowHistory(self.userid)
        self.usershowhistory.show()

    def __Gocart(self):
        self.gocart = GoCart(self.userid)
        self.gocart.show()



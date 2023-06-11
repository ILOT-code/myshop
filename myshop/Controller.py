from SelectLogin_con import SelectLogin
from UserMain_con import UserMain
from AdminMain_con import AdminMain


class Controller:
    def __init__(self):
        self.selectlogin = SelectLogin()
        self.selectlogin.show()
        self.selectlogin.suclogin.connect(self.check_login)



    def check_login(self, logtype, idallow):
        self.selectlogin.close()

        if logtype == 'Userlogin':
            self.usermain = UserMain(idallow)
            self.usermain.show()
        if logtype == "Adminlogin":
            self.adminmain = AdminMain(idallow)
            self.adminmain.show()


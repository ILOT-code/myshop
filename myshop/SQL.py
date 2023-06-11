import pymysql


class SQLdata():
    def __init__(self):
        self.sql = None

    def connect(self):
        try:
            self.sql = pymysql.Connect(host='localhost', port=3306, user='root', password='1282542712',
                                        database='myshop', charset='utf8')
        except:
            print("error:连接db失败")
            return None
        return self.sql

    def close(self):
        self.sql.close()
        self.sql = None



mysql = SQLdata()

def GetMySql():
    return mysql

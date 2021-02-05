import pymysql
from readConfig import ReadConfig
import threading
import lock
import time




#LocalReadConfig = readConfig.ReadConfig
class myDB:
    global host, username, password, port, database, config
    host = ReadConfig().get_db("host")
    username = ReadConfig().get_db("username")
    password = ReadConfig().get_db("password")
    port = ReadConfig().get_db("port")
    database = ReadConfig().get_db("database")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database
    }
    def __init__(self):
        self.db = None
        self.cursor = None


    def connectDB(self):
        try:
            # 连接数据库
            self.db=pymysql.connect(**config)
            # 创建游标
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def executeSQL(self,sql,params):
        #lock = threading.Lock()
        #lock.acquire()
        self.connectDB()
        # executing sql游标下执行sql
        self.cursor.execute(sql, params)
        # 提交游标数据到数据库
        self.db.commit()
        return self.cursor


    def get_all(self,cursor):
        value = cursor.fetchall()


    def get_one(self,cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
       # self.connectDB()
        self.db.close()
        print("Database closed")

    def fuct(self):
        lock = threading.Lock()
        lock.acquire()
        self.executeSQL()
        lock.release()


if __name__ == "__main__":
    #lock=threading.Lock()
    #lock.acquire()
    test = myDB()

    sql="select event_id from event where code=%s"
    params =("2101150200000014",)
    a = myDB().executeSQL(sql=sql,params=params)
    res=myDB().get_one(a)
    print(res)
    #test.closeDB()


    #print(test)
    #lock.release()








"""
# 导入pymysql模块
import pymysql

# 连接database
conn = pymysql.connect(host="localhost", port=13306, user="root", password="123456", database="user_center", charset="utf8")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# print('连接对象' . cursor)
# 定义要执行的SQL语句
sql = 
CREATE TABLE USER1 (
id INT auto_increment PRIMARY KEY ,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;

# 执行SQL语句
cursor.execute(sql)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()
"""
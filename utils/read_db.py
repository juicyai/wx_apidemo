"""
读取数据库
"""
import pymysql
class ReadDB:

    conn=None #用变量管理数据库连接，实现连接共享
    #创建数据库连接
    @classmethod
    def get_conn(cls):
        if not cls.conn:
            cls.conn=pymysql

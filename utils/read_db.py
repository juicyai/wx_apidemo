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
            cls.conn=pymysql.connect("127.0.0.1","root","Aa123456","test",charset="utf8")
        return cls.conn
    #创建游标对象
    @classmethod
    def get_cursor(cls):
        return cls.get_conn().cursor()
    #关闭游标对象
    @classmethod
    def close_cursor(cls,cursor):
        #若游标不存在，关闭会抛异常
        if cursor:
            cursor.close()

    #关闭连接对象
    @classmethod
    def close_conn(cls):
        #若连接不存在，连接操作会抛异常
        if cls.conn:
            cls.conn.close()
            #关闭连接后，对象还存在内存中，可以将对象置空处理
            cls.conn=None

    #获取数据库执行语句，并执行
    @classmethod
    def get_sql_one(cls,sql):
        cursor=None
        data=None
        try:
            # 获取游标对象
            cursor = cls.get_cursor()
            cursor.execute(sql)
            data=cursor.fetchone() #获取单条结果
        except Exception as e:
            print("get_sql err: ",e)
        finally:
            cls.close_cursor(cursor)
            cls.close_conn()
            return data

    #执行sql语句，获取所有结果集
    @classmethod
    def get_sql_all(cls,sql):
        cursor = None
        data = None
        try:
            # 获取游标对象
            cursor = cls.get_cursor()
            cursor.execute(sql)
            data = cursor.fetchall()  # 获取单条结果
        except Exception as e:
            print("get_sql err: ", e)
        finally:
            cls.close_cursor(cursor)
            cls.close_conn()
            return data


    #增删改操作，需要进行事务处理，事物的提交和回滚
    @classmethod
    def update_sql(cls,sql):
        cursor = None
        #data = None
        try:
            # 获取游标对象
            cursor = cls.get_cursor()
            cursor.execute(sql)
            #data = cursor.fetchall()  # 获取单条结果
            #成功，则事务的提交
            cls.conn.commit()
        except Exception as e:
            print("get_sql err: ", e)
            #异常则，进行事务的回滚
            cls.conn.rollback()
        finally:
            cls.close_cursor(cursor)
            cls.close_conn()



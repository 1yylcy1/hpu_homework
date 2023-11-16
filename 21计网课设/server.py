import pymysql
import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class MyHandler(FTPHandler):

    def on_file_received(self, file):
        # 当有文件上传时，会触发该函数
        print('File %s has been received.' % file)

    def on_file_sent(self, file):
        # 当有文件下载时，会触发该函数
        print('File %s has been sent.' % file)
class server():
    def __init__(self):
        #首先连接数数据：
        self.s_connect_sql()
        # 设置FTP服务器的根目录
        self.FTP_ROOT = './ftp_root'
        # 如果不存在就创建一个文件夹
        if not os.path.exists(self.FTP_ROOT):
            os.makedirs(self.FTP_ROOT)

        # 设置FTP服务器的IP和端口
        self.HOST = 'localhost'
        self.PORT = 22

        # 客户端连接数据库
        self.conn_client = self.conn_client

        # 创建游标对象
        self.cursor = self.cursor

        #使用DummyAuthorizer类来管理用户账号和权限
        self.authorizer=DummyAuthorizer()

        # 创建FTP服务器的处理器
        self.handler=FTPHandler

    """2.连接数据库"""
    def s_connect_sql(self):
        self.conn_client = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='lx030312',
            database='ftp_info',
            charset='utf8mb4'
        )
        # 创建游标对象
        self.cursor = self.conn_client.cursor()

    #向FTP添加可以登陆的用户信息
    """3.添加用户信息"""
    def add_author(self):
        self.s_connect_sql()  # 连接数据库
        self.cursor.execute('SELECT * FROM users')#查询用户表中所有数据
        tmp_is = self.cursor.fetchall()#获取用户表中所有数据

        """
        FTP_ROOT：表示要添加的用户的根目录路径，类型为字符串
        第四个参数表示要添加的用户的权限，类型为字符串。默认值为 'elradfmwMT'，
        表示该用户拥有所有权限，包括读取、删除、创建、修改、移动和重命名文件等。
        """
        ## 设置FTP服务器的登录用户和密码
        for i in tmp_is:
            self.authorizer.add_user(i[1], i[2], self.FTP_ROOT, perm='elradfmwMT')
        self.handler.authorizer = self.authorizer

    """4.查看所有有权限的用户"""
    def check_users(self):
        for user in self.authorizer.user_table:
            print(user)

    """5. 运行FTP服务器"""
    def login(self):
        load_handler = MyHandler#监听文件的上传与否
        load_handler.authorizer = self.authorizer
        # 创建FTP服务器实例并启动
        server = FTPServer((self.HOST, self.PORT), self.handler)
        print('Starting FTP server on %s:%s' % (self.HOST, self.PORT))
        server.serve_forever()

    
if __name__=='__main__':
    s_test=server()
    s_test.add_author()
    s_test.login()









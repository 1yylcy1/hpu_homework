import ftplib
import pymysql
from datetime import datetime

class client():
    def __init__(self):
        self.c_connect_sql()#连接数据库
        self.host='localhost'
        self.port=22
        self.username='yeye'#初始用户名
        self.password='123456'

        # 客户端连接数据库
        self.conn_client=self.conn_client

        #创建游标对象
        self.cursor = self.cursor


        #标识客户端是否已经登陆
        self.log=False

        self.ftp=ftplib.FTP()#ftp对象

        # self.remote_file_path='./remote_file_path'

    """
    1.连接数据库+创建游标对象
    """
    def c_connect_sql(self):
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

    """
    # 先启动服务器之后再连接FTP服务器
    # 2.连接FTP服务器
    """
    def connect_ftp(self,host,port,username,password):
        self.ftp.connect(host, port)
        self.ftp.login(username, password)
        # 返回FTP连接对象
        return self.ftp



    """
    3.一个注册功能
    """
    def sign_up(self,username,password):
        self.c_connect_sql()#连接数据库
        self.username=username
        self.password=password
        if self.username=='' or self.password=='':
            return '用户名为空或密码可能为空'

        #查询数据库中是否有该用户名
        """
        fetchall函数
        返回一个由查询结果组成的列表，其中每一项都是一个元组，代表一条记录，会把查到的那一行的
        数据都返回，例如(‘yeyelcy’,'123456')，如果存在他会把账号加密码均放到一个元组中并返回
        查询不到则返回空元组
        """
        self.cursor.execute('SELECT * FROM users WHERE username=%s',(username))
        tmp_is=self.cursor.fetchall()#fetchall用来一次性查询结果

        # 如果用户名存在则返回True，如果不存在则返回false
        if bool(tmp_is):
            print('用户名已经存在，请勿重复注册')
            return '用户名已经存在，请勿重复注册'
        else:
            self.cursor.execute('INSERT INTO users(username,password) VALUES(%s,%s)',(self.username,self.password))

        self.conn_client.commit()#提交
        # self.conn_client.close()#关闭

    """
    4.一个登陆功能
    """
    def sign_in(self,HOST,PORT,username,password):
        self.c_connect_sql()  # 连接数据库

        """
        登陆成功后就将用户名和密码赋值给了client对象的属性
        """
        self.username = username
        self.password = password
        if self.username == '' or self.password == '':
            print('用户名为空或密码可能为空')
        else:
            self.cursor.execute('SELECT * FROM users WHERE username=%s', (username))
            tmp_is = self.cursor.fetchall()  # fetchall用来一次性查询结果

            # 如果用户名存在则返回True，如果不存在则返回false
            if bool(tmp_is):
                #如果存在账户，则进行连接FTP请求
                #账号密码正确且均为字符串类型
                self.connect_ftp(HOST,PORT,self.username,self.password)
                self.log=True#标识已经登陆
                self.ftp.set_pasv(True)
                return self.ftp
            else:
                print('查无此用户')


    """
    5. 上传文件功能，remote_path指的是目标文件夹中的文件，local_path指的是下载到本地的文件夹
    """

    def ftp_upload(self,ftp,local_file_path):
        if self.log:
            # 打开本地文件并上传到FTP服务器
            a = local_file_path.split('/')  # a是要上传的文件名
            print(f'要上传的文件名为{a}')
            with open(local_file_path, 'rb') as fp:
                #这个ftp默认如果已经登陆的话就会被拥有
                ftp.storbinary('STOR ' + a[-1], fp)  # 往服务器中上传文件
        else:
            print('请您登陆之后再操作')



        # 记录上传信息到数据库
        op='up_load'
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #获取当前时间
        now=str(now)
        # print(type(now))
        print([self.username,a[-1], op, now])#注意a[-1]才是文件名
        a[-1]=str(a[-1])
        self.conn_client.autocommit(True)
        self.cursor.execute('INSERT INTO downloads (username,filename,op,time) VALUES (%s, %s, %s, %s)', (self.username, a[-1], op, now))

        print("upload  successfully")
        self.conn_client.commit()
        self.conn_client.close()  # 关闭

        # 关闭FTP连接
        # self.ftp.quit()
    """
    6. 下载文件功能
    """

    #LOCAL_FILE_PATH是文件要下载到的文件夹
    def ftp_download(self,ftp,local_file_path, remote_file_path):

        if self.log:

            # 打开本地文件并从FTP服务器下载
            a = remote_file_path.split('/')
            # print(local_file_path + '/' + a[-1])
            # print(remote_file_path)

            with open(local_file_path + '/' + a[-1], 'wb') as fp:
                # print('what?')
                ftp.retrbinary('RETR ' + remote_file_path, fp.write)
            # print('hello?')
        else:
            print('请你登陆后再操作')



        #记录下载/上传文件信息
        op='down_load'
        now = datetime.now()
        formatted = now.strftime("%Y-%m-%d %H:%M:%S")
        # print(type(formatted))
        self.cursor.execute('INSERT INTO downloads(username, filename, op,time) VALUES (%s, %s, %s, %s)',
                             (self.username, a[-1], op,formatted))

        print(f"Downlload file {remote_file_path}: successfully")

        # print("download  successfully")
        self.conn_client.commit()

        # 关闭FTP连接
        # self.ftp.quit()

if __name__=='__main__':

      test=client()
      ftp=test.sign_in('172.19.96.1',22,'yeyelcy','123456')#登陆
      test.ftp_upload(ftp,'./local_file_path/周杰伦-告白气球.mp3')#上传文件
      # # test.ftp_download(ftp,'./local_file_path','周杰伦-告白气球.mp3')#下载文件
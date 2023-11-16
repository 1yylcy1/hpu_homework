from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout, QGroupBox,QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

from client import client
from win_client import MainWindow

# from win_main import MainWindow
import sys


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle('Login')
        self.resize(400, 600)

        # 设定背景图和整体布局占比
        background = QLabel(self)
        pixmap = QPixmap('background.jpg')
        background.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        # 创建控件
        logo_label = QLabel(self)
        logo_label.setPixmap(QPixmap('./WIN_ico/logo.png'))
        logo_label.setAlignment(Qt.AlignCenter)

        title_label = QLabel(self)
        title_label.setText('Sign in to FTP')
        title_label.setAlignment(Qt.AlignCenter)


        #用户名输入框
        self.username_edit = QLineEdit(self)
        self.username_edit.setPlaceholderText('Enter your username')
        self.username_edit.setText('yeyelcy')

        #密码输入框
        self.password_edit = QLineEdit(self)
        self.password_edit.setEchoMode(QLineEdit.Password)#设置密码不可见
        self.password_edit.setPlaceholderText('Enter your password')
        self.password_edit.setText('123456')

        # 添加服务器 IP 地址输入框
        self.ip_label = QLabel(self)
        self.ip_label.setText('Server IP:')
        self.ip_edit = QLineEdit(self)
        self.ip_edit.setPlaceholderText('Enter the server IP address')
        self.ip_edit.setText('localhost')  # 设置默认值

        # 添加端口号输入框
        self.port_label = QLabel(self)
        self.port_label.setText('Port:')
        self.port_edit = QLineEdit(self)
        self.port_edit.setPlaceholderText('Enter the port number')
        self.port_edit.setText('22')



        #登录按钮
        login_btn = QPushButton('Login', self)
        login_btn.clicked.connect(self.login_clint)

        #注册按钮
        register_btn = QPushButton('Register', self)
        register_btn.clicked.connect(self.login_up)

        btn_group = QGroupBox(self)
        btn_layout = QHBoxLayout(btn_group)
        btn_layout.addWidget(login_btn)
        btn_layout.addWidget(register_btn)

        # 构建主布局，并设置左右两边的间距
        main_layout = QVBoxLayout(self)
        main_layout.addStretch(3)
        main_layout.addWidget(logo_label, stretch=5)
        main_layout.addWidget(title_label, stretch=1)
        main_layout.addStretch(3)
        main_layout.addWidget(self.username_edit, stretch=1)
        main_layout.addWidget(self.password_edit, stretch=1)
        main_layout.addWidget(btn_group, stretch=1)
        main_layout.addStretch(4)

        ip_port_layout = QHBoxLayout()
        ip_port_layout.addWidget(self.ip_label)
        ip_port_layout.addWidget(self.ip_edit)
        ip_port_layout.addWidget(self.port_label)
        ip_port_layout.addWidget(self.port_edit)
        main_layout.addLayout(ip_port_layout)

        main_layout.addWidget(btn_group, stretch=1)
        main_layout.addStretch(4)


        # 绑定提示文本
        self.username_edit.setToolTip('Please enter your username')
        self.password_edit.setToolTip('Please enter your password')




    def show_login(self):
        self.show()


    #登陆客户端代码
    def login_clint(self):
        self.sign_in = client()  # 会自动指定端口号
        self.username = self.username_edit.text()
        self.password = self.password_edit.text()
        self.host = self.ip_edit.text()
        self.port = int(self.port_edit.text())
        print('账号密码为：')
        print(self.username, self.password)
        print("ip和端口号为")
        print(self.host,self.port,self)
        a=self.sign_in.sign_in(self.host,self.port,self.username, self.password)#进行登陆

        #self.sign_in是一个client对象
        if self.sign_in.log:
            self.log_client=MainWindow()
            MainWindow.ftp = a
            MainWindow.user_log = self.sign_in
            #self.log_client.ftp=a # 为 下一个界面添加一个具有权限的服务器端ftp
            self.log_client.show()
        else:
            print('请登录重试')

    #注册客户端代码
    def login_up(self):
        self.sign_in=client()
        self.username = self.username_edit.text()
        self.password = self.password_edit.text()
        # self.host=self.ip_edit.text()
        # self.port=self.port_edit.text()
        print('账号密码为：')
        print(self.username, self.password)
        self.sign_in.sign_up(self.username, self.password)  # 进行登陆







if __name__ == '__main__':
    app = QApplication([])
    login_window = LoginWindow()
    login_window.show_login()
    app.exec_()

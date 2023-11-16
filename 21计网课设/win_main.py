import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from datetime import datetime
from PyQt5.QtGui import QIcon

from win_login import LoginWindow
from server import server


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 设置窗口的名字
        self.setWindowTitle('a simple FTP')
        # 设置窗口的图标
        self.setWindowIcon(QIcon('./WIN_ico/logo.png'))
        # 创建logo标签
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('github.png')  # 假象，只是为了左边空一列
        logo_label.setPixmap(logo_pixmap)
        #设置窗口背景
        # background = QPixmap('./WIN_ico/background.jpg')
        # self.setStyleSheet(f"background-image: url({background});")

        # 创建显示时间的标签
        time_label = QLabel(self)
        time_label.setAlignment(Qt.AlignCenter)  # 居中对齐
        time_label.setText(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # 显示当前时间

        # 创建两个按钮
        client_button = QPushButton('客户端', self)
        server_button = QPushButton('服务端', self)

        # 设置按钮点击事件
        client_button.clicked.connect(self.on_client_button_clicked)
        server_button.clicked.connect(self.on_server_button_clicked)

        # 将按钮放到一个group中
        button_group = QGroupBox()
        button_vbox_layout = QVBoxLayout()
        button_vbox_layout.addWidget(client_button)
        button_vbox_layout.addWidget(server_button)
        button_group.setLayout(button_vbox_layout)

        # 创建垂直布局，放置时间标签和group
        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(time_label)  # 将时间标签放到最上面
        vbox_layout.addWidget(button_group)  # 将group放到下方
        vbox_layout.addStretch()  # 添加弹性占位符，使group位于底部

        # 创建水平布局，将logo和垂直布局放入其中
        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(logo_label)
        hbox_layout.addLayout(vbox_layout)

        # 控制左右两边的宽度比例
        hbox_layout.setStretchFactor(logo_label, 1)  # 左边控件宽度权重为1
        hbox_layout.setStretchFactor(vbox_layout, 5)  # 右边布局宽度权重为3

        self.setLayout(hbox_layout)
        self.setWindowTitle('主界面')
        self.resize(400, 300)

    def on_client_button_clicked(self):

        #跳转到登陆界面
        self.login=LoginWindow()
        self.login.show_login()
        print('点击了客户端按钮')
        # TODO: 跳转到客户端登陆界面

    def on_server_button_clicked(self):
        self.serv=server()
        self.serv.add_author()
        self.serv.login()
        print('点击了服务端按钮')
        # TODO: 跳转到服务端操作界面


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()
    # sys.exit()

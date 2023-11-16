# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import  QWidget, QVBoxLayout, QPushButton, QLabel,QFileDialog,QMainWindow,QApplication
from PyQt5 import QtCore, QtWidgets
import sys
from client import client
import ftplib




class UploadWindow(QWidget):
    def __init__(self):
        super().__init__()


        # 创建控件
        label = QLabel('This is the upload window.')
        upload_button = QPushButton('Upload')
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(upload_button)

class DownloadWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建控件
        label = QLabel('This is the download window.')
        download_button = QPushButton('Download')
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(download_button)

class AccountWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建控件
        label = QLabel('This is the account management window.')
        manage_button = QPushButton('Manage')
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(manage_button)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 384)

        # 创建主控件
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(568, 379))
        self.centralwidget.setObjectName("centralwidget")

        # 创建水平布局器
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # 创建分组框
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(568, 379))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        # 创建垂直布局器
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # 创建框架
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setMinimumSize(QtCore.QSize(568, 45))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # 创建水平布局器
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # 创建水平布局器
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 创建按钮1
        self.pushButton_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_1.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout.addWidget(self.pushButton_1)

        # 创建按钮2
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        # 创建按钮3
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        # 创建布局器项
        spacerItem = QtWidgets.QSpacerItem(348, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame)

        #创建了一个堆叠窗口对象 stacked_widget
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox)
        self.stackedWidget.setMinimumSize(QtCore.QSize(568, 334))
        self.stackedWidget.setObjectName("stackedWidget")

        # 添加页面1控件
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        #添加一个选择文件的功能
        self.upload_button = QtWidgets.QPushButton(self.page)
        self.upload_button.clicked.connect(self.upload_file)
        self.horizontalLayout_4.addWidget(self.upload_button)
        self.stackedWidget.addWidget(self.page)

        # 添加页面2控件
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")


        self.download_button = QtWidgets.QPushButton(self.page_2)

        self.download_button.clicked.connect(self.download_file)
        self.horizontalLayout_5.addWidget(self.download_button)

        self.stackedWidget.addWidget(self.page_2)



        # 添加页面3控件
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_5")

        self.user_info=QtWidgets.QPushButton(self.page_3)
        self.user_info.clicked.connect(self.user_acount)
        self.user_info.setText('check on user info')
        self.horizontalLayout_6.addWidget(self.user_info)

        self.stackedWidget.addWidget(self.page_3)


        #添加整体的
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout_3.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def upload_file(self):
        # 打开文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(self, "Upload File", "", "All Files (*);;Text Files (*.txt)")
        print(file_path)

        # 如果有选择文件，执行上传操作
        if file_path:
            #self.up_o=client()
            # TODO self.up_o.ftp_upload(self,self.ftp,file_path)
            if MainWindow.ftp:
                #self.up_o.ftp_upload(MainWindow.ftp,file_path)
                MainWindow.user_log.ftp_upload(MainWindow.ftp,file_path)
                # 执行上传操作
                print("Upload file:", file_path)
            else:
                print("报错")

    def download_file(self):
        # TODO: 执行下载操作
        down_path, _ = QFileDialog.getOpenFileName(self, "Save File", "", "All Files (*);;Text Files (*.txt)")

        print("Download file path:", down_path)
        down_path=down_path.split('/')[-1]


        # 如果选择了要下载的文件路径，执行保存文件的操作
        if down_path:
            if MainWindow.ftp:
                MainWindow.user_log.ftp_download(MainWindow.ftp,'./local_file_path',down_path)

        else:
            print('报错')

    def user_acount(self):
        print("用户信息为",MainWindow.user_log.username)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "win_client"))
        self.pushButton_1.setText(_translate("MainWindow", "upload"))
        self.pushButton_2.setText(_translate("MainWindow", "download"))
        self.pushButton_3.setText(_translate("MainWindow", "account"))
        # self.pushButton_4.setText(_translate("MainWindow", "页面1")
        self.upload_button.setText(_translate("MainWindow", "upload_button"))
        # self.pushButton_5.setText(_translate("MainWindow", "页面2"))
        self.download_button.setText(_translate("MainWindow","Download File"))
class MainWindow(QMainWindow, Ui_MainWindow):
    ftp = None
    user_log = None
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


        # self.ftp=ftplib.FTP()#ftp对象
        self.pushButton_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
if __name__=='__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())

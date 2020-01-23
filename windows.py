# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from spider import Spider
from stock_info import Ui_Dialog
import find2
import hot_stock
from a21 import Figure_Canvas


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi()
        self.reault = {}
        self.main_hot_info()
        self.toolButton.clicked.connect(self.stock_dialog)
        self.enter_key()

    def setupUi(self):
        self.setObjectName("MyWindow")
        self.setStyleSheet(r"#MyWindow{border-image:url(C:/Users/xiaoqi/Documents/spider/bg4.jpg)}")     #设置背景图片
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 180, 371, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 80, 211, 101))
        self.label.setObjectName("icon")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(550, 180, 71, 31))
        self.toolButton.setObjectName("toolButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 230, 531, 351))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("#label_2{font-size: 20px;font: bold}")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi()
        icon = QIcon('dio.jpg')
        self.setWindowIcon(icon)
        image_name_path = 'C:/Users/xiaoqi/Documents/spider/icon.png'
        jpg = QtGui.QPixmap(image_name_path).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MyWindow", "巴菲特预测系统"))
        self.label.setText(_translate("MyWindow", "icon"))
        self.toolButton.setText(_translate("MyWindow", "确定"))
        self.label_2.setText(_translate("MyWindow", "hot_stock"))


    def enter_key(self):
        self.lineEdit.returnPressed.connect(self.stock_dialog)

    def __call(self):
        Dialog = Ui_Dialog()
        self.label2_info(Dialog)
        self.label_3_4_info(Dialog)
        self.img()
        Dialog.show()
        Dialog.exec_()


    def __Error(self):
        QMessageBox.warning(self, '输入有误', '请输入正确编码')

    def stock_dialog(self):
        if self.search():
            search_text = self.lineEdit.text()

            reault = Spider.Search(search_text)

            reault = reault.return_info()

            process = Spider.Process(reault)

            self.reault = process.search_page()              #股票的数据

            self.__call()

        else:
            self.__Error()

    def search(self):
        search_text = self.lineEdit.text()

        if search_text == '':

            return False
        else:

            return True


    def img(self):
        f = Figure_Canvas(0)
        stock_code = Spider.Search(self.lineEdit.text())
        stock_code = stock_code.return_info()
        try:
            f.vision(stock_code['stock_code'])
        except TypeError:
            pass

    def label2_info(self, Dialog):
        stock_code = Spider.Search(self.lineEdit.text())
        stock_code = stock_code.return_info()
        try:
            reault1,reault2 = find2.parse_page_info(stock_code['stock_code'])
            find2.transform(reault1,reault2)
            for i in range(20):
                Dialog.list[i](reault1[i]+'\n'+reault2[i])
        except IndexError:
            pass
        except TypeError:
            pass

    def label_3_4_info(self, Dialog):
        s = Spider.Search(self.lineEdit.text())
        reault = s.return_info()
        try:
            Dialog.label_2.setText(dict(reault)['stock_name'])
            Dialog.label_3.setText(dict(reault)['stock_code'][2:])
        except TypeError:
            pass

    def main_hot_info(self):
        res = hot_stock.getTarget(hot_stock.getHtml())
        reault = ''
        for item in res:
            reault += item['title']+' 热度:'+item['hot']+'\n'+' '.join(list(key+':'+value for key,value in item['data'].items())) + '\n'
            reault += '\n'
        self.label_2.setText(reault)
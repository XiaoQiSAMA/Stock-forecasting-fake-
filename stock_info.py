# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock_info.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(855, 549)
        self.setWindowFlags(Qt.WindowStaysOnTopHint|QtCore.Qt.WindowCloseButtonHint)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 20, 640, 300))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 161, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 161, 51))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(750, 30, 92, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 80, 92, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 130, 92, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(750, 180, 92, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(750, 230, 92, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(750, 280, 92, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 320, 831, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 7, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 6, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 9, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 8, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 1, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 1, 4, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 1, 5, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 1, 6, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 1, 7, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 1, 8, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 1, 9, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.pushButton.clicked.connect(self.button_1)
        self.pushButton_2.clicked.connect(self.button_2)
        self.pushButton_3.clicked.connect(self.button_3)
        self.pushButton_4.clicked.connect(self.button_4)
        self.pushButton_5.clicked.connect(self.button_5)
        self.pushButton_6.clicked.connect(self.button_6)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "股票信息"))
        self.label.setText(_translate("Dialog", "炒股有风险,入股需谨慎"))
        self.label_2.setText(_translate("Dialog", "公司名称"))
        self.label_3.setText(_translate("Dialog", "股票编号"))
        self.label_2.setStyleSheet("#label_2{font-size: 18px;font: bold}")
        self.label_3.setStyleSheet("#label_3{font-size: 18px;font: bold}")
        self.pushButton.setText(_translate("Dialog", "收盘变化率"))
        self.pushButton_2.setText(_translate("Dialog", "日均价"))
        self.pushButton_3.setText(_translate("Dialog", "日涨跌幅"))
        self.pushButton_4.setText(_translate("Dialog", "核密度"))
        self.pushButton_5.setText(_translate("Dialog", "核估统计"))
        self.pushButton_6.setText(_translate("Dialog", "皮尔森估计"))
        self.label_4.setText(_translate("Dialog", "今开"))
        self.label_5.setText(_translate("Dialog", "成交量"))
        self.label_6.setText(_translate("Dialog", "最高"))
        self.label_7.setText(_translate("Dialog", "涨停"))
        self.label_8.setText(_translate("Dialog", "内盘"))
        self.label_9.setText(_translate("Dialog", "成交额"))
        self.label_10.setText(_translate("Dialog", "流通市值"))
        self.label_11.setText(_translate("Dialog", "市盈率"))
        self.label_12.setText(_translate("Dialog", "每股收益"))
        self.label_13.setText(_translate("Dialog", "总股本"))
        self.label_14.setText(_translate("Dialog", "昨收"))
        self.label_15.setText(_translate("Dialog", "换手率"))
        self.label_16.setText(_translate("Dialog", "最低"))
        self.label_17.setText(_translate("Dialog", "跌停"))
        self.label_18.setText(_translate("Dialog", "外盘"))
        self.label_19.setText(_translate("Dialog", "振幅"))
        self.label_20.setText(_translate("Dialog", "量比"))
        self.label_21.setText(_translate("Dialog", "市净率"))
        self.label_22.setText(_translate("Dialog", "每股净资产"))
        self.label_23.setText(_translate("Dialog", "流通股本"))
        self.setStyleSheet(r"#Dialog{border-image:url(C:/Users/xiaoqi/Documents/spider/bg_1.jpg)}")
        self.label.setStyleSheet("#label{font-size: 60px}")


        self.list = [
            self.label_4.setText,
            self.label_5.setText,
            self.label_6.setText,
            self.label_7.setText,
            self.label_8.setText,
            self.label_9.setText,
            self.label_10.setText,
            self.label_11.setText,
            self.label_12.setText,
            self.label_13.setText,
            self.label_14.setText,
            self.label_15.setText,
            self.label_16.setText,
            self.label_17.setText,
            self.label_18.setText,
            self.label_19.setText,
            self.label_20.setText,
            self.label_21.setText,
            self.label_22.setText,
            self.label_23.setText,
        ]

    def button_1(self):
        image_name_path = 'stock_1.jpg'
        jpg = QtGui.QPixmap(image_name_path).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)


    def button_2(self):
        image_name_path = 'stock_2.jpg'
        jpg = QtGui.QPixmap(image_name_path).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)

    def button_3(self):
        image_name_path = 'stock_3.jpg'
        jpg = QtGui.QPixmap(image_name_path).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)

    def button_4(self):
        image_name_path = 'stock_4.jpg'
        jpg = QtGui.QPixmap(image_name_path).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)

    def button_5(self):
        image_name_path = 'stock_5.jpg'
        jpg = QtGui.QPixmap(image_name_path).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)

    def button_6(self):
        image_name_path = 'stock_6.jpg'
        jpg = QtGui.QPixmap(image_name_path).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\Desktop\A股数据预测\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QWidget, QApplication,QTableWidgetItem,QFont,QBrush,Qt,QColor,QAbstractItemView,QCoreApplication
import sqlite3
import math
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
from rank import Ui_Form1
from selectfirm import Ui_Form00
score = np.zeros((6, 5), np.float16)
class Ui_MainWindow1(object):
    def __init__(self, name1="世纪星源"):
        self.name1 = name1
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1238, 754)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(440, 130, 801, 581))
        self.tableWidget.setStyleSheet("background: rgb(252,253,253);\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(37)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(30, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(31, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(32, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(33, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(34, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(35, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(36, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(140, 140, 140))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 104, 104))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(136, 136, 136))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 4, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 100, 801, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 216, 212);\n"
"border-radius:5px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 100, 441, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(139, 139, 139);\n"
"border-radius:5px;")
        self.label_2.setObjectName("label_2")    
        self.label_2.setFont(font)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 130, 441, 581))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 161, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 50, 161, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(480, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(630, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(780, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(290, 10, 21, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(450, 10, 21, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(610, 10, 21, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(760, 10, 21, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(910, 10, 31, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(930, 0, 101, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(170, 50, 101, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(320, 50, 101, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(480, 50, 101, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(630, 50, 101, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(790, 50, 101, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(930, 50, 101, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(1080, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(1080, 50, 101, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(255, 57, 57);")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1152, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu.addSeparator()
        self.menubar.addAction(self.menu.menuAction())
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1080, 0, 91, 31))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(192, 242, 255);\n"
                                      "border-radius:5px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.searchButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1080, 40, 91, 31))
        self.pushButton_2.clicked.connect(self.selectButton)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(192, 242, 255);\n"
                                      "border-radius:5px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "现金与约当现金(占总资产%)"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "应收款项(占总资产%)"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "存货(占总资产%)"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "流动资产(占总资产%)"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "非流动资产(占总资产%)"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "应付款项(占总资产%)"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "流动负债(占总资产%)"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "非流动负债(占总资产%)"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "股东权益(占总资产%)"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "负债占资产比率(%)"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "长期资金占不动产及设备比率(%)"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "流动比率(%)"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "速动比率(%)"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "应收款项周转率(次/年)"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "应收款项周转天数(天)"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "存货周转天数(天)"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "应收款项周转天数(天)"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "固定资产周转率(次/年)"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "完整生意周期(天)"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "应付款项周转天数(天)"))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "缺钱天数(天)"))
        item = self.tableWidget.verticalHeaderItem(21)
        item.setText(_translate("MainWindow", "总资产周转率(次/年)"))
        item = self.tableWidget.verticalHeaderItem(22)
        item.setText(_translate("MainWindow", "ROA=资产收益率(%)"))
        item = self.tableWidget.verticalHeaderItem(23)
        item.setText(_translate("MainWindow", "ROE=净资产收益率(%)"))
        item = self.tableWidget.verticalHeaderItem(24)
        item.setText(_translate("MainWindow", "税前纯益占实收资本比率(%)"))
        item = self.tableWidget.verticalHeaderItem(25)
        item.setText(_translate("MainWindow", "毛利率(%)"))
        item = self.tableWidget.verticalHeaderItem(26)
        item.setText(_translate("MainWindow", "营业利润率(%)"))
        item = self.tableWidget.verticalHeaderItem(27)
        item.setText(_translate("MainWindow", "净利率(%)"))
        item = self.tableWidget.verticalHeaderItem(28)
        item.setText(_translate("MainWindow", "营业费用率(%)"))
        item = self.tableWidget.verticalHeaderItem(29)
        item.setText(_translate("MainWindow", "经营安全边际率(%)"))
        item = self.tableWidget.verticalHeaderItem(30)
        item.setText(_translate("MainWindow", "EPS=基本每股收益(元)"))
        item = self.tableWidget.verticalHeaderItem(31)
        item.setText(_translate("MainWindow", "营收增长率(%)"))
        item = self.tableWidget.verticalHeaderItem(32)
        item.setText(_translate("MainWindow", "净利增长率(%)"))
        item = self.tableWidget.verticalHeaderItem(33)
        item.setText(_translate("MainWindow", "净资本增长率(%)"))
        item = self.tableWidget.verticalHeaderItem(34)
        item.setText(_translate("MainWindow", "现金流量比率(%)"))
        item = self.tableWidget.verticalHeaderItem(35)
        item.setText(_translate("MainWindow", "现金流量允当比率(%)"))
        item = self.tableWidget.verticalHeaderItem(36)
        item.setText(_translate("MainWindow", "现金再投资比率(%)"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "图例"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2017年"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "2016年"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "2015年"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "2014年"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "2013年"))
        self.label_5.setText(_translate("MainWindow", "现金占比权重（去年）"))
        self.label_6.setText(_translate("MainWindow", "经营能力权重（去年）"))
        self.label_7.setText(_translate("MainWindow", "获利能力权重（去年）"))
        self.label_8.setText(_translate("MainWindow", "财务结构权重（去年）"))
        self.label_9.setText(_translate("MainWindow", "偿债能力权重（去年）"))
        self.label_10.setText(_translate("MainWindow", "+"))
        self.label_11.setText(_translate("MainWindow", "+"))
        self.label_12.setText(_translate("MainWindow", "+"))
        self.label_13.setText(_translate("MainWindow", "×"))
        self.label_14.setText(_translate("MainWindow", "＝"))
        self.label_15.setText(_translate("MainWindow", "公司评分"))
        self.pushButton.setText(_translate("MainWindow", "公司评分排名"))
        self.pushButton_2.setText(_translate("MainWindow", "公司评分筛选"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", " 财务比例"))
        self.label_2.setText(_translate("MainWindow", " 这家公司状况"))
        self.menu.setTitle(_translate("MainWindow", "主页面"))
        str1 = self.name1  # 获取输入框数据
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus']=False
        path_root = './finally'
        dirs = os.listdir(path_root)
        name=[]
        years = np.array([2013, 2014, 2015, 2016, 2017], np.int64)
        for dir in dirs:
            file_name = dir.split('.')
            filename=file_name[0].split('_')
            name.append(filename)
        for i in range(len(name)):
            if str1 in name[i]:
                path=name[i][0]+"_"+name[i][1]+".csv"
                code=name[i][0]
        file = path_root+'\\' + path
        file = csv.reader(open(file, 'r',encoding='utf-8'))
        data = np.zeros((37, 5), np.float16)
        for i, row in enumerate(file):
            if i==0:
                continue
            for j in range(5):
                data[i-1, j] =np.float16(row[j+1])  
        def drowplt(data, years):
        #每支股票的全部的表
            for i in range(37):
                plt.figure(figsize=(1.29, 0.36))  
                plt.plot(years,data[i],'r',lw=2)
                plt.fill(years,data[i], color = "grey", alpha = 0.3)  
                plt.xticks([])
                plt.yticks([])
                plt.axis('off')
                plt.savefig("./image/{}.jpg".format(i))
        
        global score 
        for j in range(5):
        #求股票的气
        #求现金占比
            if data[0, j] >= 10:
                score[0, j] = score[0, j] + 7
            else:
                score[0, j] = score[0, j] + data[0, j]*7/ 25
        #求股票的应收款周转天数
            if data[14, j] <= 15:
                score [0, j] = score [0, j] + 2
            else:
                score [0, j] = score [0, j] + 2*15/data[14, j]
        #现金的三大比例
            i = 0
            if data[34, j] >= 100:      #现金流量比率
                i = 1
            else:
                i = (data[34, j]/100)
            if data[35, j] >= 100:      #现金允当比例
                i = i + 1
            else:
                i = (data[35, j]/100)+i
            if data[36, j] >= 10:       #现金在投资比例
                i = i + 1 
            else:
                i = i + (data[36, j]/100)
            score [0, j] = score[0, j] + i/3
            if score[0,j]==-np.inf:
                score[0,j]=0
            #经营能力
            #资产周转率
            if data[21, j] <1:
                score[1, j] = score[0, j] 
            else:
                score[1, j] = score[1, j] + 5
                if data[17, j] <= 30:     #存货周转天数
                    score[1,j] = score[1, j] + 2.5
                else:
                    score[1,j] = score[1, j] + 2.5*30/data[17, j]
                if data[14, j]<=90:      #应收款项周转天数
                    score[1,j] = score[1, j] + 2.5
                else:
                    score[1,j] = score[1, j] + 2.5*60/data[14, j]
            #获利能力
            #毛利率
            if data[25, j]>=32:    
                score[2, j] = score[2, j] + 2
            else:
                score[2, j] = score[2, j] + 2*data[25, j]/30
            #营业利益率
            if data[26, j] >= 10:
                score[2, j] = score[2, j] + 2
            else:
                score[2, j] = score[2, j] + 2*data[26, j]/10
            if data[29, j]>=60:    #经营安全边界
                score[2, j] = score[2, j] + 2
            else:
                score[2, j] = score[2, j] + 2*data[29, j]/60
            if data[27, j]>=2:     #净利率
                score[2, j] = score[2, j] + 1
            else:
                score[2, j] = score[2, j] + data[27, j]/2
            if data[30, j]>=1:      #EPS
                score[2, j] = score[2, j] + 1
            else:
                score[2, j] = score[2, j] + data[30, j]
            if data[23, j]>=20:     #ROE
                score[2, j] = score[2, j] + 1
            else:
                score[2, j] = score[2, j] + data[23, j]/20
            if score[2,j]==-np.inf:
                score[2,j]=0
            #财务结构
            #负债占资产比例
            if data[9, j]  >= 25 and data[9, j] <= 70:
                score[3, j] = score[3, j]+5
            elif data[9, j] < 25:
                score[3, j] = score[3, j] + 5*data[9, j]/25
            else:
                score[3, j] = score[3, j]+0
            #长期资金占不动产比率
            if data[10, j] >=100:
                score[3, j] = score[3, j] + 5
            else:
                score[3, j] = score[3, j] + 5*data[10, j]/100
            #偿债能力
            #流动比率
            if data[11, j] >= 300:
                score[4, j] = score[4, j] + 5
            else:
                score[4, j] = score[4, j] + 5*data[11, j]/300
            #速动比率
            if data[12, j] >= 150:
                score[4, j] = score[4, j] + 5
            else:
                score[4, j] = score[4, j] + 5*data[12, j]/100
    
            score[5, j] = score[0, j] * 3 + score[1, j]* 3 + score[2, j]*2 + score[3, j] + score[4, j]
        drowplt(data, years)
        for i in range(37):
            lbp1=QtWidgets.QLabel()  
            lbp1.setPixmap(QtGui.QPixmap("image/{}.jpg".format(i)))  
            self.tableWidget.setCellWidget(i,0,lbp1)  
        self.label_3.setText(_translate("MainWindow", str1))
        self.label_4.setText(_translate("MainWindow", "股票代码：{}".format(code)))
        self.label_16.setText(_translate("MainWindow", "{0:.1f}".format(score[0,4])))
        self.label_17.setText(_translate("MainWindow", "{0:.1f}".format(score[1,4])))
        self.label_18.setText(_translate("MainWindow", "{0:.1f}".format(score[2,4])))
        self.label_19.setText(_translate("MainWindow", "{0:.1f}".format(score[3,4])))
        self.label_20.setText(_translate("MainWindow", "{0:.1f}".format(score[4,4])))
        self.label_21.setText(_translate("MainWindow", "{0:.1f}".format(score[5,4])))
        conn = sqlite3.connect(r'./database.db3')
        conn.isolation_level = None
        conn.commit()
        cur = conn.cursor()
        cur.execute("select * from %s" % str1)
        res = cur.fetchall()
        row = len(res)  # 数据库表中总行数
        cown = len(res[0]) # 数据库中每行的列数
        for i in range(row):
            for j in range(1,cown):
                # 设置i行j列的内容为Value
                if abs(float(res[i][j]))<0.1:
                    item=QtWidgets.QTableWidgetItem(str(round(float(res[i][j]),2)))
                else:
                    item=QtWidgets.QTableWidgetItem(str(round(float(res[i][j]),1)))
#                if i % 2 == 0:
#                    item.setBackground(QtGui.QBrush(QtGui.QColor(200, 200, 200)))  # 背景
#                    # item.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))#字体
#                elif i % 2 == 1:
#                    item.setBackground(QtGui.QBrush(QtGui.QColor(254, 254, 254)))
#                    # item.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 0)))
                self.tableWidget.setItem(i, j, item)
        evaluate=[]#评价
        year=['2017年','2016年','2015年','2014年','2013年']
        #现金与约当现金(占总资产%)
        for i in range(1,6):
            print(year[i-1])
            evaluate=[]
            evaluate.append(year[i-1])
            if float(res[0][i])<10:
                print("气很短")
                evaluate.append("气很短 ")
            elif float(res[0][i])<15:
                print("气一般")
                evaluate.append("气一般 ")
            elif float(res[0][i])<25:
                print("现金充足")
                evaluate.append("现金充足 ")
            else:
                print("气很长")
                evaluate.append("气很长 ")
#现金流量比率(%)
            if ((float(res[34][i])<0)or(float(res[35][i])<0)or(float(res[36][i])<0)):
                print("现金流状况不佳")
                evaluate.append("现金流状况不佳.")
            else:
                print("现金流状况一般")
                evaluate.append("现金流状况一般.")
#应收款项周转天数(天)
            if float(res[14][i])<15:
                print("天天收现金")
                evaluate.append("天天收现金!")
            elif float(res[14][i])<80:
                print("收款很快")
                evaluate.append("收款很快.")
            elif float(res[14][i])<100:
                print("收款速度一般")
                evaluate.append("收款速度一般.")
            elif float(res[14][i])<150:
                print("收款速度很慢！")
                evaluate.append("收款速度很慢!")
            else:
                print("收款速度也太慢了吧！")
                evaluate.append("收款速度也太慢了吧!")
#总资产周转率(次/年)
            if float(res[21][i])<1:
                evaluate.append("重资产,周转很慢，风险高!")
                if float(res[0][i])<10:
                    print("而且现金水位过低!")
                    evaluate.append("而且现金水位过低!")
                elif float(res[0][i])<15:
                    print("而且现金比率偏低!")
                    evaluate.append("而且现金比率偏低!")
                elif float(res[0][i])<25:
                    print("好在现金还算充足!")
                    evaluate.append("好在现金还算充足!")
                else:
                    print("还好现金超级多!")
                    evaluate.append("还好现金超级多!")
            elif float(res[21][i])<1.5:
                print("经营稳健,还不错.")
                evaluate.append("经营稳健,还不错.")
            elif float(res[21][i])<2:
                print("经营效率优异")
                evaluate.append("经营效率优异.")
            else:
                print("团队运营超一流")
                evaluate.append("团队运营超一流!")
#存货周转天数
            if float(res[16][i])<10:
                print("基本无存货,产品火爆")
                evaluate.append("基本无存货,产品火爆.")
            elif float(res[16][i])<30:
                print("货卖的很快,口碑好")
                evaluate.append("货卖的很快,口碑好.")
            elif float(res[16][i])<60:
                print("货卖的不错")
                evaluate.append("货卖的不错.")
            elif float(res[16][i])<100:
                print("货卖的一般")
                evaluate.append("货卖的一般.")
            elif float(res[16][i])<150:
                print("卖货很慢,属于原物料或低频消费品.")
                evaluate.append("卖货很慢,属于原物料或低频消费品.")
            else:
                print("产品可能不好卖,特殊产业除外(酒类,地产等).")
                evaluate.append("产品可能不好卖,特殊产业除外(酒类,地产等).")
#缺钱天数
            if float(res[20][i])<0:
                print("不需要资金就可以做生意!")
                evaluate.append("不需要资金就可以做生意!")
#完整生意周期
            if float(res[18][i])>200:
                print("一轮生意要{0:.1f}天.生意完整周期偏长.".format(float(res[18][i])))
                evaluate.append("一轮生意要{0:.1f}天.生意完整周期偏长.".format(float(res[18][i])))
                if float(res[0][i])<10:
                    print("而且现金水位过低!")
                    evaluate.append("而且现金水位过低!")
                    if float(res[25][i])>30:
                        print("还好毛利足够高!")
                        evaluate.append("还好毛利足够高!")
                elif float(res[0][i])<15:
                    print("而且现金比率偏低!")
                    evaluate.append("而且现金比率偏低!")
                elif float(res[0][i])<25:
                    print("好在现金还算充足!")
                    evaluate.append("好在现金还算充足!")
                else:
                    print("还好现金超级多!")
                    evaluate.append("还好现金超级多!")
            else:
                print("一轮生意要{0:.1f}天.".format(float(res[18][i])))
                evaluate.append("一轮生意要{0:.1f}天.".format(float(res[18][i])))
#毛利率
            if float(res[25][i])<10:
                print("生意很难做,费用率{0:.1f}个点".format(float(res[28][i])))
                evaluate.append("生意很难做,费用率{0:.1f}个点".format(float(res[28][i])))
            elif float(res[25][i])<20:
                print("生意很艰辛,费用率{0:.1f}个点".format(float(res[28][i])))
                evaluate.append("生意很艰辛,费用率{0:.1f}个点".format(float(res[28][i])))
            elif float(res[25][i])<30:
                print("毛利还可以,费用率{0:.1f}个点".format(float(res[28][i])))
                evaluate.append("毛利还可以,费用率{0:.1f}个点".format(float(res[28][i])))
            elif float(res[25][i])<40:
                print("毛利还不错,费用率{0:.1f}个点".format(float(res[28][i])))
                evaluate.append("毛利还不错,费用率{0:.1f}个点".format(float(res[28][i])))
            elif float(res[25][i])<55:
                print("毛利很高,费用率{0:.1f}个点".format(float(res[28][i])))
                evaluate.append("毛利很高,费用率{0:.1f}个点".format(float(res[28][i])))
            elif float(res[25][i])<70:
                print("毛利超高,费用率{0:.1f}个点".format(float(res[28][i])))
                evaluate.append("毛利超高,费用率{0:.1f}个点".format(float(res[28][i])))
            else:
                print("毛利堪比卖白粉,费用率{0:.1f}个点".format(float(res[28][i])))
                evaluate.append("毛利堪比卖白粉,费用率{0:.1f}个点".format(float(res[28][i])))
#营业费用率
            if float(res[28][i])<5:
                print("可能是营运超牛的公司!")
                evaluate.append("这个生意赚不到钱!")
            elif float(res[28][i])<9:
                print("生意又大又省钱!")
                evaluate.append("生意又大又省钱!")
            elif float(res[28][i])<13:
                print("市场规模很大!")
                evaluate.append("市场规模很大!")
#净利率
            if float(res[27][i])<0:
                print("这个生意赚不到钱!")
                evaluate.append("这个生意赚不到钱!")
            elif float(res[27][i])<10:
                print("税后利润一般,")
                evaluate.append("税后利润一般,")
            elif float(res[27][i])<20:
                print("税后利润不错,")
                evaluate.append("税后利润不错,")
            elif float(res[27][i])<30:
                print("税后利润优异")
                evaluate.append("税后利润优异,")
            else:
                print("即使税后也非常赚钱,")
                evaluate.append("即使税后也非常赚钱,")
#ROE
            if float(res[23][i])<0:
                print("股东在亏损!")
                evaluate.append("股东在亏损!")
            elif float(res[23][i])<10:
                print("收益率不高.")
                evaluate.append("收益率不高.")
            elif float(res[23][i])<15:
                print("还可以收益的.")
                evaluate.append("还可以的收益.")
            elif float(res[23][i])<20:
                print("不错的回报率.")
                evaluate.append("不错的回报率.")
            elif float(res[23][i])<30:
                print("能够打败巴菲特的回报率.")
                evaluate.append("能够打败巴菲特的回报率.")
            elif float(res[23][i])<40:
                print("很牛逼的回报率.")
                evaluate.append("很牛逼的回报率.")
#EPS
            if float(res[30][i])<0:
                print("每一股在去年赔了{0:.2f}元钱".format(float(res[30][i])))
                evaluate.append("每一股在去年赔了{0:.2f}元钱".format(float(res[30][i])))
            else:
                print("每一股在去年为公司赚了{0:.2f}元钱".format(float(res[30][i])))
                evaluate.append("每一股在去年为公司赚了{0:.2f}元钱".format(float(res[30][i])))
#负债占资产比率
            if float(res[9][i])<30:
                print("基本没什么杆杠，看来股东非常看好公司,")
                evaluate.append("基本没什么杆杠，看来股东非常看好公司,")
            elif float(res[9][i])<40:
                print("不用举债就能存活很好.")
                evaluate.append("不用举债就能存活很好,")
            elif float(res[9][i])<60:
                print("杆杠稳健,")
                evaluate.append("杆杠稳健,")
            elif float(res[9][i])<80:
                print("杆杠偏高,")
                evaluate.append("杆杠偏高,")
            else:
                print("杆杠过大,风险偏高,")
                evaluate.append("杆杠过大,风险偏高,")
#长期资金占不动及设备比例
            if float(res[10][i])<100:
                print("长期资金来源缺乏.")
                evaluate.append("长期资金来源缺乏.")
            elif float(res[10][i])<200:
                print("长期资金来源稳健.")
                evaluate.append("长期资金来源稳健.")
            elif float(res[10][i])<300:
                print("长期资金来源充足.")
                evaluate.append("长期资金来源充足.")
            else:
                print("长期资金源源不断!")
                evaluate.append("长期资金源源不断!")
#速动比率
            if float(res[12][i])<100:
                if float(res[11][i])<100:
                    print("短期外债偏高,公司目前有{0:d}成是现金资产.".format(math.floor(float(res[0][i])/10)))
                    evaluate.append("短期外债偏高,公司目前有{0:d}成是现金资产.".format(math.floor(float(res[0][i])/10)))
                else:
                    print("如果发生债务纠纷,可能缺乏立即清偿能力.")
                    evaluate.append("如果发生债务纠纷,可能缺乏立即清偿能力.") 
            elif float(res[12][i])<150:
                    print("即使发生债务纠纷,公司清偿问题不大.")
                    evaluate.append("即使发生债务纠纷,公司清偿问题不大.")
            else:
                print("即使发生债务纠纷,公司也能立即清偿.")
                evaluate.append("即使发生债务纠纷,公司也能立即清偿.")
            print(type(evaluate))
            print(evaluate)
            print(str(evaluate))
            for ch in '[],\'':
                evaluate=str(evaluate).replace(ch,"")
            print(evaluate)
            self.textBrowser.append(evaluate)
        
        cur.close()
        conn.close()
    def searchButton(self): 
        self.page = QtWidgets.QDialog()
        self.ui = Ui_Form1()
        self.ui.setupUi(self.page)
        self.page.show()
    def selectButton(self):
        self.page1 = QtWidgets.QDialog()
        self.ui = Ui_Form00()
        self.ui.setupUi(self.page1)
        self.page1.show()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\Desktop\A股数据预测\1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication
from main import Ui_MainWindow1
import startphoto
import os
path_root = r'./finally'
dirs = os.listdir(path_root)
name=[]
firmname=""

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(500, 277)
#        Form.resize(500, 277)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Form.setFont(font)
        Form.setStyleSheet("")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 190, 231, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 190, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(125, 125, 125);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 4px;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 110, 281, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 60, 211, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 500, 277))
        self.graphicsView.setStyleSheet("background-image: url(:/1/start.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 190, 121, 31))
        self.label_3.setStyleSheet("color: rgb(202, 202, 202);")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 0, 31, 20))
        self.pushButton_2.setStyleSheet("background-image: url(:/2/exit.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton.clicked.connect(self.searchButton)
        self.graphicsView.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.lineEdit.textChanged.connect(self.masklabel3)
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton_2.raise_()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowFlags(Qt.FramelessWindowHint)
        Form.setWindowTitle(_translate("Form", "小财报"))
        self.pushButton.setText(_translate("Form", "搜索"))
        self.label.setText(_translate("Form", "快速锁定财富洼地, 你的价值投资军火库"))
        self.label_2.setText(_translate("Form", "一眼看懂公司财报"))
        self.label_3.setText(_translate("Form", "输入公司名/股票代码"))
    def masklabel3(self,Form):
        self.label_3.setText(None)
    def searchButton(self):   
        global firmname
        if(self.lineEdit.text!=""):
            firmname=self.lineEdit.text()
        for dir in dirs:
            file_name = dir.split('.')
            file_name=file_name[0].split('_')
            name.append(file_name)
        namebool=False
        for i in range(len(name)):
            if firmname in name[i]:
                name1=name[i][1]
                namebool=True
        if namebool==False:
            name1=name[0][1]
        self.mainpage = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1(name1)
        self.ui.setupUi(self.mainpage)
        self.mainpage.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) 
    Dialog = QtWidgets.QDialog()
    ui=Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
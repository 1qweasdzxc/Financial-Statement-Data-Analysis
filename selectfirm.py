# -*- coding: utf-8 -*-
"""
Created on Tue May 29 17:45:19 2018

@author: 来来
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import os
import csv
class Ui_Form00(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(402, 504)
        Form.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 30, 51, 20))
        self.lineEdit.setText("0")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 30, 51, 20))
        self.lineEdit_2.setText("0")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 30, 111, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 111, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 60, 51, 20))
        self.lineEdit_3.setText("0")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 60, 51, 20))
        self.lineEdit_4.setText("0")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(180, 10, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(270, 10, 54, 12))
        self.label_4.setObjectName("label_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(260, 90, 51, 20))
        self.lineEdit_6.setText("0")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 90, 51, 20))
        self.lineEdit_5.setText("0")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 90, 111, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 120, 111, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(170, 120, 51, 20))
        self.lineEdit_7.setText("0")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(260, 120, 51, 20))
        self.lineEdit_8.setText("0")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(260, 150, 51, 20))
        self.lineEdit_10.setText("0")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(170, 150, 51, 20))
        self.lineEdit_9.setText("0")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(50, 150, 111, 21))
        self.label_7.setObjectName("label_7")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(50, 180, 271, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(340, 30, 51, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 216, 184);\n"
"border-radius:5px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.changetext)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "现金占比"))
        self.label_2.setText(_translate("Form", "经营能力"))
        self.label_3.setText(_translate("Form", "最小值"))
        self.label_4.setText(_translate("Form", "最大值"))
        self.label_5.setText(_translate("Form", "获利能力"))
        self.label_6.setText(_translate("Form", "财务结构"))
        self.label_7.setText(_translate("Form", "偿债能力"))
        self.pushButton.setText(_translate("Form", "筛选"))
       
    def changetext(self):
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.setText(_translate("Form", "公司代码      公司名"))
        min0=self.lineEdit.text()
        max0=self.lineEdit_2.text()
        min1=self.lineEdit_3.text()
        max1=self.lineEdit_4.text()
        min2=self.lineEdit_5.text()
        max2=self.lineEdit_6.text()
        min3=self.lineEdit_7.text()
        max3=self.lineEdit_8.text()
        min4=self.lineEdit_9.text()
        max4=self.lineEdit_10.text()
        section=[[min0,max0],[min1,max1],[min2,max2],[min3,max3],[min4,max4]]
        f1=open("./score.txt","rt")
        for i0, line in enumerate(f1):
            if i0==0:
                continue
            le=line.strip().split(",")
            g=0
            g1=0
            j=1
            for i in section:
                j=j+1
                if i[0]!="0" or i[1]!="0":
                    g=g+1
                    if (float(le[j])>float(i[0])) & (float(le[j])<float(i[1])):
                         g1=g1+1
            if (g==g1) or (g==0):
                print(le[1])
                self.textBrowser.append("{}\t{}".format(le[0],le[1]))   
        Dialog = QtWidgets.QDialog()
        ui=Ui_Form00()
        ui.setupUi(Dialog)
        Dialog.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) 
    Dialog = QtWidgets.QDialog()
    ui=Ui_Form00()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
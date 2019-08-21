# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pplogin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from aachoose import Ui_Dialog3
from aanewuserlogindetails import Ui_Dialog5
import mysql as mdb
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='railway_concession',
                                       user='root',
                                       password='')
        if conn.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
 
    finally:
        conn.close()
 
 
if __name__ == '__main__':
    connect()

class Ui_Dialog(object):
    def InsertData(self):
        con= mdb.connector.connect(host="localhost",user="root", passwd="",db="railway_concession")

        #with con:
        cur = con.cursor()  
        cur.execute('''INSERT INTO users(username, password)
                           VALUES (%s, %s)''', 
                           ( self.lineEdit.text(),
                             self.lineEdit_2.text(),
                              )
                       )            
        cur.close()

        #QMessageBox.information(self, "Connection", "Data Inserted Successfully")

        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.initWindow() 
    def newText(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)

    def newuser(self):
        self.aanewuserlogindetailsWindow=QtWidgets.QDialog()
        self.ui=Ui_Dialog5()
        self.ui.setupUi(self.aanewuserlogindetailsWindow)
        self.aanewuserlogindetailsWindow.show()
    def form(self):
        self.aaformWindow=QtWidgets.QDialog()
        self.ui=Ui_Dialog3()
        self.ui.setupUi(self.aaformWindow)
        self.aaformWindow.show()
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1102, 866)
        Dialog.setStyleSheet("QDialog {\n"
"background-color:rgb(255, 255, 255);\n"
"}    \n"
"    image: url(:/newPrefix/logodbit.jpg);\n"
"\n"
"")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(390, 490, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(390, 540, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(530, 490, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 540, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 610, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        #button event
        self.pushButton.clicked.connect(self.InsertData)
        self.pushButton.clicked.connect(self.form)
        #
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 610, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        #button event
        self.pushButton_2.clicked.connect(self.newuser)
        #
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(1104, 5, 141, 121))
        self.label_4.setStyleSheet("image: url(:/newPrefix/logodbit.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 1101, 371))
        self.label.setStyleSheet("image: url(:/newPrefix/cLG.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(260, 10, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Username :"))
        self.label_3.setText(_translate("Dialog", "Password :"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter Moodle ID"))
        self.lineEdit.textChanged.connect(self.newText)
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.pushButton_2.setText(_translate("Dialog", "New User"))
        self.label_5.setText(_translate("Dialog", "DBIT RAILWAY CONCESSION"))

import new

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


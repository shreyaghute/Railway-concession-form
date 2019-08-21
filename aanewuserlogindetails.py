# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ppnewuserlogindetails.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from aanewuser_details import Ui_Dialog6
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

class Ui_Dialog5(object):
    def InsertData(self):
        con= mdb.connector.connect(host="localhost",user="root", passwd="",db="railway_concession")

        #with con:
        cur = con.cursor()  
        cur.execute('''INSERT INTO users(username, password)
                           VALUES (%s, %s)''', 
                           ( self.usernamet.text(),
                             self.passwordt.text(),
                              )
                       )            
        cur.close()

        #QMessageBox.information(self, "Connection", "Data Inserted Successfully")

        self.usernamet.setText('')
        self.passwordt.setText('')
        self.initWindow() 
    def newText(self):
        if self.usernamet.text() and self.passwordt.text():
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)
    def details(self):
        self.aanewuser_detailsWindow=QtWidgets.QDialog()
        self.ui=Ui_Dialog6()
        self.ui.setupUi(self.aanewuser_detailsWindow)
        self.aanewuser_detailsWindow.show()
        
    def setupUi(self, Dialog5):
        Dialog5.setObjectName("Dialog5")
        Dialog5.resize(1104, 870)
        Dialog5.setStyleSheet("QDialog {\n"
"background-color:rgb(255, 255, 255);\n"
"    \n"
"}\n"
"")
        self.password = QtWidgets.QLabel(Dialog5)
        self.password.setGeometry(QtCore.QRect(360, 460, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.username = QtWidgets.QLabel(Dialog5)
        self.username.setGeometry(QtCore.QRect(360, 400, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.usernamet = QtWidgets.QLineEdit(Dialog5)
        self.usernamet.setGeometry(QtCore.QRect(520, 390, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.usernamet.setFont(font)
        self.usernamet.setInputMask("")
        self.usernamet.setText("")
        self.usernamet.setObjectName("usernamet")
        self.heading = QtWidgets.QLabel(Dialog5)
        self.heading.setGeometry(QtCore.QRect(400, 110, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.heading.setFont(font)
        self.heading.setObjectName("heading")
        self.passwordt = QtWidgets.QLineEdit(Dialog5)
        self.passwordt.setGeometry(QtCore.QRect(520, 460, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordt.setFont(font)
        self.passwordt.setObjectName("passwordt")
        self.pushButton = QtWidgets.QPushButton(Dialog5)
        self.pushButton.setGeometry(QtCore.QRect(470, 580, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        #
        self.pushButton.clicked.connect(self.InsertData)
        self.pushButton.clicked.connect(self.details)
        
        self.label_2 = QtWidgets.QLabel(Dialog5)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1111, 71))
        self.label_2.setStyleSheet("\n"
"background-color: rgb(0, 170, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog5)
        self.layoutWidget.setGeometry(QtCore.QRect(500, 370, 16, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(Dialog5)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog5)
        QtCore.QMetaObject.connectSlotsByName(Dialog5)

    def retranslateUi(self, Dialog5):
        _translate = QtCore.QCoreApplication.translate
        Dialog5.setWindowTitle(_translate("Dialog5", "Dialog"))
        self.password.setText(_translate("Dialog5", "PASSWORD"))
        self.username.setText(_translate("Dialog5", "USERNAME"))
        self.usernamet.setPlaceholderText(_translate("Dialog5", "Enter Moodle ID"))
        self.usernamet.textChanged.connect(self.newText)
        self.heading.setText(_translate("Dialog5", "RAILWAY CONCESSION"))
        self.pushButton.setText(_translate("Dialog5", "Next"))
        self.label_3.setText(_translate("Dialog5", ":"))
        self.label.setText(_translate("Dialog5", ":"))
        self.label_5.setText(_translate("Dialog5", "New user"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog5 = QtWidgets.QDialog()
    ui = Ui_Dialog5()
    ui.setupUi(Dialog5)
    Dialog5.show()
    sys.exit(app.exec_())


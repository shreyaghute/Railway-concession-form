# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ppform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from aadonthavepass import Ui_Dialog7
from aainfo import Ui_Dialog8
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

class Ui_Dialog3(object):
    def InsertData(self):
        con= mdb.connector.connect(host="localhost",user="root", passwd="",db="railway_concession")

        #with con:
        cur = con.cursor()  
        cur.execute('''INSERT INTO `form`(`ticket_no`, `class`, `e_station`, `s_date`, `e_date`, `voucher_no`, `ec_station`, `period`, `c_class`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                           ( self.ticketnt.text(),
                             self.classbox.currentText(),
                             self.estationbox.currentText(),
                             self.lineEdit.text(),
                             self.lineEdit_2.text(),
                             self.vouchert.text(),
                             self.cestationbox.currentText(),
                             self.periodclass.currentText(),
                             self.cclassbox.currentText(),
                                                          
                                                          )
                       )            
        cur.close()
        #QMessageBox.information(self, "Connection", "Data Inserted Successfully")
        self.ticketnt.setText('')
        self.classbox.currentText('')
        self.estationbox.currentText('')
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.vouchert.setText('')
        self.cestationbox.currentText('')
        self.periodclass.currentText('')
        self.cclassbox.currentText('')
        
        
        
        self.initWindow() 
    def newText(self):
        if self.ticketnt.text() and self.classbox.currentText() and self.estationbox.currentText() and self.lineEdit.text() and self.lineEdit_2.text() and self.vouchert.text() and self.cestationbox.currentText() and self.periodclass.currentText() and self.cclassbox.currentText() :
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)
            
    def clickhere(self):
        self.aadonthavepassWindow=QtWidgets.QDialog()
        self.ui=Ui_Dialog7()
        self.ui.setupUi(self.aadonthavepassWindow)
        self.aadonthavepassWindow.show()
        
    def info(self):
        self.aainfoWindow=QtWidgets.QDialog()
        self.ui=Ui_Dialog8()
        self.ui.setupUi(self.aainfoWindow)
        self.aainfoWindow.show()
    
    def setupUi(self, Dialog3):
        Dialog3.setObjectName("Dialog3")
        Dialog3.resize(1108, 867)
        Dialog3.setStyleSheet("\n"
"background-color:rgb(255, 255, 255);\n"
"\n"
"")
        self.previout = QtWidgets.QLabel(Dialog3)
        self.previout.setGeometry(QtCore.QRect(10, 390, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setUnderline(False)
        self.previout.setFont(font)
        self.previout.setObjectName("previout")
        self.currentt = QtWidgets.QLabel(Dialog3)
        self.currentt.setGeometry(QtCore.QRect(560, 400, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setUnderline(False)
        self.currentt.setFont(font)
        self.currentt.setObjectName("currentt")
        self.layoutWidget = QtWidgets.QWidget(Dialog3)
        self.layoutWidget.setGeometry(QtCore.QRect(580, 440, 163, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cestation = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cestation.setFont(font)
        self.cestation.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cestation.setObjectName("cestation")
        self.verticalLayout_2.addWidget(self.cestation)
        self.period = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.period.setFont(font)
        self.period.setObjectName("period")
        self.verticalLayout_2.addWidget(self.period)
        self.cclass = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cclass.setFont(font)
        self.cclass.setObjectName("cclass")
        self.verticalLayout_2.addWidget(self.cclass)
        self.submit = QtWidgets.QPushButton(Dialog3)
        self.submit.setGeometry(QtCore.QRect(490, 800, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        #
        self.submit.clicked.connect(self.InsertData)
        self.submit.clicked.connect(self.info)
        
        self.urllink = QtWidgets.QCommandLinkButton(Dialog3)
        self.urllink.setGeometry(QtCore.QRect(280, 340, 131, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.urllink.setFont(font)
        self.urllink.setObjectName("urllink")
        #
        self.urllink.clicked.connect(self.clickhere)
        
        self.dontt = QtWidgets.QLabel(Dialog3)
        self.dontt.setGeometry(QtCore.QRect(10, 350, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dontt.setFont(font)
        self.dontt.setObjectName("dontt")
        self.pleaset = QtWidgets.QLabel(Dialog3)
        self.pleaset.setGeometry(QtCore.QRect(10, 750, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.pleaset.setFont(font)
        self.pleaset.setObjectName("pleaset")
        self.layoutWidget1 = QtWidgets.QWidget(Dialog3)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 430, 163, 291))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ticket = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ticket.setFont(font)
        self.ticket.setObjectName("ticket")
        self.verticalLayout.addWidget(self.ticket)
        self.class_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.class_2.setFont(font)
        self.class_2.setObjectName("class_2")
        self.verticalLayout.addWidget(self.class_2)
        self.etation = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etation.setFont(font)
        self.etation.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.etation.setObjectName("etation")
        self.verticalLayout.addWidget(self.etation)
        self.sdate = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sdate.setFont(font)
        self.sdate.setObjectName("sdate")
        self.verticalLayout.addWidget(self.sdate)
        self.edate = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.edate.setFont(font)
        self.edate.setObjectName("edate")
        self.verticalLayout.addWidget(self.edate)
        self.vno = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vno.setFont(font)
        self.vno.setObjectName("vno")
        self.verticalLayout.addWidget(self.vno)
        self.label_2 = QtWidgets.QLabel(Dialog3)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1111, 71))
        self.label_2.setStyleSheet("\n"
"background-color: rgb(0, 170, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog3)
        self.label.setGeometry(QtCore.QRect(20, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label.setObjectName("label")
        self.layoutWidget2 = QtWidgets.QWidget(Dialog3)
        self.layoutWidget2.setGeometry(QtCore.QRect(740, 430, 231, 161))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cestationbox = QtWidgets.QComboBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cestationbox.setFont(font)
        self.cestationbox.setObjectName("cestationbox")
        self.cestationbox.addItem("")
        self.cestationbox.addItem("")
        self.verticalLayout_4.addWidget(self.cestationbox)
        self.periodclass = QtWidgets.QComboBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.periodclass.setFont(font)
        self.periodclass.setObjectName("periodclass")
        self.periodclass.addItem("")
        self.periodclass.addItem("")
        self.verticalLayout_4.addWidget(self.periodclass)
        self.cclassbox = QtWidgets.QComboBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cclassbox.setFont(font)
        self.cclassbox.setObjectName("cclassbox")
        self.cclassbox.addItem("")
        self.cclassbox.addItem("")
        self.verticalLayout_4.addWidget(self.cclassbox)
        self.layoutWidget3 = QtWidgets.QWidget(Dialog3)
        self.layoutWidget3.setGeometry(QtCore.QRect(200, 420, 221, 321))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ticketnt = QtWidgets.QLineEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ticketnt.setFont(font)
        self.ticketnt.setObjectName("ticketnt")
        self.verticalLayout_5.addWidget(self.ticketnt)
        self.classbox = QtWidgets.QComboBox(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.classbox.setFont(font)
        self.classbox.setObjectName("classbox")
        self.classbox.addItem("")
        self.classbox.addItem("")
        self.verticalLayout_5.addWidget(self.classbox)
        self.estationbox = QtWidgets.QComboBox(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.estationbox.setFont(font)
        self.estationbox.setObjectName("estationbox")
        self.estationbox.addItem("")
        self.estationbox.addItem("")
        self.verticalLayout_5.addWidget(self.estationbox)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.vouchert = QtWidgets.QLineEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vouchert.setFont(font)
        self.vouchert.setObjectName("vouchert")
        self.verticalLayout_5.addWidget(self.vouchert)
        self.label_3 = QtWidgets.QLabel(Dialog3)
        self.label_3.setGeometry(QtCore.QRect(190, 90, 711, 251))
        self.label_3.setStyleSheet("image: url(:/newPrefix/ticket.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog3)
        self.classbox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog3)

    def retranslateUi(self, Dialog3):
        _translate = QtCore.QCoreApplication.translate
        Dialog3.setWindowTitle(_translate("Dialog3", "Dialog"))
        self.previout.setText(_translate("Dialog3", "Previous Pass Details :"))
        self.currentt.setText(_translate("Dialog3", "Current Pass Details :"))
        self.cestation.setText(_translate("Dialog3", "Ending Station :"))
        self.period.setText(_translate("Dialog3", "Period :"))
        self.cclass.setText(_translate("Dialog3", "Train Class :"))
        self.submit.setText(_translate("Dialog3", "Submit"))
        self.urllink.setText(_translate("Dialog3", "Click Here"))
        self.dontt.setText(_translate("Dialog3", "Don\'t have previous pass ?"))
        self.pleaset.setText(_translate("Dialog3", "* Please check whether the voucher Number  you filled is correct."))
        self.ticket.setText(_translate("Dialog3", "Ticket Number :"))
        self.class_2.setText(_translate("Dialog3", "Train Class :"))
        self.etation.setText(_translate("Dialog3", "Ending Station :"))
        self.sdate.setText(_translate("Dialog3", "Starting Date :"))
        self.edate.setText(_translate("Dialog3", "Ending Date :"))
        self.vno.setText(_translate("Dialog3", "Voucher Number :"))
        self.label.setText(_translate("Dialog3", "Concession Form"))
        self.cestationbox.setItemText(0, _translate("Dialog3", "Vidyavihar"))
        self.cestationbox.setItemText(1, _translate("Dialog3", "SantaCruz"))
        self.periodclass.setItemText(0, _translate("Dialog3", "Monthly"))
        self.periodclass.setItemText(1, _translate("Dialog3", "Quaterly"))
        self.cclassbox.setItemText(0, _translate("Dialog3", "First"))
        self.cclassbox.setItemText(1, _translate("Dialog3", "Second"))
        self.classbox.setItemText(0, _translate("Dialog3", "First"))
        self.classbox.setItemText(1, _translate("Dialog3", "Second"))
        self.estationbox.setItemText(0, _translate("Dialog3", "Vidyavihar"))
        self.estationbox.setItemText(1, _translate("Dialog3", "SantaCruz"))
        self.lineEdit.setPlaceholderText(_translate("Dialog3", "YYYY-MM-DD"))
        self.lineEdit.textChanged.connect(self.newText)
        self.lineEdit_2.setPlaceholderText(_translate("Dialog3", "YYYY-MM-DD"))
        self.lineEdit_2.textChanged.connect(self.newText)

import new

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog3 = QtWidgets.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(Dialog3)
    Dialog3.show()
    sys.exit(app.exec_())


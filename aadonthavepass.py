# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ppdonthavepass.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
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

class Ui_Dialog7(object):
    def InsertData(self):
        con= mdb.connector.connect(host="localhost",user="root", passwd="",db="railway_concession")

        #with con:
        cur = con.cursor()  
        cur.execute('''INSERT INTO `newusers_form`(`e_station`, `peroid`, `class`) VALUES (%s, %s, %s)''', 
                           ( self.cestationbox.currentText(),
                             self.periodclass.currentText(),
                             self.cclassbox.currentText(),
                                                          
                                                          )
                       )            
        cur.close()
        #QMessageBox.information(self, "Connection", "Data Inserted Successfully")
        self.cestationbox.currentText('')
        self.periodclass.currentText('')
        self.cclassbox.currentText('')
        
        
        
        self.initWindow() 
    def newText(self):
        if self.cestationbox.currentText() and self.periodclass.currentText() and self.cclassbox.currentText() :
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)
    def info(self):
        self.aainfoWindow=QtWidgets.QDialog()
        self.ui=Ui_Dialog8()
        self.ui.setupUi(self.aainfoWindow)
        self.aainfoWindow.show()
        
    def setupUi(self, Dialog7):
        Dialog7.setObjectName("Dialog7")
        Dialog7.resize(1107, 867)
        Dialog7.setStyleSheet("QDialog{background-color: rgb(255, 255, 255);}")
        self.layoutWidget = QtWidgets.QWidget(Dialog7)
        self.layoutWidget.setGeometry(QtCore.QRect(520, 310, 231, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cestationbox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cestationbox.setFont(font)
        self.cestationbox.setObjectName("cestationbox")
        self.cestationbox.addItem("")
        self.cestationbox.addItem("")
        self.verticalLayout_4.addWidget(self.cestationbox)
        self.periodclass = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.periodclass.setFont(font)
        self.periodclass.setObjectName("periodclass")
        self.periodclass.addItem("")
        self.periodclass.addItem("")
        self.verticalLayout_4.addWidget(self.periodclass)
        self.cclassbox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cclassbox.setFont(font)
        self.cclassbox.setObjectName("cclassbox")
        self.cclassbox.addItem("")
        self.cclassbox.addItem("")
        self.verticalLayout_4.addWidget(self.cclassbox)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog7)
        self.layoutWidget_2.setGeometry(QtCore.QRect(360, 320, 163, 141))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cestation = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cestation.setFont(font)
        self.cestation.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cestation.setObjectName("cestation")
        self.verticalLayout_2.addWidget(self.cestation)
        self.period = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.period.setFont(font)
        self.period.setObjectName("period")
        self.verticalLayout_2.addWidget(self.period)
        self.cclass = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cclass.setFont(font)
        self.cclass.setObjectName("cclass")
        self.verticalLayout_2.addWidget(self.cclass)
        self.currentt = QtWidgets.QLabel(Dialog7)
        self.currentt.setGeometry(QtCore.QRect(300, 270, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setUnderline(False)
        self.currentt.setFont(font)
        self.currentt.setObjectName("currentt")
        self.submit = QtWidgets.QPushButton(Dialog7)
        self.submit.setGeometry(QtCore.QRect(470, 530, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        #
        self.submit.clicked.connect(self.InsertData)
        self.submit.clicked.connect(self.info)
        
        self.label_2 = QtWidgets.QLabel(Dialog7)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1111, 71))
        self.label_2.setStyleSheet("\n"
"background-color: rgb(0, 170, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog7)
        self.label.setGeometry(QtCore.QRect(20, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog7)
        QtCore.QMetaObject.connectSlotsByName(Dialog7)

    def retranslateUi(self, Dialog7):
        _translate = QtCore.QCoreApplication.translate
        Dialog7.setWindowTitle(_translate("Dialog7", "Dialog"))
        self.cestationbox.setItemText(0, _translate("Dialog7", "Vidyavihar"))
        self.cestationbox.setItemText(1, _translate("Dialog7", "SantaCruz"))
        self.periodclass.setItemText(0, _translate("Dialog7", "Monthly"))
        self.periodclass.setItemText(1, _translate("Dialog7", "Quaterly"))
        self.cclassbox.setItemText(0, _translate("Dialog7", "First"))
        self.cclassbox.setItemText(1, _translate("Dialog7", "Second"))
        self.cestation.setText(_translate("Dialog7", "Ending Station :"))
        self.period.setText(_translate("Dialog7", "Period :"))
        self.cclass.setText(_translate("Dialog7", "Train Class :"))
        self.currentt.setText(_translate("Dialog7", "Current Pass Details :"))
        self.submit.setText(_translate("Dialog7", "Submit"))
        self.label.setText(_translate("Dialog7", "Concession Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog7 = QtWidgets.QDialog()
    ui = Ui_Dialog7()
    ui.setupUi(Dialog7)
    Dialog7.show()
    sys.exit(app.exec_())


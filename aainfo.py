# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ppinfo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog8(object):
    def login(self):
        self.ppchooseWindow=QtWidgets.QDialog()
        self.ui=Ui_Dialog2()
        self.ui.setupUi(self.ppchooseWindow)
        self.ppchooseWindow.show()
        
    def setupUi(self, Dialog8):
        Dialog8.setObjectName("Dialog8")
        Dialog8.resize(1227, 871)
        Dialog8.setStyleSheet("QDialog{background-color: rgb(255, 255, 255);}")
        self.label = QtWidgets.QLabel(Dialog8)
        self.label.setGeometry(QtCore.QRect(460, 330, 371, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog8)
        self.pushButton.setGeometry(QtCore.QRect(480, 450, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        #
        self.pushButton.clicked.connect(self.login)

        self.retranslateUi(Dialog8)
        QtCore.QMetaObject.connectSlotsByName(Dialog8)

    def retranslateUi(self, Dialog8):
        _translate = QtCore.QCoreApplication.translate
        Dialog8.setWindowTitle(_translate("Dialog8", "Dialog"))
        self.label.setText(_translate("Dialog8", "Information Successfully Updated !!"))
        self.pushButton.setText(_translate("Dialog8", "Go back to Main Window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog8 = QtWidgets.QDialog()
    ui = Ui_Dialog8()
    ui.setupUi(Dialog8)
    Dialog8.show()
    sys.exit(app.exec_())


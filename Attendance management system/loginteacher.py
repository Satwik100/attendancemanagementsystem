# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\loginteacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from http.client import OK
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="attendance",
  port=3307
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(646, 605)
        Dialog.setStyleSheet("background-color:rgb(54,54,54);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 50, 348, 65))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("\n"
"color:rgb(231, 251, 255)")
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 440, 282, 109))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(165, 251, 255)")
        self.label_4.setObjectName("label_4")
        self.pregister = QtWidgets.QPushButton(Dialog)
        self.pregister.setGeometry(QtCore.QRect(250, 470, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pregister.setFont(font)
        self.pregister.setStyleSheet("background-color:rgb(255, 70, 24);\n"
"color:rgb(165, 251, 255)\n"
"\n"
"")
        self.pregister.setObjectName("pregister")
        self.pclear = QtWidgets.QPushButton(Dialog)
        self.pclear.setGeometry(QtCore.QRect(350, 350, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pclear.setFont(font)
        self.pclear.setStyleSheet("background-color:rgb(255, 70, 24);\n"
"color:rgb(165, 251, 255)")
        self.pclear.setObjectName("pclear")
        self.plogin = QtWidgets.QPushButton(Dialog)
        self.plogin.setGeometry(QtCore.QRect(40, 350, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.plogin.setFont(font)
        self.plogin.setStyleSheet("background-color:rgb(255, 70, 24);\n"
"color:rgb(165, 251, 255)\n"
"\n"
"")
        self.plogin.setObjectName("plogin")
        self.tpassword = QtWidgets.QLineEdit(Dialog)
        self.tpassword.setGeometry(QtCore.QRect(240, 250, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tpassword.setFont(font)
        self.tpassword.setStyleSheet("background-color:rgb(221, 255, 254)")
        self.tpassword.setText("")
        self.tpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tpassword.setObjectName("tpassword")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 240, 171, 79))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(165, 251, 255)")
        self.label_3.setObjectName("label_3")
        self.tusername = QtWidgets.QLineEdit(Dialog)
        self.tusername.setGeometry(QtCore.QRect(240, 140, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tusername.setFont(font)
        self.tusername.setStyleSheet("background-color:rgb(221, 255, 254)")
        self.tusername.setText("")
        self.tusername.setObjectName("tusername")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 161, 64))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(165, 251, 255)")
        self.label_2.setObjectName("label_2")

        self.plogin.clicked.connect(self.teacherlogin)
        self.pregister.clicked.connect(self.preglogin)

        self.retranslateUi(Dialog)
        self.pclear.clicked.connect(self.tusername.clear) # type: ignore
        self.pclear.clicked.connect(self.tpassword.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Login Portal"))
        self.label_4.setText(_translate("Dialog", "New account ?"))
        self.pregister.setText(_translate("Dialog", "Register here"))
        self.pclear.setText(_translate("Dialog", "Clear"))
        self.plogin.setText(_translate("Dialog", "Log in"))
        self.label_3.setText(_translate("Dialog", " Password "))
        self.label_2.setText(_translate("Dialog", "Username:"))

    def teacherlogin(self):
            username=self.tusername.text()
            password=self.tpassword.text()
            mycursor=mydb.cursor()
            getLoggedInsql = f'SELECT * FROM faculty WHERE username ="{username}" AND password="{password}"'
            mycursor.execute(getLoggedInsql)
            result = mycursor.fetchall()
            if (len(result) == 1): 
                msg=QMessageBox()
                msg.setText("Login successful")
                msg.setWindowTitle("show info")
                msg.setStandardButtons(QMessageBox.Ok)
                retval=msg.exec_()
                if OK:
                        lastteacher="insert into teacherloggedin(username) values('"+username+"')"
                        mycursor.execute(lastteacher)
                        mydb.commit()
                        # teacherloggedin=f'INSERT INTO teacherlogged values ('"+firstname+"')'
                        from teacherend import Ui_Dialog
                        Dialog = QtWidgets.QDialog()
                        ui = Ui_Dialog()
                        ui.setupUi(Dialog)
                        X=Dialog.exec() 
                        
                        
                        # valuet=mycursor.fetchall()        
                        # print(valuet)

            else:
                        msg=QMessageBox()
                        msg.setText("Wrong credentials")
                        msg.setWindowTitle("show error")
                        msg.setStandardButtons(QMessageBox.Ok)
                        retval=msg.exec_()
                        self.tusername.clear()
                        self.tpassword.clear()

    def preglogin(self):
                from teacherregistration import Ui_Dialog
                Dialog = QtWidgets.QDialog()
                ui = Ui_Dialog()
                ui.setupUi(Dialog)
                X=Dialog.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\teacherend.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(521, 284)
        Dialog.setMouseTracking(True)
        Dialog.setStyleSheet("background-color:rgb(54,54,54);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 10, 431, 65))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("\n"
"color:rgb(231, 251, 255)")
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.classroutine = QtWidgets.QPushButton(Dialog)
        self.classroutine.setGeometry(QtCore.QRect(30, 90, 221, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.classroutine.setFont(font)
        self.classroutine.setStyleSheet("background-color:rgb(85, 255, 255);\n"
"\n"
"")
        self.classroutine.setObjectName("classroutine")
        self.classdetails = QtWidgets.QPushButton(Dialog)
        self.classdetails.setGeometry(QtCore.QRect(270, 90, 221, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.classdetails.setFont(font)
        self.classdetails.setStyleSheet("background-color:rgb(85, 255, 255);\n"
"\n"
"")
        self.classdetails.setObjectName("classdetails")

        self.classdetails.clicked.connect(self.showclass)
        self.classroutine.clicked.connect(self.rout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Teacher/Evaluator End"))
        self.classroutine.setText(_translate("Dialog", "My Routine"))
        self.classdetails.setText(_translate("Dialog", "Class Details"))

    def showclass(self):
                from attendance import Ui_Dialog
                Dialog = QtWidgets.QDialog()
                ui = Ui_Dialog()
                ui.setupUi(Dialog)
                X=Dialog.exec()

    def rout(self):
        from myroutine import Ui_Dialog
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

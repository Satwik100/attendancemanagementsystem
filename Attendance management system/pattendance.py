# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\attendance.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from http.client import OK
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.QtWidgets import QCalendarWidget

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
        Dialog.resize(1303, 906)
        Dialog.setStyleSheet("background-color:rgb(54,54,54);")
        self.classsection = QtWidgets.QComboBox(Dialog)
        self.classsection.setGeometry(QtCore.QRect(40, 20, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.classsection.setFont(font)
        self.classsection.setStyleSheet("background-color:rgb(19, 31, 59);\n"
"color:rgb(170, 255, 255)")
        self.classsection.setObjectName("classsection")
        self.classsection.addItem("")
        self.selectclass = QtWidgets.QPushButton(Dialog)
        self.selectclass.setGeometry(QtCore.QRect(320, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.selectclass.setFont(font)
        self.selectclass.setStyleSheet("background-color:rgb(31, 54, 24);\n"
"color:rgb(165, 251, 255)\n"
"\n"
"")
        self.selectclass.setObjectName("selectclass")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 90, 1271, 721))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.takeattendance = QtWidgets.QPushButton(self.page)
        self.takeattendance.setGeometry(QtCore.QRect(610, 530, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.takeattendance.setFont(font)
        self.takeattendance.setStyleSheet("background-color:rgb(6, 21, 72);\n"
"color:rgb(165, 251, 255)\n"
"\n"
"")
        self.takeattendance.setObjectName("takeattendance")
        self.tableWidget = QtWidgets.QTableWidget(self.page)
        self.tableWidget.setGeometry(QtCore.QRect(40, 30, 771, 481))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color:rgb(0, 255, 255)")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.calendar = QtWidgets.QCalendarWidget(self.page_2)
        self.calendar.setGeometry(QtCore.QRect(20, 0, 441, 281))
        self.calendar.setStyleSheet("background-color:rgb(174, 254, 255);\n"
"color:rgb(9, 9, 9)")
        self.calendar.setObjectName("calendar")
        self.list1 = QtWidgets.QListWidget(self.page_2)
        self.list1.setGeometry(QtCore.QRect(20, 360, 311, 381))
        self.list1.setStyleSheet("background-color:rgb(174, 254, 255);\n"
"color:rgb(9, 9, 9)")
        self.list1.setObjectName("list1")
        self.lineEdit = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit.setGeometry(QtCore.QRect(840, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgb(174, 254, 255);\n"
"color:rgb(9, 9, 9)")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(530, 20, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color:rgb(170, 255, 255)")
        self.label.setObjectName("label")
        self.list2 = QtWidgets.QListWidget(self.page_2)
        self.list2.setGeometry(QtCore.QRect(360, 360, 321, 381))
        self.list2.setStyleSheet("background-color:rgb(174, 254, 255);\n"
"color:rgb(9, 9, 9)")
        self.list2.setObjectName("list2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(30, 310, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color:rgb(170, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(370, 310, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"color:rgb(170, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(480, 130, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"color:rgb(170, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.page_2)
        self.textEdit.setGeometry(QtCore.QRect(690, 110, 571, 131))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color:rgb(255, 221, 249)")
        self.textEdit.setObjectName("textEdit")
        self.saveattendance = QtWidgets.QPushButton(self.page_2)
        self.saveattendance.setGeometry(QtCore.QRect(720, 410, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.saveattendance.setFont(font)
        self.saveattendance.setStyleSheet("background-color:rgb(174, 254, 255);\n"
"color:rgb(9, 9, 9)")
        self.saveattendance.setObjectName("saveattendance")
        self.saveattendance_2 = QtWidgets.QPushButton(self.page_2)
        self.saveattendance_2.setGeometry(QtCore.QRect(720, 500, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.saveattendance_2.setFont(font)
        self.saveattendance_2.setStyleSheet("background-color:rgb(174, 254, 255);\n"
"color:rgb(9, 9, 9)")
        self.saveattendance_2.setObjectName("saveattendance_2")
        self.stackedWidget.addWidget(self.page_2)

        classcursor = mydb.cursor()
        sql="select *from classsec"
        classcursor.execute(sql)
        addclass = classcursor.fetchall()
        # print(addclass)
        for row in addclass:
                self.classsection.addItem(str(row[0]))
        classcursor.close()

        self.selectclass.clicked.connect(self.studentdetails)
        self.takeattendance.clicked.connect(self.take)
        self.saveattendance_2.clicked.connect(self.goback)

        self.list1.itemDoubleClicked.connect(self.removelist1)
        self.list2.itemDoubleClicked.connect(self.removelist2)

        self.saveattendance.clicked.connect(self.save)

        self.calendar.selectionChanged.connect(self.calendarDateChanged)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.classsection.setItemText(0, _translate("Dialog", "Select Students"))
        self.selectclass.setText(_translate("Dialog", "Select"))
        self.takeattendance.setText(_translate("Dialog", "Take Attendance"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Full name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Phone no"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Year"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Attendance  "))
        self.label.setText(_translate("Dialog", "Please confirm your name :"))
        self.label_2.setText(_translate("Dialog", "Students list:"))
        self.label_3.setText(_translate("Dialog", "Attendees:"))
        self.label_5.setText(_translate("Dialog", "Point to be noted: "))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Double click on students list to take attendance.You can undo this operation by double clicking a particular student from attendees list.Click on save button to save attendance.</span></p></body></html>"))
        self.saveattendance.setText(_translate("Dialog", "Save "))
        self.saveattendance_2.setText(_translate("Dialog", "Go back"))

    def studentdetails(self):

        self.list1.clear()
        self.list2.clear()
        if self.classsection.currentText()=='Select Students':
                msg=QMessageBox()
                msg.setText("Please select class")
                msg.setWindowTitle("show error")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                retval=msg.exec_()
                
        else:
                con=mydb.cursor()
                sql=f'select*from {self.classsection.currentText()}'
                con.execute(sql)
                detail=con.fetchall()
            
                # print(detail)
                rowline=0
                self.tableWidget.setRowCount(len(detail))

                for i in detail:
                        self.tableWidget.setItem(rowline, 0, QtWidgets.QTableWidgetItem(str(i[0])))
                        self.tableWidget.setItem(rowline, 1, QtWidgets.QTableWidgetItem(i[1]))
                        self.tableWidget.setItem(rowline, 2, QtWidgets.QTableWidgetItem(i[2]))
                        self.tableWidget.setItem(rowline, 3, QtWidgets.QTableWidgetItem(str(i[3])))
                        self.tableWidget.setItem(rowline, 4, QtWidgets.QTableWidgetItem(str(i[4])))
                        rowline=rowline+1

                
                selectstudents=f"select Roll,name from {self.classsection.currentText()} "
                # c=mydb.cursor()
                con.execute(selectstudents)
                studentslist=con.fetchall()
                # print(studentslist)
                # print(studentslist[0][1])
                # print(studentslist)
                # studentslist=list(studentslist)

                for i in studentslist:
                        # print(i)
                        self.list1.addItem(str(i))
                        # print(i)
                print(studentslist)

    def take(self):
             self.stackedWidget.setCurrentWidget(self.page_2)

    def goback(self):
             self.stackedWidget.setCurrentWidget(self.page)

    def removelist1(self,item):
            self.list1.takeItem(self.list1.row(item))
            
            self.list2.addItem(item.text())

    def removelist2(self,item):
        self.list2.takeItem(self.list2.row(item))
        self.list1.addItem(item.text())

    def save(self):
            


            listcount=self.list2.count() 
            if self.classsection.currentText()=='Select Students':
                msg=QMessageBox()
                msg.setText("Please select class")
                msg.setWindowTitle("show error")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                retval=msg.exec_()
            elif len(self.lineEdit.text())==0:
                msg=QMessageBox()
                msg.setText("Please enter your proper name")
                msg.setWindowTitle("error")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                retval=msg.exec_()

            else:
                # grabbed_date=self.calendar.selectedDate().toPyDate()
                #     print(grabbed_date)
                

                if listcount==0:
                        msg=QMessageBox()
                        msg.setText("Please mark attendance properly")
                        msg.setWindowTitle("error")
                        msg.setIcon(QMessageBox.Warning)
                        msg.setStandardButtons(QMessageBox.Ok)
                        retval=msg.exec_()
                else:
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setText("After saving you won't be able to edit or modify the attendees.Are you sure you want to save")
                        msgBox.setWindowTitle("QMessageBox ")
                        msgBox.setIcon(QtWidgets.QMessageBox.Question)
                        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                        returnValue = msgBox.exec()
                        if returnValue == QtWidgets.QMessageBox.Ok:
                                self.attendancesaved()
                        else:
                                return 

            
    def calendarDateChanged(self):
            print(self.calendar.selectedDate().toPyDate())

    def attendancesaved(self):
        

        # selected=[]
        # for i in range(self.list2.count()):

        #         selected.append(self.list2.item(i).text())
        #         print(selected)
        # print(list(selected))

        grabbed_date=self.calendar.selectedDate().toPyDate()
        tname=self.lineEdit.text()
        classname=self.classsection.currentText()

        lastteacher="select username from teacherloggedin order by series desc limit 1"
        teachercursor=mydb.cursor()
        teachercursor.execute(lastteacher)
        solved=list(teachercursor.fetchone())[0]
        #     print(solved)
            
        teachername="select first_name,last_name from faculty where username='"+solved+"' "
        teachercursor.execute(teachername)
        firstlast=list(teachercursor.fetchone())
        firstlast=firstlast[0]+" "+firstlast[1]
        # print(firstlast)


        if firstlast!=tname:
                msg=QMessageBox()
                msg.setText("Please enter correct name")
                msg.setWindowTitle("error")
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                retval=msg.exec_()
                if OK: 
                        return  




        absentees=""
        for i in range(self.list1.count()):
                abscurrent=self.list1.item(i).text()
                st=abscurrent[1:len(abscurrent)-1]
                absentees+=st
                if i<self.list1.count()-1:
                        absentees+=","
        print(absentees)

       
        selected=""

        for i in range(self.list2.count()):
                # print(self.list2.item(i).text())

                single=self.list2.item(i).text()
                # print(sel)
                sa=single[1:len(single)-1]
                selected+=sa
                if i<self.list2.count()-1:
                        selected+=","
                print(sa)
                # print(single[0])
                st=sa.index(",")
                # print(st)
                idno=int(sa[0:st])
                print(idno)
                updateattendance=f"update {classname} set attendance=attendance+1 where Roll={idno}"
                update=mydb.cursor()
                update.execute(updateattendance)
                mydb.commit()

                # insertattendance="Insert into dates,attendance_taken_by,class,students_present,absentees_list"
        print(selected)

        attendancebydate="""INSERT INTO Attendance_daywise(dates,attendance_taken_by, username, class, students_present, absentees_list)
        VALUES (%s, %s, %s, %s, %s, %s)"""
        val= (grabbed_date,tname,solved,classname,selected,absentees)
        teachercursor.execute(attendancebydate, val)
        mydb.commit()

        msg=QMessageBox()
        msg.setText("attendance saved")
        msg.setWindowTitle("done")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        retval=msg.exec_()
        
       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(501, 184)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 471, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hours_label = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.hours_label.setObjectName("hours_label")
        self.horizontalLayout.addWidget(self.hours_label)
        self.minutes_input = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.minutes_input.setObjectName("minutes_input")
        self.horizontalLayout.addWidget(self.minutes_input)
        self.seconds_input = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.seconds_input.setObjectName("seconds_input")
        self.horizontalLayout.addWidget(self.seconds_input)
        self.minutes_label = QtWidgets.QLabel(Dialog)
        self.minutes_label.setGeometry(QtCore.QRect(190, 20, 91, 31))
        self.minutes_label.setObjectName("minutes_label")
        self.seconds_label = QtWidgets.QLabel(Dialog)
        self.seconds_label.setGeometry(QtCore.QRect(350, 20, 91, 31))
        self.seconds_label.setObjectName("seconds_label")
        self.hours_label_2 = QtWidgets.QLabel(Dialog)
        self.hours_label_2.setGeometry(QtCore.QRect(30, 20, 81, 31))
        self.hours_label_2.setObjectName("hours_label_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(60, 100, 371, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clear_btn_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.clear_btn_2.setObjectName("clear_btn_2")
        self.horizontalLayout_2.addWidget(self.clear_btn_2)
        self.clear_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_2.addWidget(self.clear_btn)
        self.submit_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.submit_btn.setObjectName("submit_btn")
        self.horizontalLayout_2.addWidget(self.submit_btn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.minutes_label.setText(_translate("Dialog", "Minutes"))
        self.seconds_label.setText(_translate("Dialog", "Seconds"))
        self.hours_label_2.setText(_translate("Dialog", "Hours"))
        self.clear_btn_2.setText(_translate("Dialog", "Init Server"))
        self.clear_btn.setText(_translate("Dialog", "Clear"))
        self.submit_btn.setText(_translate("Dialog", "Submit"))

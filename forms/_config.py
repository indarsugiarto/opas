# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Config(object):
    def setupUi(self, Config):
        Config.setObjectName("Config")
        Config.resize(800, 500)
        Config.setMinimumSize(QtCore.QSize(800, 500))
        Config.setMaximumSize(QtCore.QSize(800, 500))
        self.label = QtWidgets.QLabel(Config)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 16))
        self.label.setObjectName("label")
        self.ipAddr = QtWidgets.QLineEdit(Config)
        self.ipAddr.setGeometry(QtCore.QRect(20, 40, 113, 23))
        self.ipAddr.setObjectName("ipAddr")
        self.label_2 = QtWidgets.QLabel(Config)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 131, 16))
        self.label_2.setObjectName("label_2")
        self.s1Loc = QtWidgets.QPlainTextEdit(Config)
        self.s1Loc.setGeometry(QtCore.QRect(20, 100, 361, 51))
        self.s1Loc.setPlainText("")
        self.s1Loc.setObjectName("s1Loc")
        self.label_3 = QtWidgets.QLabel(Config)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 131, 16))
        self.label_3.setObjectName("label_3")
        self.s2Loc = QtWidgets.QPlainTextEdit(Config)
        self.s2Loc.setGeometry(QtCore.QRect(20, 190, 361, 51))
        self.s2Loc.setPlainText("")
        self.s2Loc.setObjectName("s2Loc")
        self.label_4 = QtWidgets.QLabel(Config)
        self.label_4.setGeometry(QtCore.QRect(20, 260, 131, 16))
        self.label_4.setObjectName("label_4")
        self.s3Loc = QtWidgets.QPlainTextEdit(Config)
        self.s3Loc.setGeometry(QtCore.QRect(20, 280, 361, 51))
        self.s3Loc.setPlainText("")
        self.s3Loc.setObjectName("s3Loc")
        self.label_5 = QtWidgets.QLabel(Config)
        self.label_5.setGeometry(QtCore.QRect(20, 350, 131, 16))
        self.label_5.setObjectName("label_5")
        self.s4Loc = QtWidgets.QPlainTextEdit(Config)
        self.s4Loc.setGeometry(QtCore.QRect(20, 370, 361, 51))
        self.s4Loc.setPlainText("")
        self.s4Loc.setObjectName("s4Loc")
        self.label_6 = QtWidgets.QLabel(Config)
        self.label_6.setGeometry(QtCore.QRect(420, 80, 131, 16))
        self.label_6.setObjectName("label_6")
        self.s5Loc = QtWidgets.QPlainTextEdit(Config)
        self.s5Loc.setGeometry(QtCore.QRect(420, 100, 361, 51))
        self.s5Loc.setPlainText("")
        self.s5Loc.setObjectName("s5Loc")
        self.label_7 = QtWidgets.QLabel(Config)
        self.label_7.setGeometry(QtCore.QRect(420, 170, 131, 16))
        self.label_7.setObjectName("label_7")
        self.s6Loc = QtWidgets.QPlainTextEdit(Config)
        self.s6Loc.setGeometry(QtCore.QRect(420, 190, 361, 51))
        self.s6Loc.setPlainText("")
        self.s6Loc.setObjectName("s6Loc")
        self.label_8 = QtWidgets.QLabel(Config)
        self.label_8.setGeometry(QtCore.QRect(420, 260, 131, 16))
        self.label_8.setObjectName("label_8")
        self.s7Loc = QtWidgets.QPlainTextEdit(Config)
        self.s7Loc.setGeometry(QtCore.QRect(420, 280, 361, 51))
        self.s7Loc.setPlainText("")
        self.s7Loc.setObjectName("s7Loc")
        self.label_9 = QtWidgets.QLabel(Config)
        self.label_9.setGeometry(QtCore.QRect(420, 350, 131, 16))
        self.label_9.setObjectName("label_9")
        self.s8Loc = QtWidgets.QPlainTextEdit(Config)
        self.s8Loc.setGeometry(QtCore.QRect(420, 370, 361, 51))
        self.s8Loc.setPlainText("")
        self.s8Loc.setObjectName("s8Loc")
        self.pbSave = QtWidgets.QPushButton(Config)
        self.pbSave.setGeometry(QtCore.QRect(600, 460, 80, 23))
        self.pbSave.setObjectName("pbSave")
        self.pbCancel = QtWidgets.QPushButton(Config)
        self.pbCancel.setGeometry(QtCore.QRect(690, 460, 80, 23))
        self.pbCancel.setObjectName("pbCancel")

        self.retranslateUi(Config)
        QtCore.QMetaObject.connectSlotsByName(Config)

    def retranslateUi(self, Config):
        _translate = QtCore.QCoreApplication.translate
        Config.setWindowTitle(_translate("Config", "Form"))
        self.label.setText(_translate("Config", "Server IP Address:"))
        self.ipAddr.setText(_translate("Config", "10.52.129.2"))
        self.label_2.setText(_translate("Config", "Station-1 Location:"))
        self.label_3.setText(_translate("Config", "Station-2 Location:"))
        self.label_4.setText(_translate("Config", "Station-3 Location:"))
        self.label_5.setText(_translate("Config", "Station-4 Location:"))
        self.label_6.setText(_translate("Config", "Station-5 Location:"))
        self.label_7.setText(_translate("Config", "Station-6 Location:"))
        self.label_8.setText(_translate("Config", "Station-7 Location:"))
        self.label_9.setText(_translate("Config", "Station-8 Location:"))
        self.pbSave.setText(_translate("Config", "Save"))
        self.pbCancel.setText(_translate("Config", "Cancel"))

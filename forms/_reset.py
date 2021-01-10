# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reset.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Reset(object):
    def setupUi(self, Reset):
        Reset.setObjectName("Reset")
        Reset.resize(600, 350)
        Reset.setMinimumSize(QtCore.QSize(600, 350))
        Reset.setMaximumSize(QtCore.QSize(600, 350))
        self.label = QtWidgets.QLabel(Reset)
        self.label.setGeometry(QtCore.QRect(20, 20, 561, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icon/warning.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Reset)
        self.label_2.setGeometry(QtCore.QRect(50, 170, 121, 111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icon/hand_stop.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Reset)
        self.label_3.setGeometry(QtCore.QRect(190, 180, 361, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.pbCancel = QtWidgets.QPushButton(Reset)
        self.pbCancel.setGeometry(QtCore.QRect(450, 290, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pbCancel.setFont(font)
        self.pbCancel.setObjectName("pbCancel")
        self.pbCancel_2 = QtWidgets.QPushButton(Reset)
        self.pbCancel_2.setGeometry(QtCore.QRect(190, 290, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pbCancel_2.setFont(font)
        self.pbCancel_2.setObjectName("pbCancel_2")
        self.pbCancel_3 = QtWidgets.QPushButton(Reset)
        self.pbCancel_3.setGeometry(QtCore.QRect(320, 290, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pbCancel_3.setFont(font)
        self.pbCancel_3.setObjectName("pbCancel_3")

        self.retranslateUi(Reset)
        self.pbCancel.clicked.connect(Reset.close)
        QtCore.QMetaObject.connectSlotsByName(Reset)

    def retranslateUi(self, Reset):
        _translate = QtCore.QCoreApplication.translate
        Reset.setWindowTitle(_translate("Reset", "Warning"))
        self.label_3.setText(_translate("Reset", "Do you want to reset or power-off the station?"))
        self.pbCancel.setText(_translate("Reset", "Cancel"))
        self.pbCancel_2.setText(_translate("Reset", "Reset"))
        self.pbCancel_3.setText(_translate("Reset", "Power-off"))

from . import form_src_rc

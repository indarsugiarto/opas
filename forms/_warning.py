# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Warning(object):
    def setupUi(self, Warning):
        Warning.setObjectName("Warning")
        Warning.resize(600, 350)
        Warning.setMinimumSize(QtCore.QSize(600, 350))
        Warning.setMaximumSize(QtCore.QSize(600, 350))
        self.label = QtWidgets.QLabel(Warning)
        self.label.setGeometry(QtCore.QRect(20, 20, 561, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icon/warning.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Warning)
        self.label_2.setGeometry(QtCore.QRect(50, 170, 121, 111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icon/hand_stop.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Warning)
        self.label_3.setGeometry(QtCore.QRect(200, 180, 361, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Warning)
        self.pushButton.setGeometry(QtCore.QRect(260, 300, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Warning)
        self.pushButton.clicked.connect(Warning.close)
        QtCore.QMetaObject.connectSlotsByName(Warning)

    def retranslateUi(self, Warning):
        _translate = QtCore.QCoreApplication.translate
        Warning.setWindowTitle(_translate("Warning", "Warning"))
        self.label_3.setText(_translate("Warning", "Raspberry pi clients will be terminated at 17:00!"))
        self.pushButton.setText(_translate("Warning", "Close"))

from . import form_src_rc

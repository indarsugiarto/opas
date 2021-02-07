# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reset.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Reset(object):
    def setupUi(self, Reset):
        Reset.setObjectName("Reset")
        Reset.resize(600, 350)
        Reset.setMinimumSize(QtCore.QSize(600, 350))
        Reset.setMaximumSize(QtCore.QSize(600, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/pcr-icon-on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Reset.setWindowIcon(icon)
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
        self.label_3.setGeometry(QtCore.QRect(190, 170, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.pbCancel = QtWidgets.QPushButton(Reset)
        self.pbCancel.setGeometry(QtCore.QRect(450, 300, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pbCancel.setFont(font)
        self.pbCancel.setObjectName("pbCancel")
        self.pbReset = QtWidgets.QPushButton(Reset)
        self.pbReset.setGeometry(QtCore.QRect(190, 300, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pbReset.setFont(font)
        self.pbReset.setObjectName("pbReset")
        self.pbShutdown = QtWidgets.QPushButton(Reset)
        self.pbShutdown.setGeometry(QtCore.QRect(320, 300, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pbShutdown.setFont(font)
        self.pbShutdown.setObjectName("pbShutdown")
        self.label_4 = QtWidgets.QLabel(Reset)
        self.label_4.setGeometry(QtCore.QRect(190, 230, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(204, 0, 0);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Reset)
        self.pbCancel.clicked.connect(Reset.close)
        QtCore.QMetaObject.connectSlotsByName(Reset)

    def retranslateUi(self, Reset):
        _translate = QtCore.QCoreApplication.translate
        Reset.setWindowTitle(_translate("Reset", "Warning"))
        self.label_3.setText(_translate("Reset", "Apakah mau me-reset station atau mematikan (shutdown) station?"))
        self.pbCancel.setText(_translate("Reset", "Cancel"))
        self.pbReset.setText(_translate("Reset", "Reset"))
        self.pbShutdown.setText(_translate("Reset", "Shutdown"))
        self.label_4.setText(_translate("Reset", "Note: Station yang di-shutdown hanya bisa dinyalakan kembali secara manual!"))
from . import form_src_rc

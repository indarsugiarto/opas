# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutForm(object):
    def setupUi(self, AboutForm):
        AboutForm.setObjectName("AboutForm")
        AboutForm.resize(450, 310)
        AboutForm.setMinimumSize(QtCore.QSize(450, 310))
        AboutForm.setMaximumSize(QtCore.QSize(450, 310))
        self.pbClose = QtWidgets.QDialogButtonBox(AboutForm)
        self.pbClose.setGeometry(QtCore.QRect(180, 280, 81, 24))
        self.pbClose.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.pbClose.setObjectName("pbClose")
        self.textEdit = QtWidgets.QTextEdit(AboutForm)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 450, 271))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(AboutForm)
        QtCore.QMetaObject.connectSlotsByName(AboutForm)

    def retranslateUi(self, AboutForm):
        _translate = QtCore.QCoreApplication.translate
        AboutForm.setWindowTitle(_translate("AboutForm", "Online Community Streaming Radio"))
        self.textEdit.setHtml(_translate("AboutForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Radio Komunitas Daring</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Sistem siaran radio berdasarkan konsep IoT (</span><span style=\" font-size:12pt; font-style:italic;\">Internet of Things</span><span style=\" font-size:12pt;\">) yang mendukung pengembangan </span><span style=\" font-size:12pt; font-weight:600;\">Smart Society</span><span style=\" font-size:12pt;\"> dan Mobilitas Masyarakat Modern di era </span><span style=\" font-size:12pt; font-weight:600;\">Society 5.0</span><span style=\" font-size:12pt;\">.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Developer: Petra Campus Radio</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Kontak kami: pcr@petra.ac.id</span></p></body></html>"))


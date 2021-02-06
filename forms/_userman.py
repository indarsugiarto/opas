# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userman.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_userman(object):
    def setupUi(self, userman):
        userman.setObjectName("userman")
        userman.resize(670, 590)
        userman.setMinimumSize(QtCore.QSize(670, 590))
        userman.setMaximumSize(QtCore.QSize(670, 590))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/pcr-icon-on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        userman.setWindowIcon(icon)
        self.tutorialText = QtWidgets.QTextEdit(userman)
        self.tutorialText.setGeometry(QtCore.QRect(0, 0, 670, 540))
        self.tutorialText.setReadOnly(True)
        self.tutorialText.setObjectName("tutorialText")
        self.pbClose = QtWidgets.QPushButton(userman)
        self.pbClose.setGeometry(QtCore.QRect(290, 550, 91, 31))
        self.pbClose.setObjectName("pbClose")

        self.retranslateUi(userman)
        QtCore.QMetaObject.connectSlotsByName(userman)

    def retranslateUi(self, userman):
        _translate = QtCore.QCoreApplication.translate
        userman.setWindowTitle(_translate("userman", "User Manual"))
        self.tutorialText.setHtml(_translate("userman", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">User Manual :</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">1. Monitoring</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Pilih</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\"> File -&gt; Monitor</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">  / simbol </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\"> Monitor</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> / Tekan</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\"> F3</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> untuk membuka tampilan monitor.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Jika di status station </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">&quot;Offline&quot;</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> berarti raspberry sedang dalam keadaan mati.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Jika di status station </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">&quot;Online&quot;</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> dan kolom</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\"> IP</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> muncul angka berarti raspberry sedang dalam keadaan hidup.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">AUX</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> untuk debugging dan meilhat kerja sistem dibalik layar.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">2. Volume Control</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Volume bisa dibesarkan atau dikecilkan dengan slider di setiap kotak station.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">Centang checkbox mute</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> untuk mematikan volume. </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">Hapus centang checkbox mute</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> untuk menghidupkan volume</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">3. Reset</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Jika raspberry mengalami masalah maka tekan tombol</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\"> Reset</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> pada kotak station</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Akan muncul halaman reset.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Tekan tombol</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\"> Reset</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> untuk mematikan lalu menyalakan ulang raspberry</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Tekan tombol </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">Shutdown</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> untuk mematikan raspberry</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Tekan tombol </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">Cancel</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> untuk membatalkan</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">4. Location Info Update </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Pilih </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">File -&gt; Setting</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> / simbo</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">l Setting</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> / Tekan </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">F2</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> untuk membuka tampilan Update info Lokasi</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Tuliskan letak lokasi raspberry dan speaker </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Tekan tombol </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">Save</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> untuk memperbaharui lokasi pada tampilan monitor</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Tekan tombol </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">Cancel</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> untuk membatalkan</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">5. About &amp; User Manual</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Pilih </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">Help -&gt; About</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> / Tekan </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">F12</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> untuk membuka halaman About</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Pilih </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">Help -&gt; Manual</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> / Tekan </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">F1</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> untuk membuka halaman User Manual</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Halaman About berisikan info tentang aplikasi ini.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Halaman User Manual berisikan cara pemakaian dari aplikasi ini.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">6. Reminder</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Pukul </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">16.45</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"> Aplikasi akan menampilkan halaman Reminder</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Halaman ini memberi info tentang waktu raspberry pi akan dimatikan</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.pbClose.setText(_translate("userman", "Close"))
from . import form_src_rc

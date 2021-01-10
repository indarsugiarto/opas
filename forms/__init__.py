from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QMessageBox
import time
from ._mainWindow import Ui_MainWindow
from ._dashboard import Ui_MonitorForm
from ._about import Ui_AboutForm
from ._warning import Ui_Warning
from ._reset import Ui_Reset
from ._config import Ui_Config
"""
-----------------------------------------
Bagian ini berhubungan dengan main Window
Online Public Address System (OPAS)
-----------------------------------------
"""
class opas(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """
        Bikin UI utama
        """
        super(opas,self).__init__(parent)
        #self.MainWindow = QtWidgets.QMainWindow()
        #self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.setCentralWidget(self.mdiArea)
        #self.MainWindow.setCentralWidget(self.ui.mdiArea)
        """
        Bikin UI dashboard
        """
        self.dash = dashboard(self)
        self.subDash = QtWidgets.QMdiSubWindow(self.mdiArea)
        self.subDash.setWidget(self.dash)
        self.mdiArea.addSubWindow(self.subDash)
        self.subDash.hide()

        """
        Lalu UI about
        """
        self.about = about(self)
        self.subAbout = QtWidgets.QMdiSubWindow(self.mdiArea)
        self.subAbout.setWidget(self.about)
        self.mdiArea.addSubWindow(self.subAbout)
        self.subAbout.hide()

        """
        Lalu UI konfigurasi
        """
        self.config = config(self)
        self.subConfig = QtWidgets.QMdiSubWindow(self.mdiArea)
        self.subConfig.setWidget(self.config)
        self.mdiArea.addSubWindow(self.subConfig)
        self.subConfig.hide()

        """
        Tambahan
        """
        self.opStatus = QtWidgets.QLabel("Operator: Lab Radio PCU")
        self.sepStatus = QtWidgets.QLabel("|")
        self.netStatus = QtWidgets.QLabel("Network connected")
        self.statusBar().addWidget(self.netStatus)
        self.statusBar().addWidget(self.sepStatus)
        self.statusBar().addWidget(self.opStatus)
        """
        Timer
        """
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getTime)
        self.timer.setInterval(1000)
        self.timer.start()
        """
        ide: semua di-hide sampai login berhasil
        """
        self.signalslot()

        """
        finally: tampilkan
        """
        self.show()

    def signalslot(self):
        """
        deklarasi mekanisme signal-slot"
        """
        self.action_Monitor.triggered.connect(self.showDashboard)
        self.action_About.triggered.connect(self.showAbout)
        self.action_Keluar.triggered.connect(self.finish)
        self.action_Seting.triggered.connect(self.showConfig)
        self.action_Penggunaan.triggered.connect(self.oops)
        self.pbSetting.clicked.connect(self.showConfig)
        self.pbMon.clicked.connect(self.showDashboard)
        self.pbHelp.clicked.connect(self.oops)

    def oops(self):
        QMessageBox.information(self, 'Error', "Belum selesai dibuat...", QMessageBox.Ok, QMessageBox.Ok)

    def finish(self):
        self.close()

    def getTime(self):
        sekarang = time.localtime()
        d = sekarang.tm_sec; detik = "%02d" % d
        m = sekarang.tm_min; menit = "%02d" % m
        j = sekarang.tm_hour; jam = "%02d" % j
        tgl = "%02d/%02d/%02d" % (sekarang.tm_mday, sekarang.tm_mon, sekarang.tm_year)
        #tampilkan
        self.lcdDetik.display(detik)
        self.lcdMenit.display(menit)
        self.lcdJam.display(jam)
        #self.tanggal.setText(tgl)

    def showDashboard(self):
        """
        Tampilkan dashboard
        """
        self.dash.show()
        #print("Dashboard")

    def showConfig(self):
        self.config.show()

    def showAbout(self):
        """
        Tampilkan identitas program
        """
        self.about.show()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F12:
            self.info = about()
            self.info.setWindowModality(QtCore.Qt.ApplicationModal)
            self.info.show()
            #contoh debugging
            self.dash.dbgConsole.appendPlainText("Tombol F12 ditekan")
        elif event.key() == QtCore.Qt.Key_F2:
            self.showConfig()
        elif event.key() == QtCore.Qt.Key_F3:
            self.showDashboard()
            #buat debugging aja
            self.dash.dbgConsole.appendPlainText("Tombol F3 ditekan, dashboard diaktifkan")
        #buat testing aja, jika tombol F10 ditekan akan muncul warning
        elif event.key() == QtCore.Qt.Key_F10:
            self.warn = warning()
            self.warn.setWindowModality(QtCore.Qt.ApplicationModal)
            self.warn.show()

"""
------------------------------------------------
Bagian ini berhubungan dengan tampilan dashboard
------------------------------------------------
"""
class dashboard(QtWidgets.QWidget, Ui_MonitorForm):
    def __init__(self, parent=None):
        super(dashboard,self).__init__(parent)
        #self.ui = Ui_MonitorForm()
        self.setupUi(self)
        self.signalslot()

    def signalslot(self):
        """
        deklarasi mekanisme signal-slot jika diperlukan"
        """

    def tampilkan(self):
        self.show()

class config(QtWidgets.QWidget, Ui_Config):
    def __init__(self, parent=None):
        super(config,self).__init__(parent)
        self.setupUi(self)
        self.signalslot()

    def signalslot(self):
        """
        Isi nanti jika digunakan
        """

    def tampilkan(self):
        self.show()

class about(QtWidgets.QWidget, Ui_AboutForm):
    def __init__(self, parent=None):
        super(about,self).__init__(parent)
        self.setupUi(self)
        self.pbClose.clicked.connect(self.finish)
    def finish(self):
        self.close()

class warning(QtWidgets.QDialog, Ui_Warning):
    def __init__(self, parent=None):
        super(warning,self).__init__(parent)
        self.setupUi(self)


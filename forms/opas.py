from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QMessageBox, QApplication
import paho.mqtt.client as mqtt
import paho.mqtt.publish as pub
import re
import time
import subprocess
import os
from ._mainWindow import Ui_MainWindow
from ._warning import Ui_Warning
from .dashboard import dashboard
from .help import about, userman
from .config import config
from .cdatastruct import opasData
from .settings import *

"""
class MQTTthread:
Meng-handle komunikasi dengan MQTT via thread terpisah
"""
class MQTTthread(QtCore.QObject, mqtt.Client):
    connected = QtCore.pyqtSignal()
    newMsg = QtCore.pyqtSignal(str)
    def __init__(self, topic, server=SERVER, port=1883, ttl=60):
        super(MQTTthread, self).__init__()
        self.t = topic
        self.s = server
        self.p = port
        self.l = ttl

    def run(self):
        self.on_connect = self.OnConnect
        self.on_message = self.OnMessage
        self.connect(self.s, self.p, self.l)
        self.loop_start()

    def stop(self):
        self.loop_stop()

    def OnConnect(self, client, userdata, flags, rc):
        print("[MQTT] Connected with result code "+str(rc))
        print("[MQTT] Subscribing to "+self.t)
        self.subscribe(self.t)
        self.connected.emit()

    def OnMessage(self, client, userdata, msg):
        pesan = str(msg.payload)
        self.newMsg.emit(pesan)
        
        

"""
Kelas actMonitor berisi QTimer untuk memantau aktivitas 
masing-masing station
"""
class actMonitor(QtCore.QObject):
    actChanged = QtCore.pyqtSignal(int, bool)
    def __init__(self):
        super(actMonitor, self).__init__()
        self.timer = list()
        self.ip = list()
        for i in range(N_STATION):
            self.timer.append(QtCore.QTimer())
            self.timer[i].setInterval(DEF_ACTMON_INTERVAL)
            self.timer[i].setSingleShot(True)
            self.ip.append("")
        self.running = True
        """ Bikin slot untuk masing-masing station """
        self.timer[0].timeout.connect(self.timeout1)
        self.timer[1].timeout.connect(self.timeout2)
        self.timer[2].timeout.connect(self.timeout3)
        self.timer[3].timeout.connect(self.timeout4)
        self.timer[4].timeout.connect(self.timeout5)
        self.timer[5].timeout.connect(self.timeout6)
        self.timer[6].timeout.connect(self.timeout7)
        self.timer[7].timeout.connect(self.timeout8)
        
    def run(self):
        """ Event loop ada di sini """
        while self.running:
            QtCore.QCoreApplication.processEvents()
            
    def stop(self):
        self.running = False    
        
    def setIP(self, idx, ip):
        """ idx adalah index station yang dimulai dari 1 """
        self.ip[int(idx)-1] = ip
        
    def incomingMsg(self, ip):
        """ main Event mgkin akan kirim info kalau ada station
            dgn IP tertentu mengirimkan MQTT
        """
        #print("[ACTM] Receiving data for IP", ip)
        if ip in self.ip:
            idx = self.ip.index(ip)
            sID = idx + 1 #karena index mulai dari 0
            self.actChanged.emit(sID, True) #lalu notifikasi dashboard
            self.timer[idx].start() #lalu jalankan timernya
        
    """ Kemudian implementasi slot-nya """
    def timeout1(self):
        self.actChanged.emit(1,False)
        
    def timeout2(self):
        self.actChanged.emit(2,False)
        
    def timeout3(self):
        self.actChanged.emit(3,False)
        
    def timeout4(self):
        self.actChanged.emit(4,False)
        
    def timeout5(self):
        self.actChanged.emit(5,False)
        
    def timeout6(self):
        self.actChanged.emit(6,False)
        
    def timeout7(self):
        self.actChanged.emit(7,False)
        
    def timeout8(self):
        self.actChanged.emit(8,False)
        

"""
Kelas warning hanya menampilkan warning kalau sudah mau tutup sore
"""
class warning(QtWidgets.QDialog, Ui_Warning):
    def __init__(self, parent=None):
        super(warning,self).__init__(parent)
        self.setupUi(self)



"""
-----------------------------------------
Bagian ini berhubungan dengan main Window
Online Public Address System (OPAS)
-----------------------------------------
"""
class opas(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(opas,self).__init__(parent)
        
        """ Cek dulu apakah darkice sudah dinyalakan """
        shell = subprocess.run(['ps','aux'],stdout=subprocess.PIPE)
        result = str(shell.stdout)
        if result.find('darkice') == -1:
            #QMessageBox.critical(self, 'ERROR', "Streaming Server 'darkice' belum dijalankan!", QMessageBox.Ok, QMessageBox.Ok)
            os.system("sudo /usr/bin/darkice &")
        else:
            print("[OPAS] Info: darkice sudah terdeteksi!")

        """
        Mulai dengan setting
        """
        self.settings = QSettings("PCR", "Online Public Address System")
        self.param = opasData(N_STATION)
        self.readSettings()

        """
        Bikin UI utama
        """
        self.setupUi(self)
        self.setCentralWidget(self.mdiArea)

        """
        Mekanisme MQTT
        """
        self.mqttc = MQTTthread(topic=T_STATION)
        self.mqttt = QtCore.QThread()
        self.mqttc.moveToThread(self.mqttt)
        self.mqttt.started.connect(self.mqttc.run)
        self.mqttt.finished.connect(self.mqttt.deleteLater)
        self.mqttc.newMsg.connect(self.newMsg)

        self.mqttt.start()

        """
        Bikin UI dashboard
        """
        self.dash = dashboard(self.param, self)
        self.subDash = QtWidgets.QMdiSubWindow(self.mdiArea)
        self.subDash.setWidget(self.dash)
        w = self.dash.width(); h = self.dash.height()
        self.subDash.setFixedSize(w+5,h+25)
        self.mdiArea.addSubWindow(self.subDash)

        """
        Lalu UI about
        """
        self.about = about(self)
        self.subAbout = QtWidgets.QMdiSubWindow(self.mdiArea)
        self.subAbout.setWidget(self.about)
        self.mdiArea.addSubWindow(self.subAbout)
        w = self.about.width(); h = self.about.height()
        self.subAbout.setFixedSize(w+5,h+25)
        self.subAbout.hide()

        """
        Lalu UI User Manual
        """
        self.user = userman(self)
        self.subUser = QtWidgets.QMdiSubWindow(self.mdiArea)
        self.subUser.setWidget(self.user)
        self.mdiArea.addSubWindow(self.subUser)
        w = self.user.width(); h = self.user.height()
        self.subUser.setFixedSize(w+5,h+25)
        self.subUser.hide()

        """
        Lalu UI konfigurasi
        """
        self.config = config(self.param, self)
        self.subConfig = QtWidgets.QMdiSubWindow(self.mdiArea)
        self.subConfig.setWidget(self.config)
        self.mdiArea.addSubWindow(self.subConfig)
        w = self.config.width(); h = self.config.height()
        self.subConfig.setFixedSize(w+5,h+25)
        self.subConfig.hide()
        
        """ Terkait warning 15 menit sebelum jam 5 sore """
        self.warningActive = False

        """
        Tambahan
        """
        self.opStatus = QtWidgets.QLabel("Operator: Lab Radio PCU")
        self.sepStatus = QtWidgets.QLabel("|")
        self.netStatus = QtWidgets.QLabel("MQTT Network connected") #Karena MQTT server juga di komputer yang sama
        self.statusBar().addWidget(self.netStatus)
        self.statusBar().addWidget(self.sepStatus)
        self.statusBar().addWidget(self.opStatus)

        """
        Timer untuk menampilkan jam di Toolbar
        """
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getTime)
        self.timer.setInterval(1000)
        self.timer.start()
        
        """
        Lalu activity monitor
        """
        self.actMon = actMonitor()
        self.actMonT = QtCore.QThread()
        self.actMon.moveToThread(self.actMonT)
        self.actMonT.started.connect(self.actMon.run)
        self.actMonT.finished.connect(self.actMonT.deleteLater)
        self.actMon.actChanged.connect(self.dash.actChanged)

        self.actMonT.start()
               
        """
        ide: semua di-hide sampai login berhasil
        """
        self.signalslot()

        """
        finally: tampilkan
        """
        w = self.dash.width()
        h = self.dash.height()
        desktop = QApplication.desktop()
        screct = desktop.screenGeometry()
        sw = screct.width()
        wh = screct.height()
        self.setGeometry(sw/2-w/2,wh/2-h/2-60,w,h)
        self.show()

    def closeEvent(self, event):
        self.writeSettings()
        event.accept()

    def signalslot(self):
        """
        deklarasi mekanisme signal-slot"
        """
        self.action_Monitor.triggered.connect(self.showDashboard)
        self.action_About.triggered.connect(self.showAbout)
        self.action_Penggunaan.triggered.connect(self.showUserman)
        self.action_Keluar.triggered.connect(self.finish)
        self.action_Seting.triggered.connect(self.showConfig)
        self.pbSetting.clicked.connect(self.showConfig)
        self.pbMon.clicked.connect(self.showDashboard)
        self.pbHelp.clicked.connect(self.showUserman)
        self.dash.volChanged.connect(self.updateVol)
        self.config.finish.connect(self.updateInfo)
        self.about.finished.connect(self.aboutFinished)
        self.user.finished.connect(self.manualFinished)

    def aboutFinished(self):
        self.about.close()
        self.subAbout.hide()

    def manualFinished(self):
        self.user.close()
        self.subUser.hide()
        
    def updateInfo(self, kode, param):
        if kode==2:
            self.param.info = param.info
            self.dash.updateInfo(param)
        self.config.close()
        self.subConfig.hide()
        
    def updateVol(self, sID, val):
        self.param.vol[sID-1] = val;

    def readSettings(self):
        """
        Baca pertama kali saat program baru dijalankan
        """
        for i in range(1,N_STATION+1):
            vol = f"vol{i}"
            self.param.vol[i-1] = self.settings.value(vol,type=int)
            info = f"info{i}"
            self.param.info[i-1] = self.settings.value(info,type=str)
            ip = f"ip{i}"
            self.param.ip[i-1] = self.settings.value(ip,type=str)
            muted = f"muted{i}"
            self.param.muted[i-1] = self.settings.value(muted,type=bool)

    def writeSettings(self):
        """
        Sebelum program berakhir, simpan dulu parameternya
        """
        for i in range(1,N_STATION+1):
            vol = f"vol{i}"
            self.settings.setValue(vol,self.param.vol[i-1])
            info = f"info{i}"
            self.settings.setValue(info,self.param.info[i-1])
            ip = f"ip{i}"
            self.settings.setValue(ip,self.param.ip[i-1])
            muted = f"muted{i}"
            self.settings.setValue(muted,self.param.muted[i-1])

    """
    For Handling MQTT
    """       
    def newMsg(self,msg):
        info = f"[MQTT] Receiving: {msg}"
        self.dash.dbgConsole.appendPlainText(info)
        print(info)
        #Contoh data dari  raspberry: 192.168.1.10/21,station8,[100%]
        payload = msg.replace("b'","").replace("'","").replace("[","").replace("%]","")
        strList = payload.split(",")
        if len(strList)==3: #kita butuh 3 data dari station
            fiqn = strList[0].split("/")
            ip = fiqn[0]
            hostname = strList[1]
            sID = re.sub("[^0-9]", "", hostname)
            vol = strList[2]
            msg = f"Hostname {hostname} has IP {ip}"
            """ Then visualize the volume"""
            self.dash.volMon(int(sID),int(vol))
            self.dash.setIP(int(sID),ip)
            
            """ TODO: 
                - perlu didata dulu peta sID dengan ip 
                - dan send initial volume """
            self.param.map(sID, ip)
            self.dash.sendVol(sID)
            
            
            """ Lalu update activity Monitor """
            self.actMon.setIP(sID, ip) #buat reset activity monitor timer
            self.actMon.incomingMsg(ip)
            

    def on_connect(self, client, userdata, flags, rc):
        msg = "[MQTT] Connected with result code "+str(rc)
        self.mqttc.subscribe("opas/station")
        print(msg)
        self.dash.dbgConsole.appendPlainText(msg)
        self.dash.dbgConsole.appendPlainText("[MQTT] Subscribing to opas/station")

    def on_message(self, client, userdata, msg):
        pesan = str(msg.payload)
        msg = "[INFO] Msg: "+msg.topic+" "+pesan
        self.dash.dbgConsole.appendPlainText(msg)
        print(msg)

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
        
        """ Terkait warning untuk shutdown raspberry pi """
        if j==16 and m==45 and d==00:
            if self.warningActive is False:
                self.warningActive = True
                warn = warning()
                warn.exec()
                self.warningActive = False
            
    def showDashboard(self):
        self.dash.show()

    def showConfig(self):
        self.config.show()

    def showAbout(self):
        self.about.show()
    
    def showUserman(self):
        self.user.show()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F12:
            self.showAbout()
        elif event.key() == QtCore.Qt.Key_F1:
            self.showUserman()
        elif event.key() == QtCore.Qt.Key_F2:
            self.showConfig()
        elif event.key() == QtCore.Qt.Key_F3:
            self.showDashboard()



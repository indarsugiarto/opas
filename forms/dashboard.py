from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QMessageBox
import subprocess
import paho.mqtt.publish as pub
from ._dashboard import Ui_MonitorForm
from ._reset import Ui_Reset
from .cdatastruct import opasData
from .settings import *

"""
Kelas reset untuk menampilkan widget reset
"""
class reset(QtWidgets.QDialog, Ui_Reset):
    def __init__(self, parent=None):
        super(reset,self).__init__(parent)
        self.setupUi(self)
        self.signalslot()
       
    def signalslot(self):
        self.pbReset.clicked.connect(self.Reset)
        self.pbShutdown.clicked.connect(self.Shutdown)
        
    def Reset(self):
        """ 
        Jika tombol Cancel ditekan, tidak perlu melakukan apa-apa
        """
        self.done(RESET_RESET_CODE)

    def Shutdown(self):
        """ 
        Jika tombol Cancel ditekan, tidak perlu melakukan apa-apa
        """
        self.done(RESET_SHUTDOWN_CODE)



"""
------------------------------------------------
Bagian ini berhubungan dengan tampilan dashboard
------------------------------------------------
"""
class dashboard(QtWidgets.QWidget, Ui_MonitorForm):
    volChanged = QtCore.pyqtSignal(int,int)
    def __init__(self, param, parent=None):
        super(dashboard,self).__init__(parent)
        self.ui = Ui_MonitorForm()
        self.setupUi(self)
        """
        Lalu sesuaikan dengan parameter yang ada
        """
        self.vol1.setValue(param.vol[0])
        self.vol2.setValue(param.vol[1])
        self.vol3.setValue(param.vol[2])
        self.vol4.setValue(param.vol[3])
        self.vol5.setValue(param.vol[4])
        self.vol6.setValue(param.vol[5])
        self.vol7.setValue(param.vol[6])
        self.vol8.setValue(param.vol[7])
        self.info1.setPlainText(param.info[0])
        self.info2.setPlainText(param.info[1])
        self.info3.setPlainText(param.info[2])
        self.info4.setPlainText(param.info[3])
        self.info5.setPlainText(param.info[4])
        self.info6.setPlainText(param.info[5])
        self.info7.setPlainText(param.info[6])
        self.info8.setPlainText(param.info[7])
        self.ip1.setText(param.ip[0])
        self.ip2.setText(param.ip[1])
        self.ip3.setText(param.ip[2])
        self.ip4.setText(param.ip[3])
        self.ip5.setText(param.ip[4])
        self.ip6.setText(param.ip[5])
        self.ip7.setText(param.ip[6])
        self.ip8.setText(param.ip[7])
        if param.muted[0]:
            self.mute1.setChecked(True)
        else:
            self.mute1.setChecked(False)
        if param.muted[1]:
            self.mute2.setChecked(True)
        else:
            self.mute2.setChecked(False)
        if param.muted[2]:
            self.mute3.setChecked(True)
        else:
            self.mute3.setChecked(False)
        if param.muted[3]:
            self.mute4.setChecked(True)
        else:
            self.mute4.setChecked(False)
        if param.muted[4]:
            self.mute5.setChecked(True)
        else:
            self.mute5.setChecked(False)
        if param.muted[5]:
            self.mute6.setChecked(True)
        else:
            self.mute6.setChecked(False)
        if param.muted[6]:
            self.mute7.setChecked(True)
        else:
            self.mute7.setChecked(False)
        if param.muted[7]:
            self.mute8.setChecked(True)
        else:
            self.mute8.setChecked(False)
        
        """ Simpan history parameter, khususnya untuk mute action """
        self.param = param
        
        """ Lalu konfigurasi signal-slot """        
        self.signalslot()

    def signalslot(self):
        """ Jika tombol reset ditekan """
        self.pbReset1.clicked.connect(self.Reset1)
        self.pbReset2.clicked.connect(self.Reset2)
        self.pbReset3.clicked.connect(self.Reset3)
        self.pbReset4.clicked.connect(self.Reset4)
        self.pbReset5.clicked.connect(self.Reset5)
        self.pbReset6.clicked.connect(self.Reset6)
        self.pbReset7.clicked.connect(self.Reset7)
        self.pbReset8.clicked.connect(self.Reset8)

        """ Berhubungan dengan slider """
        self.vol1.valueChanged.connect(self.updateVol1Txt)
        self.vol2.valueChanged.connect(self.updateVol2Txt)
        self.vol3.valueChanged.connect(self.updateVol3Txt)
        self.vol4.valueChanged.connect(self.updateVol4Txt)
        self.vol5.valueChanged.connect(self.updateVol5Txt)
        self.vol6.valueChanged.connect(self.updateVol6Txt)
        self.vol7.valueChanged.connect(self.updateVol7Txt)
        self.vol8.valueChanged.connect(self.updateVol8Txt)
        self.vol1.sliderReleased.connect(self.updateVol1)
        self.vol2.sliderReleased.connect(self.updateVol2)
        self.vol3.sliderReleased.connect(self.updateVol3)
        self.vol4.sliderReleased.connect(self.updateVol4)
        self.vol5.sliderReleased.connect(self.updateVol5)
        self.vol6.sliderReleased.connect(self.updateVol6)
        self.vol7.sliderReleased.connect(self.updateVol7)
        self.vol8.sliderReleased.connect(self.updateVol8)
        
        """ Berhubungan dengan checkbox mute """
        self.mute1.stateChanged.connect(self.mute1Changed)
        self.mute2.stateChanged.connect(self.mute2Changed)
        self.mute3.stateChanged.connect(self.mute3Changed)
        self.mute4.stateChanged.connect(self.mute4Changed)
        self.mute5.stateChanged.connect(self.mute5Changed)
        self.mute6.stateChanged.connect(self.mute6Changed)
        self.mute7.stateChanged.connect(self.mute7Changed)
        self.mute8.stateChanged.connect(self.mute8Changed)
                                        
    def tampilkan(self):
        self.show()
        
    def setIP(self, sID, ip):
        if sID==1:
            self.ip1.setText(ip)
        elif sID==2:
            self.ip2.setText(ip)
        elif sID==3:
            self.ip3.setText(ip)
        elif sID==4:
            self.ip4.setText(ip)
        elif sID==5:
            self.ip5.setText(ip)
        elif sID==6:
            self.ip6.setText(ip)
        elif sID==7:
            self.ip7.setText(ip)
        elif sID==8:
            self.ip8.setText(ip)
        
    def doReset(self,sID):
        rst = reset()
        hasil = rst.exec()
        if hasil != 0:
           t = f"{T_STATION}/{sID}/cmd"
           if hasil == RESET_RESET_CODE:
               pl = RESET_CMD
           else:
               pl = HALT_CMD
           pub.single(t,payload=pl,hostname=SERVER)
           print(f"[MQTT] Reset with command={hasil} has been sent to station-{sID} with topic {t}")

    def Reset1(self):
        self.doReset(1)
                
    def Reset2(self):
        self.doReset(2)
           
    def Reset3(self):
        self.doReset(3)

    def Reset4(self):
        self.doReset(4)

    def Reset5(self):
        self.doReset(5)

    def Reset6(self):
        self.doReset(6)

    def Reset7(self):
        self.doReset(7)

    def Reset8(self):
        self.doReset(8)

    def updateInfo(self, param):
        self.info1.setPlainText(param.info[0])
        self.info2.setPlainText(param.info[1])
        self.info3.setPlainText(param.info[2])
        self.info4.setPlainText(param.info[3])
        self.info5.setPlainText(param.info[4])
        self.info6.setPlainText(param.info[5])
        self.info7.setPlainText(param.info[6])
        self.info8.setPlainText(param.info[7])
        
    def updateVol1Txt(self,val):
        self.lvol1.setText(f"Volume: {val}%")

    def updateVol2Txt(self,val):
        self.lvol2.setText(f"Volume: {val}%")

    def updateVol3Txt(self,val):
        self.lvol3.setText(f"Volume: {val}%")

    def updateVol4Txt(self,val):
        self.lvol4.setText(f"Volume: {val}%")

    def updateVol5Txt(self,val):
        self.lvol5.setText(f"Volume: {val}%")

    def updateVol6Txt(self,val):
        self.lvol6.setText(f"Volume: {val}%")

    def updateVol7Txt(self,val):
        self.lvol7.setText(f"Volume: {val}%")

    def updateVol8Txt(self,val):
        self.lvol8.setText(f"Volume: {val}%")

    def updateVol1(self):
        val = self.vol1.value()
        t = T_STATION+"/1/vol"
        print(f"[MQTT] Kirim ke {SERVER} dengan topik {t}")
        pub.single(t,payload=str(val),hostname=SERVER)
        """ Lalu kirim ke main GUI untuk disimpan """
        self.volChanged.emit(1,val)
        """ Lalu simpan juga untuk history local buat mute-undo """
        self.param.vol[0] = val
        
    def updateVol2(self):
        val = self.vol2.value()
        t = T_STATION+"/2/vol"
        print(f"[MQTT] Kirim ke {SERVER} dengan topik {t}")
        pub.single(t,payload=str(val),hostname=SERVER)
        """ Lalu kirim ke main GUI untuk disimpan """
        self.volChanged.emit(2,val)
        """ Lalu simpan juga untuk history local buat mute-undo """
        self.param.vol[1] = val
        
    def updateVol3(self):
        val = self.vol3.value()
        t = T_STATION+"/3/vol"
        print(f"[MQTT] Kirim ke {SERVER} dengan topik {t}")
        pub.single(t,payload=str(val),hostname=SERVER)
        """ Lalu kirim ke main GUI untuk disimpan """
        self.volChanged.emit(3,val)
        """ Lalu simpan juga untuk history local buat mute-undo """
        self.param.vol[2] = val
        
    def updateVol4(self):
        val = self.vol4.value()
        t = T_STATION+"/4/vol"
        print(f"[MQTT] Kirim ke {SERVER} dengan topik {t}")
        pub.single(t,payload=str(val),hostname=SERVER)
        """ Lalu kirim ke main GUI untuk disimpan """
        self.volChanged.emit(4,val)
        """ Lalu simpan juga untuk history local buat mute-undo """
        self.param.vol[3] = val
        
    def updateVol5(self):
        val = self.vol5.value()
        t = T_STATION+"/5/vol"
        print(f"[MQTT] Kirim ke {SERVER} dengan topik {t}")
        pub.single(t,payload=str(val),hostname=SERVER)
        """ Lalu kirim ke main GUI untuk disimpan """
        self.volChanged.emit(5,val)
        """ Lalu simpan juga untuk history local buat mute-undo """
        self.param.vol[4] = val
        
    def updateVol6(self):
        val = self.vol6.value()
        t = T_STATION+"/6/vol"
        print(f"[MQTT] Kirim ke {SERVER} dengan topik {t}")
        pub.single(t,payload=str(val),hostname=SERVER)
        """ Lalu kirim ke main GUI untuk disimpan """
        self.volChanged.emit(6,val)
        """ Lalu simpan juga untuk history local buat mute-undo """
        self.param.vol[5] = val
        
    def updateVol7(self):
        val = self.vol7.value()
        t = T_STATION+"/7/vol"
        print(f"[MQTT] Kirim ke {SERVER} dengan topik {t}")
        pub.single(t,payload=str(val),hostname=SERVER)
        """ Lalu kirim ke main GUI untuk disimpan """
        self.volChanged.emit(7,val)
        """ Lalu simpan juga untuk history local buat mute-undo """
        self.param.vol[6] = val
        
    def updateVol8(self):
        val = self.vol8.value()
        t = T_STATION+"/8/vol"
        print(f"[MQTT] Kirim ke {SERVER} dengan topik {t}")
        pub.single(t,payload=str(val),hostname=SERVER)
        """ Lalu kirim ke main GUI untuk disimpan """
        self.volChanged.emit(8,val)
        """ Lalu simpan juga untuk history local buat mute-undo """
        self.param.vol[7] = val

    def sendVol(self, sID):
        if sID==1:
            self.updateVol1()
        elif sID==2:
            self.updateVol2()
        elif sID==3:
            self.updateVol3()
        elif sID==4:
            self.updateVol4()
        elif sID==5:
            self.updateVol5()
        elif sID==6:
            self.updateVol6()
        elif sID==7:
            self.updateVol7()
        elif sID==8:
            self.updateVol8()

    def volMon(self, sID, vol):
        """ Digunakan untuk monitoring volume real raspberry pi """
        msg = f"[MQTT] Receiving info for sID = {sID}, vol = {vol}"
        self.dbgConsole.appendPlainText(msg)
        if sID==1:
            self.volBar1.setValue(vol)
        elif sID==2:
            self.volBar2.setValue(vol)
        elif sID==3:
            self.volBar3.setValue(vol)
        elif sID==4:
            self.volBar4.setValue(vol)
        elif sID==5:
            self.volBar5.setValue(vol)
        elif sID==6:
            self.volBar6.setValue(vol)
        elif sID==7:
            self.volBar7.setValue(vol)
        elif sID==8:
            self.volBar8.setValue(vol)
        else:
            self.dbgConsole.appendPlainText(f"[ERROR] Nomor station {sID} tidak dikenali!")

    def actChanged(self, sID, status):
        if status:
            if sID==1:
                self.status1.setText("Online")
                self.status1.setStyleSheet("color: blue;  background-color: white")
            elif sID==2:
                self.status2.setText("Online")
                self.status2.setStyleSheet("color: blue;  background-color: white")
            elif sID==3:
                self.status3.setText("Online")
                self.status3.setStyleSheet("color: blue;  background-color: white")
            elif sID==4:
                self.status4.setText("Online")
                self.status4.setStyleSheet("color: blue;  background-color: white")
            elif sID==5:
                self.status5.setText("Online")
                self.status5.setStyleSheet("color: blue;  background-color: white")
            elif sID==6:
                self.status6.setText("Online")
                self.status6.setStyleSheet("color: blue;  background-color: white")
            elif sID==7:
                self.status7.setText("Online")
                self.status7.setStyleSheet("color: blue;  background-color: white")
            elif sID==8:
                self.status8.setText("Online")
                self.status8.setStyleSheet("color: blue;  background-color: white")
            else:
                self.dbgConsole.appendPlainText("[ERROR] Nomor station tidak dikenali untuk actMon")
        else:
            if sID==1:
                self.status1.setText("Offline")
                self.status1.setStyleSheet("color: red;  background-color: white")
                self.volMon(1,0)
            elif sID==2:
                self.status2.setText("Offline")
                self.status2.setStyleSheet("color: red;  background-color: white")
                self.volMon(2,0)
            elif sID==3:
                self.status3.setText("Offline")
                self.status3.setStyleSheet("color: red;  background-color: white")
                self.volMon(3,0)
            elif sID==4:
                self.status4.setText("Offline")
                self.status4.setStyleSheet("color: red;  background-color: white")
                self.volMon(4,0)
            elif sID==5:
                self.status5.setText("Offline")
                self.status5.setStyleSheet("color: red;  background-color: white")
                self.volMon(5,0)
            elif sID==6:
                self.status6.setText("Offline")
                self.status6.setStyleSheet("color: red;  background-color: white")
                self.volMon(6,0)
            elif sID==7:
                self.status7.setText("Offline")
                self.status7.setStyleSheet("color: red;  background-color: white")
                self.volMon(7,0)
            elif sID==8:
                self.status8.setText("Offline")
                self.status8.setStyleSheet("color: red;  background-color: white")
                self.volMon(8,0)
            else:
                self.dbgConsole.appendPlainText("[ERROR] Nomor station tidak dikenali untuk actMon")

    def muteVol(self, sID):
        """ Ganti label volume """
        v = "Volume: 0%"
        if sID==1:
            self.lvol1.setText(v)
            self.vol1.setEnabled(False)
        elif sID==2:
            self.lvol2.setText(v)
            self.vol2.setEnabled(False)
        elif sID==3:
            self.lvol3.setText(v)
            self.vol3.setEnabled(False)
        elif sID==4:
            self.lvol4.setText(v)
            self.vol4.setEnabled(False)
        elif sID==5:
            self.lvol5.setText(v)
            self.vol5.setEnabled(False)
        elif sID==6:
            self.lvol6.setText(v)
            self.vol6.setEnabled(False)
        elif sID==7:
            self.lvol7.setText(v)
            self.vol7.setEnabled(False)
        elif sID==8:
            self.lvol8.setText(v)
            self.vol8.setEnabled(False)
        """ Lalu kirim sebagai MQTT """
        t = T_STATION+f"/{sID}/vol"
        pub.single(t,payload=0,hostname=SERVER)        
        
    def unMuteVol(self, sID):
        """ Ganti label volume """
        oldv = self.param.vol[sID-1]
        v = f"Volume: {oldv}%"
        if sID==1:
            self.lvol1.setText(v)
            self.vol1.setEnabled(True)
        elif sID==2:
            self.lvol2.setText(v)
            self.vol2.setEnabled(True)
        elif sID==3:
            self.lvol3.setText(v)
            self.vol3.setEnabled(True)
        elif sID==4:
            self.lvol4.setText(v)
            self.vol4.setEnabled(True)
        elif sID==5:
            self.lvol5.setText(v)
            self.vol5.setEnabled(True)
        elif sID==6:
            self.lvol6.setText(v)
            self.vol6.setEnabled(True)
        elif sID==7:
            self.lvol7.setText(v)
            self.vol7.setEnabled(True)
        elif sID==8:
            self.lvol8.setText(v)
            self.vol8.setEnabled(True)
        """ Lalu kirim sebagai MQTT """
        t = T_STATION+f"/{sID}/vol"
        pub.single(t,payload=oldv,hostname=SERVER)        

    def mute1Changed(self, state):
        if state==0: #0 = unchecked
            self.unMuteVol(1)
        else:
            self.muteVol(1)

    def mute2Changed(self, state):
        if state==0: #0 = unchecked
            self.unMuteVol(2)
        else:
            self.muteVol(2)

    def mute3Changed(self, state):
        if state==0: #0 = unchecked
            self.unMuteVol(3)
        else:
            self.muteVol(3)

    def mute4Changed(self, state):
        if state==0: #0 = unchecked
            self.unMuteVol(4)
        else:
            self.muteVol(4)

    def mute5Changed(self, state):
        if state==0: #0 = unchecked
            self.unMuteVol(5)
        else:
            self.muteVol(5)

    def mute6Changed(self, state):
        if state==0: #0 = unchecked
            self.unMuteVol(6)
        else:
            self.muteVol(6)

    def mute7Changed(self, state):
        if state==0: #0 = unchecked
            self.unMuteVol(7)
        else:
            self.muteVol(7)

    def mute8Changed(self, state):
        if state==0: #0 = unchecked
            self.unMuteVol(8)
        else:
            self.muteVol(8)




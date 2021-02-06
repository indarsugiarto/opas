from PyQt5 import QtWidgets,QtCore,QtGui
from ._config import Ui_Config
from .cdatastruct import opasData
import subprocess


"""
Kelas yang mengatur tampilan konfigurasi
"""
class config(QtWidgets.QWidget, Ui_Config):
    finish = QtCore.pyqtSignal(int, opasData)
    def __init__(self, param, parent=None):
        super(config,self).__init__(parent)
        self.setupUi(self)
        """
        Lalu inisialisasi dengan info awal
        """
        self.param = param
        self.s1Loc.setPlainText(param.info[0])
        self.s2Loc.setPlainText(param.info[1])
        self.s3Loc.setPlainText(param.info[2])
        self.s4Loc.setPlainText(param.info[3])
        self.s5Loc.setPlainText(param.info[4])
        self.s6Loc.setPlainText(param.info[5])
        self.s7Loc.setPlainText(param.info[6])
        self.s8Loc.setPlainText(param.info[7])
        self.signalslot()
        
    def cancel(self):
        self.finish.emit(1,self.param)
            
    def save(self):
        self.param.info[0] = self.s1Loc.toPlainText()
        self.param.info[1] = self.s2Loc.toPlainText()
        self.param.info[2] = self.s3Loc.toPlainText()
        self.param.info[3] = self.s4Loc.toPlainText()
        self.param.info[4] = self.s5Loc.toPlainText()
        self.param.info[5] = self.s6Loc.toPlainText()
        self.param.info[6] = self.s7Loc.toPlainText()
        self.param.info[7] = self.s8Loc.toPlainText()
        self.finish.emit(2,self.param)
        
    def signalslot(self):
        self.pbCancel.clicked.connect(self.cancel)
        self.pbSave.clicked.connect(self.save)


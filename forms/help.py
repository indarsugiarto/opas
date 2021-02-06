from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QMessageBox
from ._about import Ui_AboutForm
from ._userman import Ui_userman
import subprocess

class about(QtWidgets.QWidget, Ui_AboutForm):
    finished = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(about,self).__init__(parent)
        self.setupUi(self)
        self.pbClose.clicked.connect(self.finish)
    def finish(self):
        self.finished.emit()

class userman(QtWidgets.QWidget, Ui_userman):
    finished = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(userman,self).__init__(parent)
        self.setupUi(self)
        self.pbClose.clicked.connect(self.finish)
    def finish(self):
        self.finished.emit()


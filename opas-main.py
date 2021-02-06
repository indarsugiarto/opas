#!/usr/bin/python3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from forms import opas
import subprocess


if __name__=="__main__":

    """ Cek dulu apakah opas sudah running """
    shell = subprocess.run(['ps','aux'],stdout=subprocess.PIPE)
    result = str(shell.stdout)
    num = result.count("opas-main.py")
    if num > 1:
        print("[OPAS] Sudah dijalankan!")
        sys.exit(-1)
    app = QtWidgets.QApplication(sys.argv)
    mainUI = opas()
    sys.exit(app.exec_())

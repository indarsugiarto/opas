import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from forms import opas

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainUI = opas()
    sys.exit(app.exec_())

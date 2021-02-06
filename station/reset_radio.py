#! /usr/bin/python3

from PyQt5 import QtCore
import time
import os
import sys
import subprocess
import re

import paho.mqtt.client as mqtt

shell = subprocess.run(['hostname'], stdout=subprocess.PIPE)
result = str(shell.stdout)
sID = re.sub("[^0-9]", "", result)

SERVER="10.52.129.2"
TOPIC=f"opas/station/{sID}/cmd"

class mainCtrl(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    running = False
    def __init__(self):
        super(mainCtrl, self).__init__()
        
        print("[INFO] Starting reset_radio.py")
        self.mqttc = mqtt.Client()
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_message = self.on_message
        self.mqttc.connect(SERVER, 1883, 60)
        self.mqttc.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("[INFO] reset_radio.py connected with result code "+str(rc))
        print("[INFO] reset_radio.py subscribing to "+TOPIC)
        self.mqttc.subscribe(TOPIC)

    def on_message(self, client, userdata, msg):
        pesan = str(msg.payload)
        print("[INFO] reset_radio.py Msg: "+msg.topic+" "+pesan)
        if "EXIT" in pesan.upper():
            self.mqttc.loop_stop()
            QtCore.QCoreApplication.instance().quit()
        elif "REBOOT" in pesan.upper() or "RESTART" in pesan.upper():
            print("[INFO] reset_radio.py rebooting...")
            os.system("sudo reboot")
        elif "SHUTDOWN" in pesan.upper() or "POWEROFF" in pesan.upper():
            print("[INFO] reset_radio.py shutting down...")
            os.system("sudo poweroff")
        else:
            vol = pesan.replace("b'","").replace("'","")
            cmd = "amixer sset 'Master' {}%".format(vol)
            print("[INFO] reset_radio.py gets cmd = ",cmd)
            os.system(cmd)

if __name__ == "__main__":
    app = QtCore.QCoreApplication(sys.argv)
    sub = mainCtrl()
    sys.exit(app.exec_())

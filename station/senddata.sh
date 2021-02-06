#!/bin/bash
LOGFILE=/var/log/radio.log
while true
do
  ip=`ip -4 address show dev eth0 | grep inet | sed 's/\// /' | awk '{print $2}'`
  host=`hostname`
  vol=`amixer sget Master | grep % | grep Left | awk '{print $5}'`
  msg=$ip,$host,$vol
  echo "Kirim data: " $msg >> $LOGFILE
  mosquitto_pub -h "10.52.129.2" -t "opas/station" -m $msg
  sleep 5
done

import sys
import rrdtool

def createRRD(computerName):
  computerName = computerName + ".rrd"
  ret = rrdtool.create(computerName, "--step", "300", "--start", '0',
   "DS:la:COUNTER:600:U:U",
   "RRA:MAX:0.5:1:288")

  if ret:
   print rrdtool.error()
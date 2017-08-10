import sys
sys.path.append('..')

from Network import Pinger

myPinger = Pinger.Pinger("92.168.0.")

myPinger.scanIp()
myPinger.printScannedIpAddresses()



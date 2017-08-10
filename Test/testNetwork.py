import sys
sys.path.append('..')

from Network import Pinger


def testPinger():
    myPinger = Pinger.Pinger("92.168.0.")
    myPinger.scanIp()
    myPinger.printScannedIpAddresses()

if __name__ == "__main__":
    testPinger()

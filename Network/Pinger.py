import multiprocessing
import subprocess
import os

    

class Pinger(object):
    """
    Class to Ping all IP addresses on a given subnet, but quickly.
    Was developed for a basic server operation for a hackathon,
    but the speed is useful.
    Takes in a base IpString, e.g. '192.168.1' or '130.0.1.'
    and pings every IP between '192.168.1.0' and '192.168.1.255'
    TODO: Have the ping operation be more configurable
    """
    def __init__(self, baseIpString):
        """
        Constructor for Pinger class. Takes base IP string
        """
        if not self._validateInit(baseIpString):
            print("Error in input value of: " + baseIpString)
            exit()
        if baseIpString.endswith('.'):
            baseIpString = baseIpString[:-1]
        self._ipString = baseIpString + '.{0}'
        self._activeIpAddresses = []

    def _validateInit(self, baseIpString):
        """
        Simple validator for the Pinger input.
        Check that the IP address number are within 0 and 255.
        """
        vals = baseIpString.split(".")
        vals = [int(val) for val in vals if val != ""]
        return all((val >= 0 and val <= 255) for val in vals)

    def _pinger(self, job, results):
        """
        The process that the scanner will be using for its operation
        """
        with open(os.devnull, 'w') as DEVNULL:
            while True:
                ip = job.get()
                if ip is None:
                    break
                try:
                    subprocess.check_call(['ping','-c1',ip],
                        stdout=DEVNULL)
                    results.put(ip)
                except:
                    pass
    def scanIp(self):
        """
        The primary operation of this class. Scan 256 IP addresses, but quickly
        Takes no arguments and operates off of value given in constructor
        """
        pool_size=255
        jobs = multiprocessing.Queue()
        results = multiprocessing.Queue()
        pool = [multiprocessing.Process(target=self._pinger,args=(jobs,results))
            for i in range(pool_size)]
        for p in pool:
            p.start()
        for i in range(1, pool_size):
            jobs.put(self._ipString.format(i))
        for p in pool:
            jobs.put(None)
        while not results.empty():
            activeIpAddresses.append(results.get())

    def printScannedIpAddresses(self):
        print(*self._activeIpAddresses, sep='\n')

    def returnScannedIpAddresses(self):
        return self._activeIpAddresses


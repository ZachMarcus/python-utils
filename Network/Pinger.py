import multiprocessing
import subprocess
import os
import requests
from bs4 import BeautifulSoup


    

class Pinger(object):
    # TODO: check that the ip base is valid
    def __init__(self, baseIpString):
        if baseIpString.endswith('.'):
            baseIpString = baseIpString[:-1]
        self._ipString = baseIpString + '.{0}'
        self._activeIpAddresses = []

    def _pinger(self, job, results):
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
"""
def pinger( job_q, results_q ):
    DEVNULL = open(os.devnull,'w')
    while True:
        ip = job_q.get()
        if ip is None: break

        try:
            subprocess.check_call(['ping','-c1',ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass

def getAllPrintersToFile():
    pool_size = 255

    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [ multiprocessing.Process(target=pinger, args=(jobs,results))
             for i in range(pool_size) ]

    for p in pool:
        p.start()

    for i in range(1,255):
        jobs.put('10.30.10.{0}'.format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()


    ipAddresses = []

    while not results.empty():
        ip = results.get()
        #print(ip)
        ipAddresses.append(ip)"""


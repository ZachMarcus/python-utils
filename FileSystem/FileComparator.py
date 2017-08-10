import os
import hashlib


class FileComparator(object):
    def __init__(self, filePath1, filePath2):
        if os.path.isfile(filePath1) and os.path.isfile(filePath2):
            self._filePath1 = filePath1
            self._filePath2 = filePath2
        else:
            print("Implement error handling")
            exit()
        self._hasReadInFiles = False
#        self._fileList1 = self._readInFileToList(filePath1)
#        self._fileList2 = self._readInFileToList(filePath2)

    def _readInFileToList(self, filePath):
        destinationList = []
        with open(filePath, "r") as f:
            for line in f:
                destinationList.append(line.replace("\n","").replace("\r",""))
        return destinationList

    def readInFiles(self):
        self._hasReadInFiles = True
        self._fileList1 = self._readInFileToList(self._filePath1)
        self._fileList2 = self._readInFileToList(self._filePath2)

    def findMatchingLinesAnyOrder(self, shouldPrint=False):
        if not self._hasReadInFiles:
            self.readInFiles()
        setOf2 = set(self._fileList2)
        ret = [line for line in self._fileList1 if line in setOf2]
        if shouldPrint:
            print("Matching lines between " + self._filePath1 + " and " + self._filePath2 + ":")
            removingBlanks = [line for line in ret if line != ""]
            print(*removingBlanks, sep='\n')
        return ret


    """
    Valid Hash strings:
    sha1
    sha224
    sha256
    sha384
    sha512
    blake2b
    blake2s
    md5     --    This one is usually guaranteed,
                  except on a rare FIPS compliant Python build
    """
    def compareFileHashes(self, stringOfHash="sha1", shouldPrint=True):
        hashes = []
        for filename in [self._filePath1, self._filePath2]:
            hasher = hashlib.new(stringOfHash)
            print(filename)
            with open(filename, 'rb') as f:
                buf = f.read()
                hasher.update(buf)
                hashes.append(hasher.hexdigest())
                print(hasher.hexdigest())
        ret = hashes[0] == hashes[1]
        if shouldPrint:
            print("Are hashes the same: " + str(ret))
        return ret





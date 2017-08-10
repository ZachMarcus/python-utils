import os
import hashlib



class FileComparator(object):
    """
    Class to read in two files and compare them
    Can compare for matching lines or matching hashes
    """
    def __init__(self, filePath1, filePath2):
        """
        Constructor for FileComparator object
        """
        if os.path.isfile(filePath1) and os.path.isfile(filePath2):
            self._filePath1 = filePath1
            self._filePath2 = filePath2
        else:
            print("Implement error handling")
            exit()
        self._hasReadInFiles = False

    def _readInFileToList(self, filePath):
        """
        Private method to return a list of lines contained in the input file
        """
        destinationList = []
        with open(filePath, "r") as f:
            for line in f:
                destinationList.append(line.replace("\n","").replace("\r",""))
        return destinationList

    def readInFiles(self):
        """
        Method to read the files into lists. Use when files have been updated
        """
        self._hasReadInFiles = True
        self._fileList1 = self._readInFileToList(self._filePath1)
        self._fileList2 = self._readInFileToList(self._filePath2)

    def findMatchingLinesAnyOrder(self, shouldPrint=False):
        """
        Method to match the lines within files.
        It should maintain a sensible order, like the order of the first
        file from the constructor.
        Return a list of lines that match.
        Optional argument to have it print out that list without the blank lines
        """
        if not self._hasReadInFiles:
            self.readInFiles()
        setOf2 = set(self._fileList2)
        ret = [line for line in self._fileList1 if line in setOf2]
        if shouldPrint:
            print("Matching lines between " + self._filePath1 + " and " + self._filePath2 + ":")
            removingBlanks = [line for line in ret if line != ""]
            print(*removingBlanks, sep='\n')
        return ret

    
    def compareFileHashes(self, stringOfHash="sha1", shouldPrint=True):
        """
        Method to take the hash of the two files for comparison
        Defaults to the SHA1 hashing algorithm, but the algo can be set to something like:
        - sha1
        - sha224
        - sha256
        - sha384
        - sha512
        - blake2b   (Added in newer versions of Python)
        - blake2s   (Added in newer versions of Python)
        - md5   (md5 not a guaranteed algorithm, python implementation dependent)
        Has argument to specify that as a string
        Has argument to specify whether or not to print out or just return T/F
        """
        hashes = []
        for filename in [self._filePath1, self._filePath2]:
            hasher = hashlib.new(stringOfHash)
            with open(filename, 'rb') as f:
                buf = f.read()
                hasher.update(buf)
                hashes.append(hasher.hexdigest())
                print(hasher.hexdigest())
        ret = hashes[0] == hashes[1]
        if shouldPrint:
            print("Are hashes the same: " + str(ret))
        return ret





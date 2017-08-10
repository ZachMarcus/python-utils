import sys
sys.path.append('..')

from FileSystem import FileComparator


myComp = FileComparator.FileComparator("./testFileSystem.py", "./testFileSystem.py")
newList = myComp.findMatchingLinesAnyOrder(False)
myComp.compareFileHashes("sha512")

myComp2 = FileComparator.FileComparator("./testFileSystem.py", "./testNetwork.py")
newList2 = myComp2.findMatchingLinesAnyOrder(True)
myComp2.compareFileHashes()



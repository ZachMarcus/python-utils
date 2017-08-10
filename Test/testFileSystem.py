import sys
sys.path.append('..')

from FileSystem import FileComparator
from FileSystem import DirectoryComparator

def testFileComparator():
    myComp = FileComparator.FileComparator("./testFileSystem.py", "./testFileSystem.py")
    newList = myComp.findMatchingLinesAnyOrder(False)
    myComp.compareFileHashes("sha512")

    myComp2 = FileComparator.FileComparator("./testFileSystem.py", "./testNetwork.py")
    newList2 = myComp2.findMatchingLinesAnyOrder(True)
    myComp2.compareFileHashes()

def testDirectoryComparator():
    print("------")
    myComp = DirectoryComparator.DirectoryComparator("../Test", "../Test")
    print(myComp.filesAndDirsInAButNotInB())
    print(myComp.filesAndDirsInBButNotInA())
    print(myComp.filesAndDirsInBoth())
    print(myComp.dirsInBoth())
    print(myComp.filesInBoth())
    myComp.changedFiles(True)
    print(myComp.compareChangedFiles())
    print("------")
    myComp2 = DirectoryComparator.DirectoryComparator("../FileSystem", "../Network")
    print(myComp2.filesAndDirsInAButNotInB())
    print(myComp2.filesAndDirsInBButNotInA())
    print(myComp2.filesAndDirsInBoth())
    print(myComp2.dirsInBoth())
    print(myComp2.filesInBoth())
    myComp2.changedFiles(True)
    print(myComp2.compareChangedFiles())



if __name__ == "__main__":
    testFileComparator()
    testDirectoryComparator()


from FileSystem.FileComparator import FileComparator

import filecmp



class DirectoryComparator(object):
    """
    Class to compare two directories
    Takes in two directory paths
    And can give common files and directories, or differences
    TODO: Add in better file comparison
    """
    def __init__(self, directory1, directory2, ignore=None, hide=None):
        """
        Constructor for DirectoryComparator.
        First two arguments are filepaths as string
        Optional last two arguments tell it how to behave for special files
        """
        self._directory1 = directory1
        self._directory2 = directory2
        self._ignoredFiles = ignore
        self._hiddenFiles = hide
        self._directoryCompare = filecmp.dircmp(self._directory1,
                                                self._directory2,
                                                self._ignoredFiles,
                                                self._hiddenFiles)
        self._hasComputedChangedFiles = False

    def filesAndDirsInAButNotInB(self):
        """
        Returns a list of file and directories in first dir but not second
        """
        return self._directoryCompare.left_only

    def filesAndDirsInBButNotInA(self):
        """
        Returns a list of files and dirs in second dir but not in first
        """
        return self._directoryCompare.right_only

    def filesAndDirsInBoth(self):
        """
        Returns a list of files and dirs common between them
        """
        return self._directoryCompare.common

    def dirsInBoth(self):
        """
        Returns a list of dirs common between them
        """
        return self._directoryCompare.common_dirs

    def filesInBoth(self):
        """
        Returns a list of files common between them
        """
        return self._directoryCompare.common_files

    def changedFiles(self, shouldPrint=False):
        """
        Returns a list of files common between them,
        that have been modified or that don't match for whatever reason
        """
        self._changedFiles = []
        self._hasComputedChangedFiles = True
        for fil in self.filesInBoth():
            fileComp = FileComparator(self._directory1+'/'+fil,
                                      self._directory2+'/'+fil)
            isSame = fileComp.compareFileHashes("sha1", False)
            if shouldPrint:
                print(fil + " is same: " + str(isSame))
            if not isSame:
                self._changedFiles.append(fil)
        return self._changedFiles

    def compareChangedFiles(self, shouldPrint=False):
        """
        Returns a dictionary of filename, value
        filename is the file being compared
        value is a list of matching lines
        TODO: Make it something better than a list of matching lines
        """
        if not self._hasComputedChangedFiles:
            self.changedFiles()
        ret = dict()
        for fil in self._changedFiles:
            fileComp = FileComparator(self._directory1+'/'+fil,
                                      self._directory2+'/'+fil)
            ret[fil] = fileComp.inDepthComparison()
        return ret



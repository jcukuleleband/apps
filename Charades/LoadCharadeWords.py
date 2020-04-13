import os.path
from os import path
import pathlib




class LoadCharadeWords:

    #goodFileLocation = True
    list = []

    def isDataLocationValid(self,filenamepath):
        print("DEBUG: isDataLocationValid: " + filenamepath)
        file = pathlib.Path(filenamepath)
        if file.exists():
            return True
        else:
            return False

    def setDataLocation(self,filenamepath):
        print("DEBUG: setDataLocation: " + filenamepath)
        if(self.isDataLocationValid(filenamepath)==True):
            file = open(filenamepath, "r")
            lines = file.readlines()

            for word in lines:
                if(word.strip()!=""):
                    self.list.append(word.strip())
            #add test for null and proper format
            #todo: Add debug
            for word in self.list:
                print(word)
        else:
            print("File bad")
            #TODO: Throw Exceptional error

    def getCharadeWords(self):
        print("DEBUG: getCharadeWords: NO INPUT VAR")
        #print(self.list)
        return self.list

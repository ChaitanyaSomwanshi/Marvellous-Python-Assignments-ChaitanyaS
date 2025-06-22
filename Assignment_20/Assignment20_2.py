'''
2. Design automation script which accept directory name and write names of duplicate files from that directory
into log file named as Log.txt. Log.txt file should be created into current directory.

Usage : DirectoryDuplicate.py "Demo"

Demo is name of directory.

'''

import os
import hashlib
import time


def Calchecksum(Fname):

    BlockSize = 1024

    fobj = open(Fname,"rb")

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)

    while len(buffer) > 0:
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    
    fobj.close()

    return hobj.hexdigest()



def DuplicateFiles(DirName):

    flag = os.path.isabs(DirName)

    if (flag == False):
        DirName = os.path.abspath(DirName)

    flag = os.path.exists(DirName)

    if (flag == False):
        print("Invalid Path.")
        exit()

    flag = os.path.isdir(DirName)

    if (flag == False):
        print("Valid Path but directory not found")
        exit()
    
    print("Absoulate path is :", DirName)

    Duplicate = {}

    for FolderName , SubFolderNames , FileNames in os.walk(DirName):

        for file in FileNames:
            file = os.path.join(FolderName,file)
            checksum = Calchecksum(file)

            if checksum in Duplicate:
                Duplicate[checksum].append(file)

            else:
                Duplicate[checksum] = [file]
    
    return DispalyDuplicate(Duplicate)


def DispalyDuplicate(Dict):

    result = list(filter(lambda x : len(x) > 1, Dict.values()))

    count = 0


    DuplicateFileList = []

    for Value in result:
        for SubValue in Value:
            count = count + 1
            DuplicateFileList.append(SubValue)
                
        count = 0

   

    LogFile(DuplicateFileList)



def LogFile(DuplicateFileList):

    fobj = open("Log.txt","a")

    fobj.write("-" * 84 + "\n")
    fobj.write(f"File created at : {time.ctime()} \n")
    fobj.write("-" * 84 + "\n")

    for i in DeletedFileList:
        fname = i.rsplit("\\",1)[-1]
        fobj.write(f"{fname} \n")

    fobj.write("-" * 84 + "\n")

    fobj.close()
    


def main():


    DuplicateFiles("Demo")


if __name__ == "__main__":
    main()
'''
3. Design automation script which accept directory name and delete all duplicate files from that directory.
write names of duplicate files from that directory into log file named as log.txt. log.txt file should be
created into current directory.

Usage : DirectoryDuplicateRemoval.py "Demo"

Demo is name of Directory

'''

import os
import hashlib
import time

def CheckSum(Fname):

    BlockSize = 1024

    fobj = open(Fname , "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)

    while len(buffer) > 0 :
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    return hobj.hexdigest()


def CheckDir(DirName):

    flag = os.path.isabs(DirName)

    if (flag == False):
        DirName = os.path.abspath(DirName)

    flag = os.path.exists(DirName)

    if (flag == False):
        print("Path Invalid")
        exit()

    flag = os.path.isdir(DirName)

    if (flag == False):
        print("Path valid but directory not found")
        exit()

    print("Absoulte path is :", DirName)

    Duplicate = {}
    for FolderName, SubFolderName , FileNames in os.walk (DirName):

        for FName in FileNames:
            FName = os.path.join(FolderName,FName)
            checksum = CheckSum(FName)

            if checksum in Duplicate:
                Duplicate[checksum].append(FName)

            else:
                Duplicate[checksum] = [FName]

    DeleteDuplicate(Duplicate)

def DeleteDuplicate(MyDict):

    result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    DuplicateFileList = []
    count = 0
    cnt = 0

    for value in result:
        for subvalue in value:
            count = count + 1

            if (count > 1):
                cnt = cnt + 1
                DuplicateFileList.append(subvalue)
                os.remove(subvalue)

        count = 0


    LogFile(DuplicateFileList)


def LogFile(Data):

    Lfile = open("DuplicateFilelog.txt", "a")

    Lfile.write("-" * 84 + "\n")
    Lfile.write(f"File created at : {time.ctime()} \n")
    Lfile.write("-" * 84 + "\n")

    for i in Data:

        fname = i.rsplit("\\",1)[1]
        Lfile.write(f"{fname} \n")

    Lfile.write("-" * 84 + "\n")
    # Lfile.write(f"Total Duplicate file found : {No} \n")
    Lfile.write("-" * 84 + "\n")



def main() :

    CheckDir("Demo")

    


if __name__ == "__main__":
    main()
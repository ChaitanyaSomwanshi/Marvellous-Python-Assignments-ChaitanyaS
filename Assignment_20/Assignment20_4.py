'''
4. Design automation script which accept directory name and delete all duplicate files from that directory.
write names of duplicate files from that directory into log file named as log.txt. log.txt file should be
created into current directory. Display execution time required for the script.

Usage : DirectoryDuplicateRemoval.py "Demo"

Demo is name of Directory

'''

import os
import hashlib
import time
import datetime




def CheckDirectrory(DirName):

    flag = os.path.isabs(DirName)

    if (flag == False):
        DirName = os.path.abspath(DirName)

    flag = os.path.exists(DirName)

    if( flag == False):
        print("Invalid Path")
        exit()

    flag = os.path.isdir(DirName)

    if( flag == False):
        print("Valid Path but there is no such directory")
        exit()


    # print("Absolute path is :", DirName)

    DuplicateDict = {}

    for FolderName, SubFolderName, FileName in os.walk(DirName):

        for File in FileName:
            File = os.path.join(FolderName,File)

            checksum = CheckSum(File)

            if checksum in DuplicateDict:
                DuplicateDict[checksum].append(File)


            else:
                DuplicateDict[checksum] = [File]

    
    DeleteDuplicate(DuplicateDict)

    

def CheckSum(File):

    BlockSize = 1024

    fobj = open(File, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)

    while len(buffer) > 0:
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    return hobj.hexdigest()


def DeleteDuplicate(MyDict):

    result = list(filter(lambda x : len(x) > 1 , MyDict.values()))

    count = 0
    cnt = 0
    DeleteFiles = []

    for value in result:
        for subvalue in value:
            count = count + 1

            if (count > 1) :
                DeleteFiles.append(subvalue)
                os.remove(subvalue)

        count = 0

    DeleteFileLog(DeleteFiles)
    
def DeleteFileLog(Data):

    Lfile = open("DeleteFileLog","a")

    Lfile.write("-" * 84 + "\n")
    Lfile.write(f"File created at : {time.ctime()} \n")
    Lfile.write("-" * 84 + "\n")


    for i in Data:
        fname = i.rsplit("\\",1)[-1]
        Lfile.write(f"{fname} \n")


    Lfile.write("-" * 84 + "\n")
    

    


def main():

    StartTime = datetime.datetime.now()

    # StartTime = StartTime.time()


    CheckDirectrory("Demo")


    EndTime = datetime.datetime.now()

    # EndTime = EndTime.time()

    ExtTime = EndTime - StartTime

    print("Total execution time for delete process :", ExtTime)

    




if __name__ == "__main__":
    main()
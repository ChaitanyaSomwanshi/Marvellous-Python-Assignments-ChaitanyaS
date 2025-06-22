'''
Please follow below rules while designing automation script as

● Accept input through command line or through file
● Display any message in log file instead of console
● For Separate task define Separate function
● For robustness handle every exptected exception
● Perform validations before taking any action.
● Create user defined modules to store the functionality.


1. Design automation script which accept directory name and display checksum of all files.

Usage : DirectoryChecksum.py "Demo"

Demo name is directory

'''

import os
import hashlib
import time


def DisplayChecksum(DirName):

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

    BlockSize = 1024
    Data =[]

    for FolderName, SubFolderName, FileNames in os.walk(DirName):

        for file in FileNames:
            filePath = os.path.join(FolderName,file)

            fobj = open(filePath,"rb")
            hobj = hashlib.md5()
            buffer = fobj.read(BlockSize)
            while (len(buffer) > 0):
                hobj.update(buffer)
                buffer = fobj.read(BlockSize)
            
            checksum = hobj.hexdigest()

            Data.append({"Name" : file , "checksum" : checksum})

    CreatelogFile(Data)
    
            
def CreatelogFile(Data):

    LogFile = open("LogFile","a")

    LogFile.write("-" * 84 + "\n")
    LogFile.write(f"File created at : {time.ctime()} \n")
    LogFile.write("-" * 84 + "\n")


    for i in Data:
        LogFile.write(f"File Name : {i["Name"]} , CheckSumValue :{i["checksum"]} \n")



    LogFile.write("-" * 84 + "\n")   

def main():
    # DirName = input()

    DisplayChecksum("Demo")




if __name__ == "__main__":
    main()
'''
3. Design automation script which accept two directory names. copy all files from first directory into second
directory. second directory should be created at run time.

'''

import os
import shutil
import time


def CopyFiles(Dir1,Dir2):

    flag = os.path.isabs(Dir1)

    if (flag == False):
        Dir1 = os.path.abspath(Dir1)

    flag = os.path.exists(Dir1)

    if(flag == False):
        print("Invalid Path")
        exit()


    flag = os.path.isdir(Dir1)

    if(flag == False):
        print("Valid path but there is no such directory.")
        exit()


    print("Absolute path is :", Dir1)

    flag = os.path.exists(Dir2)

    if (flag == False):
        os.mkdir(Dir2)

    Dir2 = os.path.abspath(Dir2)
    
    print("Absolute path is :", Dir2)

    data = []

    for FolderName , SubFolderNames, FileNames in os.walk(Dir1):

        for files in FileNames:
            SfilePath = os.path.join(Dir1,files)
            TfilePath = os.path.join(Dir2,files)
            shutil.copy(SfilePath,TfilePath)
            data.append(files)

    createlogfile(data)
    

def createlogfile(Data):



    file = open("CopyData.log","a")

    file.write("-" * 84 +"\n")
    file.write(f"Copy file at : {time.ctime()}\n")

    file.write("-" * 84 +"\n")

    for i in Data:
        file.write(f"{i}\n")

    file.write("-" * 84 +"\n")
    
    file.close()

def main():


    # arguments from file

    Dir1 = input()
    Dir2 = input()
    
    CopyFiles(Dir1,Dir2)


if __name__ == "__main__":
    main()
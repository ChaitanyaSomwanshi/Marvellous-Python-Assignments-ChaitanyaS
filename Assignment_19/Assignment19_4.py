'''
4. Design automation script which accept two directory names and one file extension. Copy all file with the
specified extension from first directory into second directory. second directory should be created at run time.

usage : DirectoryCopyExt.py "Demo" "Temp" ".exe"

Demo is name of directory which is existing and contains files in it. We have to create new Directory as temp and
copy all files with extension .exe from Demo to Temp.

'''

import os
import shutil
import time

def CopyExtFile(Dir1,Dir2,extension):


    flag = os.path.isabs(Dir1)

    if (flag == False):
        Dir1 = os.path.abspath(Dir1)

    flag = os.path.exists(Dir1)

    if (flag == False):
        print("Invalid Path")
        exit()

    flag = os.path.isdir(Dir1)

    if (flag == False):
        print("Valid path but there is no such directory.")
        exit()

    print("Absolute path is :", Dir1)

    flag = os.path.isdir(Dir2)

    if (flag == False):
        os.mkdir(Dir2)

    Dir2 = os.path.abspath(Dir2)
        

    print("Absolute path is :", Dir2)

    Data = []


    for FolderName, SubFolderNames, FileNames in os.walk(Dir1):

        for files in FileNames:
            if files.endswith(extension):
                Spath = os.path.join(Dir1,files)
                Dpath = os.path.join(Dir2,files)
                shutil.copy(Spath,Dpath)
                Data.append(files)

    
    CreateLogFile(Data)

def CreateLogFile(Data):

    file = open("CopyExtData.log","a")

    file.write("-" * 84 +"\n")
    file.write(f"Copy file at : {time.ctime()}\n")

    file.write("-" * 84 +"\n")

    for i in Data:
        file.write(f"{i}\n")

    file.write("-" * 84 +"\n")
    
    file.close()

def main():

    Dir1 = input()
    Dir2 = input()
    Extension = input()


    CopyExtFile(Dir1,Dir2,Extension)




if __name__ == "__main__":
    main()
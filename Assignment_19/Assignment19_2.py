'''

2. Design automation script which accept directory name and two file extensions from user.
Rename all files with first file extension with second file extension.

'''

import os

def ChangeFileExtension(DirName,extension1,extension2):

    fobj = os.path.isabs(DirName)

    if (fobj == False):
        DirName = os.path.abspath(DirName)

    fobj = os.path.exists(DirName)

    if (fobj == False):
        print("Path Invalid")
        exit()

    fobj = os.path.isdir(DirName)

    if (fobj == False):
        print("Path is valid but there is no such directory.")
        exit()

    
    # print("Absolute path is :", DirName)

    for FolderName, SubFolderNames, FileNames in os.walk(DirName):

        for file in FileNames:
            if file.endswith(extension1):
                Opath = os.path.join(DirName,file)
                Fname = os.path.splitext(file)
                Fname = (Fname[0])+extension2
                Npath = os.path.join(DirName,Fname)
                os.rename(Opath,Npath)          


def main():

    DirName = input()
    extension1 = input()
    extension2 = input()

    ChangeFileExtension(DirName,extension1,extension2)

    



if __name__ == "__main__":
    main()
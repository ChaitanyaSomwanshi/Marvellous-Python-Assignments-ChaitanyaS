'''
1. Write a program which accepts file name from user and check whether that file exists in current directory
or not.

'''

import os

def checkdir(DirName):

    flag = os.path.isabs(DirName)

    if (flag == False):
        DirName = os.path.abspath(DirName)

    flag = os.path.exists(DirName)

    if (flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirName)

    if (flag == False):
        print("path is valid but the target is not directory.")
        exit()

    print("Absolute path is :", DirName)


    print("Enter File Name : ")
    Fname = input()


    Fpath = os.path.join(DirName,Fname)

    flag = os.path.isfile(Fpath)

    if (flag == False):
        print(f"{Fname} file not found.")

    else:
        print(f"{Fname} file found.")

    # for FolderName, SubFolderNames, FileNames in os.walk(DirName):

    #     for file in FileNames:
    #         if Fname == file:
    #             print("file found :",Fname)
                
            



def main():
    print("Enter Directory Name :")
    DirName = input()

    checkdir(DirName)




if __name__ == "__main__":
    main()
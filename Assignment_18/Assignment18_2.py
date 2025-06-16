'''
2. Write a program which accept file name from user and open that file and display the contents of that file
on screen.

'''

import os

def FileContent(Fname, DirName = "1"):

    flag = os.path.isabs(DirName)

    if (flag == False):
        DirName = os.path.abspath(DirName)

    flag = os.path.exists(DirName)

    if(flag == False):
        print("Path is invalid")
        exit()

    flag = os.path.isdir(DirName)

    if(flag == False):
        print("Path is valid but there is no such directory.")
        exit()


    print("Absoulate path is :", DirName)


    flag = os.path.isfile(Fname)

    if (flag == False):
        print("File not present in directtory")

    else:
        fpath = os.path.join(DirName,Fname)

        fobj = open(fpath,"r")

        fread = fobj.read()

        print(fread)



    # for FolderName, SubFolderNames, FileNames in os.walk(DirName):

    #     for file in FileNames:
    #         if file == Fname:
    #             fobj = open(Fname,"r")
    #             fread = fobj.read()
    #             print(fread)
    #             fobj.close()




def main():
    print("Enter file name which you want to read : ")
    Fname = input()

    FileContent(Fname)



if __name__ == "__main__":
    main()
'''

Please follow below rules while designing automation script as

● Accept input through command line or through file
● Display any message in log file instead of console
● For Separate task define Separate function
● For robustness handle every exptected exception
● Perform validations before taking any action.
● Create user defined modules to store the functionality.


1. Design automation script which accept directory name and file extention from user. Display all files with
that extension.

'''

import sys
import os

def Display(DirectoryName,extension):

    fobj = os.path.isabs(DirectoryName)

    if (fobj == False):
        DirectoryName = os.path.abspath(DirectoryName)

    fobj = os.path.exists(DirectoryName)

    if (fobj == False):
        print("Path Invalid")
        exit()

    fobj = os.path.isdir(DirectoryName)

    if (fobj == False):
        print("Path is valid but there is no such directory.")
        exit()

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):

        for file in FileNames:
            if file.endswith(extension):
                print(file)




def main():

    # Accept input through command line
    

    if (len(sys.argv) == 2):
        if (sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
            print("This is automation script for find out specific extension files.")
            exit()

        if (sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
            print("script.py Argument1(DirName), Argument2(extension)")
            exit()

    if (len(sys.argv) != 3):
        print("Invalid arguments, please enter '--h' or '--u' for more info." )
        
    else:
        Display(sys.argv[1], sys.argv[2])


    # Accept input  through file

    # Display(input(),input())


if __name__ == "__main__":
    main()



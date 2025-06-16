'''

3. Write a program which accept file name from user and create new file named as Demo.txt and copy all contents 
from existing file into new file. Accept file name through command line arguments.

'''

import sys
import os

def CopyData(Fname):

    if len(sys.argv) == 2:
        if (sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
            print ("This is CopyData Automation Script")
            exit()

        if (sys.argv[1]== "--u") or (sys.argv[1] == "--U"):
            print ("ScriptName.py, Argument[1] for File Name")
            exit()

        
    flag = os.path.isfile(Fname)

    if (flag == False):
        print("File not in such directory")

    else:
        fobj = open(Fname,"r")

        fread = fobj.read()

        fobj.close()


        Nfile = open("Demo.txt","w")

        Nfile.write(fread)

        Nfile.close()

    
    


def main():

    if  (len(sys.argv) != 2):
        print("Invalid Arguments, use --h for help and --u for usage")
    else:

        CopyData(sys.argv[1])


if __name__ == "__main__":
    main()
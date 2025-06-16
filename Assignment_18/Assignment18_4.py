'''
4. Write a program which accept two file names from user and compare content of the both the file. if both the
files contains same then display success otherwise display failure.
Accpet names of the file from command line.

'''
import sys
import hashlib


def Display(Fname1, Fname2):

    BlockSize = 1024

    fobj = open(Fname1,"rb")

    hobj = hashlib.md5()
    buffer = fobj.read(BlockSize)
    while (len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)


    print (hobj.hexdigest())

    fobj.close()


    print ("_"*84)

    fobj1 = open(Fname2,"rb")

    hobj1 = hashlib.md5()
    buffer1 = fobj1.read(BlockSize)
    while (len(buffer1) > 0):
        hobj1.update(buffer1)
        buffer1 = fobj1.read(BlockSize)


    print (hobj1.hexdigest())

    fobj1.close()


    if hobj.hexdigest() == hobj1.hexdigest():
        print("Success")
    else:
        print("Failure")



def main():

    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h"  or sys.argv[1] == "--H":
            print ("This is Compare Data Automation Script")
            exit()

        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print ("ScriptName.py, Argument[1] and Argument[2] for File Name")
            exit()


    if (len(sys.argv) != 3) or sys.argv[1] and sys.argv[2] in ["--h","--u"]:
        print("Invalid Arguments, use --h for help and --u for usage")
    else:

        Display(sys.argv[1], sys.argv[2])

        




if __name__ == "__main__":
    main()
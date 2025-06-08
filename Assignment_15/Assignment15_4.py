'''

4. write a program which accept two file names from user and compare contents of both the files.
if both the files contains same contents then display success otherwise display failure.
Accept names of both the files from commnad line.

'''

import sys

def main():

    FirstFile = sys.argv[1]

    FF = open(FirstFile,'r')

    FD = FF.read()

    SecondFile = sys.argv[2]

    SF = open(SecondFile,'r')

    SD = SF.read()

    if ( FD == SD):
        print ("Success")

    else: 
        print("fail")

    FF.close()
    SF.close()


if __name__ == "__main__":
    main()



    
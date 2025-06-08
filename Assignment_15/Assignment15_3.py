'''
3. Write a program which accept file name from user and create new file as Demo.txt and copy all contents from
existing file into new file. Accept file name through command line arguments.

input : ABC.txt
Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt

'''

import sys

def main():
    
    FileName = sys.argv[1]

    existingfile = open(FileName,'r')

    data = existingfile.read()

    NewFile = open("Demo1.txt",'w')

    NewFile.write(data)

    NewFile.close()
    existingfile.close()

    # opencreatefile = open("Demo1.txt",'r')

    # NewFileData = opencreatefile.read()

    #print(NewFileData)

    
if __name__ == "__main__":
    main()





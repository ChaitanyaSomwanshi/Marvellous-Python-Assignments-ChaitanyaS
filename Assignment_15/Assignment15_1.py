'''

1. Write a program which accepts file name from user and check whether that file exists in current in current 
directory or not.

Input : Demo.txt
check whether Demo.txt exists or not.

'''

import os


def main():

    print("Enter file name to check : ")
    FileName = input()

    ret = os.path.exists(FileName)

    if (ret == True):
        print("File present in current directory.")

    else:
        print("File not present in current directory.")



if __name__ == "__main__":
    main()



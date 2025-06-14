'''
3. Write a Python script to count the number of lines, words, and characters in a give file.

'''

import os

def main():

    print("Enter File name you want to open : ")
    Fname = input()

    flag = os.path.isfile(Fname)

    #  print(flag)

    if (flag == False):
        print("Invalid file name.")

    else:

        FName = open(Fname,"r")

        Fread = FName.read()

        print(Fread)

        N = 0
        W = 0
        C = 0

        C = len(Fread)
        W = len(Fread.split())
        N = len(Fread.splitlines())

        print(N)
        print(W)
        print(C)

        

if __name__ == "__main__":
    main()
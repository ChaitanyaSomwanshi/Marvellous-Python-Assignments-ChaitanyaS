'''
Q4. Design python application which creates three threads as small, capital, digits. All the threads accepts
string as parameter. small thread display number of small characters, capital thread display number of capital
characters and digits thread display number of digits. Display id and name of each thread.

'''

import os
import threading


def Small(Char):
    count = 0
    print("thread id of Small is :", threading.get_ident())
    for i in Char:
        if i.islower():
            count = count + 1


    print("number of Small characters :", count)


def Capital(Char):
    count = 0
    print("thread id of Capital is :", threading.get_ident())
    for i in Char:
        if i.isupper():
            count = count + 1

    print("number of Capital characters :", count)

    

def digits(Char):
    count = 0
    print("thread id of digits is :", threading.get_ident())
    for i in Char:
        if i.isdigit():
            count = count + 1

    print("number of digits in Char :", count)


def main():

    print ("Enter Char to check small, capital and digits : ")
    strcheck = input()

    T1 = threading.Thread ( target = Small , args = (strcheck,))
    T2 = threading.Thread ( target = Capital , args = (strcheck,))
    T3 = threading.Thread ( target = digits , args = (strcheck,))

    T1.start()
    T2.start()
    T3.start()



if __name__ == "__main__":
    main()





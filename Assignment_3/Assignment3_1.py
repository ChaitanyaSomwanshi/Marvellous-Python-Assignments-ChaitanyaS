# 1. Write a program which accept N numbers from user and store it into list.
# Return addition of all elements from that list.

from functools import reduce

print("Enter Numbers of elements :")
No = int(input())

def Addition ():
    Data = list()
    i = 1
    while i <= No:
        print("Enter Number")
        Value = int(input())

        Data.append(Value)
        i = i + 1 

    # total = 0
    # i = 0

    # while i < len(Data):
    #     total = total + Data[i]
    #     i = i + 1

    ret = reduce ( lambda A , B : A + B, Data)

    print("Addition of numbers :", total)

if __name__ == "__main__":
    Addition()


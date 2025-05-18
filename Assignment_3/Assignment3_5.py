''' 5. Write a program which accept N numbers from user and store it into list. return addition of all prime numbers
from that list. main python file accepts N Numbers from user and pass each number to Checkprime function which is
part of our user defined module name as MarvellousNum. name of the function from main python file should be 
listPrime().
'''

from MarvellousNum import Checkprime

Data = list()

print("Enter Numbers")
Size = int(input())

for i in range(Size):
    print("Enter Numbers to add in to list")
    No = int(input())

    Data.append(No)


print(Data)

def listPrime():
    Total = 0
    primeNum = list()
    for i in Data:
        if Checkprime(i):
            Total = Total + i
            primeNum.append(i)
    
    print(primeNum)
    return Total

ret = listPrime()

print(ret)








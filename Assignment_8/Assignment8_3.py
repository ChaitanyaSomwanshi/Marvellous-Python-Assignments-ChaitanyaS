'''
Q3. Design python application which creates two threads as evenlist and oddlist. both the threads accept list
of integers as parameters. evenlist thread add even elements from input list and display addition. Oddlist
thread add all odd elements from input list and display the addition.

'''

import threading

def evenlist(No):
    EvenData = []
    sum = 0

    for i in No:
        if i % 2 == 0:
            sum = sum + i
            EvenData.append(i)

    print(EvenData)    
    print("Addition of even numbers :",sum)


def Oddlist(No):
    OddData = []
    sum = 0

    for i in No:
        if i % 2 != 0:
            sum = sum + i
            OddData.append(i)

    print(OddData)    
    print("Addition of odd numbers :",sum)


def main():
    Data = []
    print("Enter Numbers of Elements to add in list")
    number = int(input())

    for i in range(number):
        no = int(input("Enter Number :"))
        Data.append(no)

    T1 = threading.Thread(target = evenlist , args = (Data,))
    T2 = threading.Thread(target = Oddlist , args = (Data,))
    

    T1.start()
    T2.start()

   




if __name__ == "__main__":
    main()













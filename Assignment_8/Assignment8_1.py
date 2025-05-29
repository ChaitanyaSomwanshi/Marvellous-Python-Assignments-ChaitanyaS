'''
Q1. Design python application which creates two thread names as even and odd. Even thread will display first
10 even numbers and odd thread will display first 10 odd numers.
'''

import threading

def DisplayEven():
    
    count = 1
    i = 2

    while count <= 10:
        print (i)
        i = i + 2
        count = count + 1

    # print()

    # for j in range(2,21,2):
    #     print(j)
        



def DisplayOdd():

    count = 1
    i = 1

    while count <= 10:
        print(i)
        i = i + 2
        count = count + 1

    # print()

    # for j in range(1,21,2):
    #     print(j)



def main():

    Even = threading.Thread(target = DisplayEven)
    Odd = threading.Thread(target = DisplayOdd)

    print("Display first 10 even numbers")

    Even.start()
    Even.join()
    
    print()

    print("Display first 10 odd numbers")

    Odd.start()
    Odd.join()


if __name__ == "__main__":
    main()





    
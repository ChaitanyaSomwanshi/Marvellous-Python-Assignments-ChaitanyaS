'''
Q2. Design python application which creates two threads as evenfactor and oddfactor. both the thread accept one
parameter as integer. Evenfactor thread will display addition of even factors of given number and oddfactor will
display addition of odd factors of given number. after execution of both the thread gets completed main thread
should display message as "exit from main".
'''

import threading

def EvenFactor(No):
    sum = 0
    for i in range(1,No+1):
        if No % i == 0 and i % 2 == 0:
            sum = sum + i
            
    
    print (sum)


def OddFactor(No):
    sum = 0
    for i in range(1,No+1):
        if No % i == 0 and i % 2 != 0:
            sum = sum + i
            
    print (sum)
    

def main():
    T1 = threading.Thread( target = EvenFactor , args = (12,))
    T2 = threading.Thread( target = OddFactor , args = (12,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("exit from main")


if __name__ == "__main__":
    main()



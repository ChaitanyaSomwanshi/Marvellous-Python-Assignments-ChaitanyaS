'''
Q1. Create a python program that starts 3 threads, each printing numbers from 1 to 5 with a delay 
of 1 seocnd. use threading.Thread.

'''

import threading

import time

def numbers():
    for i in range(1,6):
        print(i)
        time.sleep(1)

def main():

    T1 = threading.Thread ( target = numbers)
    T2 = threading.Thread ( target = numbers)
    T3 = threading.Thread ( target = numbers)

    T1.start()
    T1. join()

    
    T2.start()
    T2.join()


    T3.start()
    T3.join()


if __name__ == "__main__":
    main()
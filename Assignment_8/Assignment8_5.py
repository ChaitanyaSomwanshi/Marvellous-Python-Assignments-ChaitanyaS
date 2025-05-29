'''
Q.5 Design python application which contains two threads named as thread1 and thread2.
thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on screen. after execution of
thread1 gets completed then schedule thread2.

'''
import threading


def thread1():
    for i in range(1,51):
        print(i)


def thread2():
    for i in range(50,0,-1):
        print(i)


def main():

    T1 = threading.Thread (target = thread1)
    T2 = threading.Thread (target = thread2)

    T1.start()
    T1.join()

    print()

    T2.start()    
    T2.join()


if __name__ == "__main__":
    main()


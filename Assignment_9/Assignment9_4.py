'''

Q4. Create a Python program that compare execution time of summing numbers from 1 to 10 million using
normal function, threading and multiprocessing.

'''

import time
import threading
import multiprocessing

def summing():

    ans = 0
    for i in range(1,10000001):
        ans = ans + i

    print( ans)


def main():

    star_time = time.time()
    summing()
    end_time = time.time()
    print("Time executed for normal function : ", end_time - star_time)

    print()

    star_time = time.time()
    T1 = threading.Thread (target = summing)

    T1.start()
    T1.join()

    end_time = time.time()
    print("Time executed for threading : ", end_time - star_time)

    print()

    star_time = time.time()
    T2 = multiprocessing.Process( target = summing )
    T2.start()
    T2.join()
    end_time = time.time()
    print("Time executed for multiprocessing : ", end_time - star_time)


if __name__ == "__main__":
    main()


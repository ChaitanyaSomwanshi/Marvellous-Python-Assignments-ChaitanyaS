'''
Q3. Create a Python program that uses multiprocessing.Pool to compute factorial of numbers in a list.

'''

import multiprocessing

def factorial(No):
    ans = 1
    for i in range(1,No+1):
        ans = ans * i

    return ans


def main():

    numbers = [5,6,7,8,9,10]

    result = []

    p = multiprocessing.Pool()
    result = p.map(factorial,numbers)

    p.close()
    p.join()

    print(result)


if __name__ == "__main__":
    main()


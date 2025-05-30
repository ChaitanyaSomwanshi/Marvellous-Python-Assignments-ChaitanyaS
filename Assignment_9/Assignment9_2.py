'''
Q2. Write a python program using multiprocessing. Process to square a list of numbers using multiple
processes.

'''

import multiprocessing

def square(No):

    Data = []

    for i in No:
        ans = i * i
        Data.append(ans)

    print (Data)


def main():

    numbers = [1,2,3,4,5,6,7,8,9,10]

    num1 = list(range(numbers[0],numbers[5]))
    num2 = list(range(numbers[5],len(numbers)+1))

    # p1 = multiprocessing.Process(target = square, args = (numbers,))
    p1 = multiprocessing.Process(target = square, args = (num1,))
    p2 = multiprocessing.Process(target = square, args = (num2,))
    

    p1.start()
    p2.start()


if __name__ == "__main__":
    main()


        
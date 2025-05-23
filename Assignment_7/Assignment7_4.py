'''
Q.4 Accept a list of numbers and use reduce () (from functools) to find the product of all numbers

'''

from functools import reduce

reduceX = lambda A , B : A * B


def main():
    Data = []
    print("Enter Number of Elements to add")
    No = int(input())

    for i in range(1,No+1):
        print("Enter Number : ")
        No1 = int(input(f"Enter {i} Number : "))
        Data.append(No1)

    print(Data)

    rdata = reduce(reduceX,Data)
    print("reduce output is : ", rdata)


if __name__ == "__main__":
    main()



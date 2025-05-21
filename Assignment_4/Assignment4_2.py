# 2. Write a program which contains one lambda function which accept two parameters and return its multiplication

from functools import reduce

multi = lambda A,B : A * B

def main():

    # print("Enter first Number")
    # No1 = int(input())

    # print("Enter second Number")
    # No2 = int(input())

    # print(multi(No1,No2))

    Data = []

    i = 1

    while i <=2:
        print("Enter Number")
        No1 = int(input())

        Data.append(No1)
        i = i + 1

    print(Data)

    ret = reduce(multi,Data)

    print(ret)

    



if __name__ == "__main__":
    main()




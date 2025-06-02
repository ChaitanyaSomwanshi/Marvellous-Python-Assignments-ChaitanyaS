'''
Q2. Write a program which contains one lambda function which accept two parameters and return its
multiplication.

'''

multi = lambda A , B : A * B


def main():

    print("Enter First Number : ")
    No1 = int(input())

    print("Enter Second Number : ")
    No2 = int(input())

    ret = multi( No1 , No2 )

    print("Multiplication of two number is : ", ret)


if __name__ == "__main__":
    main()
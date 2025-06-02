'''
Q1. Write a program which contains one lambda function which accept one parameter and return power of two.

'''

power = lambda A : 2 ** A


def main():

    print("Enter Number : ")
    No = int(input())

    

    ret = power(No)
    print(f"power of {No} is : ", ret)


if __name__ == "__main__":
    main()
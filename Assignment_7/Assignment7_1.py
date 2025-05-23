'''
Q1. Write two lambda functions:

° One to calculate square of a number
° Another to calculate cube of a number

'''

# def square(No):
#     ret = No * No

#     print(ret)

# def cube(No):
#     ret = No ** No

#     print(ret)


square = lambda No : No * No

cube = lambda No : No ** No

def main():
    print("Enter Number : ")
    No = int(input())

    ret1 = square(No)
    print(ret1)

    ret2 = cube(No)
    print(ret2)


if __name__ == "__main__":
    main()





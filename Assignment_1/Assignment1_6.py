
'''
6. Write a program which accept number form user and check whether that number is
positive or negative or zero.

'''

def checkNum(No):
    print("inside checknum")
    if No < 0:
        print("Its Negative Number")
    elif No > 0:
        print("Its Positive number")
    else:
        print("Its Zero")


print("Please Enter Number")
Value = int(input())


checkNum(Value)
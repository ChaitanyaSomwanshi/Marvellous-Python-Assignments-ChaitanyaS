'''
2. Write a program which contains one function named as chkNum() which accept one
parameters as number, if number is even then it should display "Even Number" otherwise
display "Odd Number" on console.

'''

def ChkNum(No):
    print("Inside ChkNum")


No = int(input("Pleasr enter number : "))

ChkNum(No)

if No % 2 == 0:
    print("Its Even Number")
else:
    print("Its Odd Number")



#-------------------------------------------------------------------------

def ChkNum1(No):
    print("Inside ChkNum1")
    if No % 2 == 0:
        print("Its Even Number")
    else:
        print("Its Odd Number")

No = int(input("Pleasr enter number : "))

ChkNum1(No)



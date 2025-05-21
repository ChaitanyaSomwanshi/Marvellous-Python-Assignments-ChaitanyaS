# Q.1 Arithmetic Operations on Two Numbers
#     write a program to accept two integers from the user and display their:
# Sum
# Difference
# Product
# Division

print("Enter First Number : ")
No1 = int(input())

print("Enter Second Number : ")
No2 = int(input())

def Sum(No1,No2):
    ans = No1 + No2
    print("sum of two numbers is : ", ans)

def Diff(No1,No2):
    ans = No1 - No2
    print("Diff of two numbers is : ", ans)

def Prod(No1,No2):
    ans = No1 * No2
    print("Prod of two numbers is : ", ans)

def Div(No1,No2):
    ans = No1 / No2
    print("Div of two numbers is : ", ans)


def main():

    Sum(No1,No2)
    Diff(No1,No2)
    Prod(No1,No2)
    Div(No1,No2)

if __name__ == "__main__":
    main()
    
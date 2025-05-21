'''
Q5. Even or ODD Number Check
write a program to check whether the entered number is even or odd.

'''

print("Enter Number")
No1 = int(input())

def checkEven(No):
    if No % 2 == 0:
        print("its even")
    else:
        print("its ODD")


def main():
    checkEven(No1)

if __name__ == "__main__":
    main()
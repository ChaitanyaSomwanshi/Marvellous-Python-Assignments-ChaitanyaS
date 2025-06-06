'''
2. Factorial Using Recursion
write a recursive function to calculate factorial of a number

'''


def factorial(No):
    ans = 1
    for i in range(1,No+1):
        ans = i * ans
    print(ans)


fact = 1

def factorial1(No):
    global fact
    if No >= 1:
        fact = fact * No
        No = No - 1
        factorial1(No)



def main():
    factorial(5)
    factorial1(5)




if __name__ == "__main__":
    main()
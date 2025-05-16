# 5. Write a program which accept one number from user and check whether number is prime or not.


def checkPrime():
    print("Enter Number")
    No = int(input())

    count = 0

    for i in range(1,No + 1):
        if No % i == 0:
            count = count + 1
            
    if count == 2:
        print(f"{No} is prime number")
    else:
        print(f"{No} is not prime number")

    
            

    

if __name__ =="__main__":
    checkPrime()

# 3. Write a program which accept one number from user and return its factorial.


def factorial():
    print("Enter Number")
    No = int(input())
    ans = 1

    # for i in range (1,No+1):
    #     ans =  ans * i

    for i in range(No,0,-1):
        ans = ans * i
        
    print(f"factorial of {No} is {ans}")


    ans1 = No
    i = 1

    while i < No:
        ans1 = ans1 * i
        i = i + 1

    print (f"factorial of {No} is {ans1}")

    
    

if __name__ == "__main__":
    factorial()
        
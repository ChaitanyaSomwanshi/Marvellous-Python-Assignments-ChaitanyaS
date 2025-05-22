'''
Q5. Accept a number from the user and check whether it is prime or not.

'''

def main():

    print("Enter Number")
    No = int(input())

    count = 0

    if No < 2:
        print("Invalid Number")
    else:

        for i in range (1,No+1):
            if No % i == 0:
                count = count + 1

        if count == 2:
            print(f"{No} is prime number")
        else:
            print(f"{No} is not prime number")



if __name__ == "__main__":
    main()

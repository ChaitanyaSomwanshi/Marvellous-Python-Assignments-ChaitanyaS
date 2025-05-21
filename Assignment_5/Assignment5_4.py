'''
Q.4 Find Largest Among Three Numbers
Accept three numbers from the user and print the largest using nested if else statements.

'''

def maxN():

    print("Enter First Number")
    No1 = int(input())

    print("Enter Second Number")
    No2 = int(input())

    print("Enter Third Number")
    No3 = int(input())

    if No1 > No2:
        print(No1)
        if No1 < No3:
            print(No3)
    else:
        print(No2)

def main():
    maxN()

if __name__ == "__main__":
    main()
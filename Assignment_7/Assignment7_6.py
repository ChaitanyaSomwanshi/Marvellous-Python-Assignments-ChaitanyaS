'''
Q.6 Write a function that accepts a list of integers and returns a list of prime numbers using filter().

'''

def checkprime(No):

    count = 0

    
    for i in range(1,No+1):
        if No % i == 0:
            count = count + 1
                

    if count == 2:
        return True
    else:
        return False


    


def main():
    Data = []
    print("Enter Number of Elements to add")
    No = int(input())

    for i in range(1,No+1):
        print("Enter Number : ")
        No1 = int(input(f"Enter {i} Number : "))
        Data.append(No1)

    print(Data)

    fdata = list(filter(checkprime,Data))
    print(fdata)


if __name__ == "__main__":
    main()
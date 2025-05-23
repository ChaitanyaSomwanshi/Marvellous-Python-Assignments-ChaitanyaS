'''
Q3. Accept a list of numbers and use filter () to keep only even numbers.

'''

checkeven = lambda No : No % 2 == 0


def main():
    Data = []
    print("Enter Number of Elements to add")
    No = int(input())

    for i in range(1,No+1):
        print("Enter Number : ")
        No1 = int(input(f"Enter {i} Number : "))
        Data.append(No1)

    print(Data)

    fdata = list(filter(checkeven,Data))
    print("Filter Data is : ", fdata)


if __name__ == "__main__":
    main()
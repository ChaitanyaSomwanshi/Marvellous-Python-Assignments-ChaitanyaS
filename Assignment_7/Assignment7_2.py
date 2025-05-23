'''
Q2. Accept a list of integers from the user and use the map() function to double each value.

'''

mapx = lambda A : A * 2

def main():
    Data = []
    print("Enter Number of Elements to add")
    No = int(input())

    for i in range(1,No+1):
        print("Enter Number : ")
        No1 = int(input(f"Enter {i} Number : "))

        Data.append(No1)

    print(Data)

    mdata = list(map(mapx,Data))
    print("Map Data is : ", mdata)


if __name__ == "__main__":
    main()


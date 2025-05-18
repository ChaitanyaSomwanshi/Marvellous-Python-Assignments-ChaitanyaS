# 3. Write a program which accept N numbers from user and store it into list. return minimum number from the list.

def Minimum ():
    print("Enter Number on input")
    Size = int(input())

    Data = list()

    i = 0
    while i < Size:
        print("Enter Number")
        No = int(input())

        Data.append(No)
        i = i + 1

    print(Data)

    MinimumNum = Data[0]

    for x in Data:
        if x < MinimumNum:
            MinimumNum = x

    print("Minimum number in data is :", MinimumNum)

    # Data.sort()

    # print("Minimum number in data is :", Data[0])

    # if len(Data) > 0:
    #     Min = min(Data)
    #     print("Minimum number in data is :", Min)




if __name__ == "__main__":
    Minimum()
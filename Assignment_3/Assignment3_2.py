# write a program which accept N numbers from user and store in to list. return Maximum number from that list.



def MaxNum():
    print("Number of input")
    No = int(input())
    Data = list()
    dummyvalue = 0

    i = 0
    n = 0

    while i < No:
        print("Enter Number")
        Value = int(input())
        Data.append(Value)                    
        i = i+1

    MaximumNum = Data[0]

    for x in Data:
        if x > MaximumNum:
            MaximumNum = x

    print("Maximum Number in Data is :", MaximumNum)

    # Data.sort()
    # print("Maximum Number in Data is :", Data[-1])

    # if len(Data) > 0:
    #     Maximum = max(Data)
    #     print("Maximum number is :", Maximum)

    


if __name__ == "__main__":
    MaxNum()



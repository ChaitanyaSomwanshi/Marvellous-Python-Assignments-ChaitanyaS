# 4. write a program which accept N numbers from user and store it into list. Accept one another number from
#    user and return frequncy of that number from list

def fre():
    print("Enter number of list input")
    No = int(input())

    Data = list()

    for i in range(No):
        print("Enter Number")
        Value = int(input())

        Data.append(Value)
    
    print(Data)

    print("Enter New number in to list")
    No1 = int(input())

    Data.append(No1)

    print(Data)

    count = 0

    for i in Data:
        if No1 == i:
            count = count + 1

    print("freq of No1 in Data :", count)


if __name__ == "__main__":
    fre()

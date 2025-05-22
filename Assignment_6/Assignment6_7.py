# Q7 Accept 5 numbers from the user. find and print the largest number.



def main():
    Data = []

    for i  in range(5):
        print("Enter Number")
        No = int(input())

        Data.append(No)

    print(Data)

    Max = Data[0]

    for i in range(len(Data)):
        if Data[i] > Max:
            Max = Data[i]        
    print(Max)

    



if __name__ == "__main__":
    main()
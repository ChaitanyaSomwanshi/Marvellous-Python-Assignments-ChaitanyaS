'''

5. Accept file name and one string from user and return the frequency of that string from file.

Input : Demo.txt   Marvellous

Search " Marvellous " in Demo.txt

'''


def main():

    print("Enter file name : ")
    FN = input()

    FO = open(FN,"r")

    FR = FO.read()

    FR1 = FR.split()

    SearchWord = "Marvellous"

    count = 0

    for i in FR1:
        if i == SearchWord:
            count = count + 1


    print(count)

    # if "Marvellous"  in FR:
    #     print("true")

    # else:
    #     print("false")

    FO.close()

if __name__ == "__main__":
    main()
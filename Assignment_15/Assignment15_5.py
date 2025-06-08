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

    if "Marvellous"  in FR:
        print("true")

    else:
        print("false")

    FO.close()

if __name__ == "__main__":
    main()
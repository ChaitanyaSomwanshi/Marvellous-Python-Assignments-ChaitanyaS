'''

5. Accept file name and one string from user and return the frequency of that string from file.

'''

def checkfreq(Fname,Sword):

    fobj = open(Fname,"r")

    fread = fobj.read()

    fdata = fread.split()

    # print(fdata)

    count = 0

    for i in fdata:
        if i == Sword:
            count = count+1

    print(f" Freq of {Sword} is {count}")

    

def main():
    print("Enter file name :")
    Fname = input()

    print("Enter word to check freq :")
    Sword = input()

    checkfreq(Fname,Sword)


if __name__ == "__main__":
    main()

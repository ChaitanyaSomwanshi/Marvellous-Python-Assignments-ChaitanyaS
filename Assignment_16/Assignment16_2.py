'''
2. Write a program to read and display the contents of a file data.txt.

'''


def main():

    Fname = open("data.txt", "r")

    fdata = Fname.read()

    print(fdata)




if __name__ == "__main__":
    main()
'''
5. Write a program to read a file line by line and display only those lines that contain more than 5 words.

'''

def main():

    FName = open("data.txt", "r")

    Fread = FName.read()
    
    Flines = Fread.splitlines()

    for i in Flines:
        if (len(i.split()) > 5):
            print(i)

    


if __name__ == "__main__":
    main()
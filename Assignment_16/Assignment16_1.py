'''
1. Write a Python program to create a text file named student.txt and write the names of 5 student into it.

'''


def main():

    print("Enter File Name you want Create : ")
    Fname = input()

    Sfile = open(Fname, "w")


    for i in range(5):
        print("Enter Student Name :")
        SName = input()
        Sfile.write(SName + "\n")

    Sfile.close()

if __name__ == "__main__":
    main()



    







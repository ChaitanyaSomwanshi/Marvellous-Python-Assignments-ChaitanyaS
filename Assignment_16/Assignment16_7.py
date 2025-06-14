'''

Create a file marks.txt with student name and marks. then read the file and display student who scored more than 
75 marks.

'''

def main():

    
    Mfile = open("marks.txt","w")

    print("Enter number of student data you want to add : ")

    No = int(input())

    for i in range(No):
        Sname = input("Enter Student Name : ")
        Smarks = int(input("Enter Marks : "))

        Mwrite = Mfile.write(f"{Sname}, {Smarks}\n")

    Mfile.close()

    Mfile = open("marks.txt","r")


    while True:
        Mline = Mfile.readline()
        if not Mline:
            break
        Name = Mline.split(",")[0]
        Marks = int(Mline.split(",")[1])

        if Marks > 75:
            print(Mline)

    Mfile.close()
        


if __name__ == "__main__":
    main()

    
    
'''
2. Write a program which accept file name from user and open that file and display the contents of that file
on screen.

input : Demo.txt
Display contents of demo.txt on console.

'''



def main():

    print("Enter file name you want to open and read : ")
    FileName = input()

    fobj = open(FileName,'r',encoding = 'cp1252')

    data = fobj.read()

    print(data)

    

    fobj.close()
    

if __name__ == "__main__":
    main()


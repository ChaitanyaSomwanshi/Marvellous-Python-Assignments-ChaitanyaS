'''
6. Write a python program to copy the contents of one file (source.txt) into another file (destination.txt)

'''

def main():

    Sfile = open("source.txt","r")

    Sread = Sfile.read()

    Sfile.close()

    Dfile = open("destination.txt","w")

    Dwrite = Dfile.write(Sread)

    Dfile.close()



if __name__ == "__main__":
    main()
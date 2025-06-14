'''
8. Write a script to remove all blank lines from a file. Save the cleaned output to a new file.

'''
def main():

    Ofile = open("source.txt","r")

    Oread = Ofile.read()

    Olines = Oread.splitlines()

    Ofile.close()

    Data = []

    for i in Olines:
        if len(i.split()) > 0:
            Data.append(i)

    Nfile = open("Cleaned.txt","w")

    for i in Data:
        Nfile.write(f"{i}\n")

    Nfile.close()



if __name__ == "__main__":
    main()


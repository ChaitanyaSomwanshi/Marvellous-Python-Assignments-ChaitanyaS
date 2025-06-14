'''

4. Accept 10 numbers from the user and write them into file named numbers.txt, each on a new line.

'''

def main():
    data = []

    for i in range(10):
        print("Enter Number : ")
        No = int(input())

        data.append(No)

    print(data)

    Fname = open("numbers.txt","w")

    for i in data:
        Fname.write(f"{i}\n")


if __name__ == "__main__":
    main()
'''
Q1. Print Numbers Using Recursion.
Write a recursive function to print numbers from 1 to N.

'''

def numbers(No):
    for i in range(1,No+1):
        print(i)

i = 1


def numbers1(No):
    global i
    if i <= No:
        print(i)
        i = i + 1
        numbers1(No)



def main():
    numbers(5)
    print()
    numbers1(5)


if __name__ == "__main__":
    main()









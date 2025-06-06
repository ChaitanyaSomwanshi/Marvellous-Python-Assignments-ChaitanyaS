'''

7. Print Pattern Using Recursion (Right Triangle)
Write a recursive function to print the following pattern:

*
* *
* * *
* * * *

'''


def star(N):
    for i in range(N+1):
        print("*" * i)



def starX(N):
    count = 1
    while N >= 1:
        print("*" * count)
        count = count + 1
        N = N - 1


def starXX(N):
    if N == 0:
        return 
    else:
        starXX(N-1)
        print("* " * N)

    


def main():
    star(4)
    starX(4)
    starXX(4)
    


if __name__ == "__main__":
    main()



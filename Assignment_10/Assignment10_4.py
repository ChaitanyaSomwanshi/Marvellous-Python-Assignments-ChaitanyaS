'''
Q4. Write a program which contains filter(), map() and reduce() in it. python application which
contains one list of numbers, list contains the numbers which are accepted from user. filter should
filter out all such numbers which are even. Map function will calculate its square. Reduce will
return addition of all that numbers.

'''

from functools import reduce


# even = lambda No : No % 2 == 0
# squareN = lambda No :No * No
# addition = lambda A,B : A + B


def Even(No):
    if No % 2 == 0:
        return No

def square(No):
    ans = No * No
    return ans

def Addition(A,B):
    ans = A + B 
    return ans


def main():

    input_list = [5,2,3,4,3,4,1,2,8,10]

    fdata = list(filter(Even,input_list))

    print(fdata)

    mdata = list(map(square,fdata))
    
    print(mdata)

    rdata= reduce(Addition,mdata)
    print(rdata)


if __name__ == "__main__":
    main()
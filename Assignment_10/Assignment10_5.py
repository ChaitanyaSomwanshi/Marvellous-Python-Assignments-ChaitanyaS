'''
Q5. Wtite a program which contains filter(), map() and reduce() in it. python application which contains
one list of numbers. list contains the numbers which are accepted from user. Filter should filter out
all prime numbers. Map function will multiply each number by 2. reduce will return maximum number from
that numbers. (You can also use normal functions instead of lambda functions).

'''

from functools import reduce

def primeNum(No):
    count = 0
    for i in range(1,No+1):
        if No % i == 0:
            count = count + 1

    if count == 2:
        return No

def Multi(No):
    ret = No * 2
    return ret

def MaxNumber(A,B):
    if A > B:
        return A
    else:
        return B
    
    



def main():


    input_list = (2,70,11,10,17,23,31,77)

    fdata = list(filter(primeNum,input_list))
    print(fdata)

    mdata= list(map(Multi,fdata))
    print(mdata)
    
    rdata = reduce(MaxNumber, mdata)

    print(rdata)





if __name__ == "__main__":
    main()
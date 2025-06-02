'''
Q3. Write a program which contains filter(), map(), and reduce() in it. Python application which
contains one list of numbers. list contains the numbers which are accepted from user. filter
should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map
function will increase each number by 10. Reduce will return product of all that numbers.

'''

from functools import reduce

def FNumbers(No):
    if No >= 70 and No <= 90:
        return No

def increase(No):
    ans = 0
    ans = No + 10
    return ans

def product(A,B):
    ans = A * B 
    return ans



def main():
    input_list = [4,34,36,76,68,24,89,23,86,90,45,70]

    fdata = list(filter(FNumbers,input_list))

    print(fdata)

    mdata = list(map(increase,fdata))

    print(mdata)

    rdata = reduce(product,mdata)
    print(rdata)

if __name__ == "__main__":
    main()
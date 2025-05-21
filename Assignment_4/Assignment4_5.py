'''
5. Write a program which contains filter(), map(), and reduce() in it. python applicayion which contains one list
of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers.
Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use
normal functions insted of lambda functions.)

Input List = [2,70,11,10,17,23,31,77]
list after filter = [2,11,17,23,31]
list after map = [4,22,34,46,62]
Output of reduce = 62

'''

def primeNum(No):
    count = 0
    if No < 2:
        return False    
    
    for i in range (1,No+1):
        if No % i == 0:
            count = count + 1

    if count == 2:
        return True
    else:
        return False

def Multi(No):
    return No ** 2

def MaxN(A,B):
    if A > B:
        return A
    else:
        return B


def filterX(Task,value):
    Data1 = []
    for i in value:
        ret = Task(i)
        if ret == True:
            Data1.append(i)

    return Data1

def mapX(Task,value):
    Data2 = []
    for i in value:
        ret = Task(i)
        Data2.append(ret)

    return Data2

def reduceX(Task,value):

    maxN = value[0]
    for i in value:
        ret = Task(maxN, i)

    return ret

    

def main():
    print("Number of input : ")
    No = int(input())

    Data = []

    for i in range(No):
        print("enter number")
        Num = int(input())

        Data.append(Num)   

    print(Data)

    fdata = list(filterX(primeNum, Data))
    print("filter data is : ", fdata)

    mdata = list(mapX(Multi, fdata))
    print("Mapp data is : ", mdata)

    rdata = reduceX(MaxN, mdata)
    print("reduce output is : ", rdata)



if __name__ == "__main__":
    main()





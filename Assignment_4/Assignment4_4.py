'''
4. Write a program which contains filter(), map(), and reduce() in it. Python application which contains one list
of numbers. List contains the numbers which are accepet from user. Filter should filter out all auch numbers which
are even. map function calculate its square. reduce will return addition of all that numbers.

Input List = [5,2,3,4,3,4,1,2,8,10]
List after filter = [2,4,4,2,8,10]
List after map = [4,16,16,4,64,100]
Output of reduce = 204
'''

from functools import reduce

checkeven = lambda x : (x % 2 == 0)
NumSquare = lambda x : x * x 
sum = lambda A, B : A + B 


# def filterX(Task,value):
#     Data1= []

#     for i in value:
#         ret = Task(i)
#         if ret == True:
#             Data1.append(i)

#     return Data1

# def mapX(Task,value):
#     Data2 = []

#     for i in value:
#         ret = Task(i)
#         Data2.append(ret)

#     return Data2

# def reduceX(Task,value):
#     ret = 0

#     for i in value:
#         ret = Task(ret,i)

#     return ret


def main():
    print("Number of input : ")
    No = int(input())

    Data = []

    for i in range(No):
        print("enter number")
        Num = int(input())

        Data.append(Num)   

    print(Data)

    fdata = list(filter(checkeven, Data))
    print("filter data is : ", fdata)

    mdata = list(map(NumSquare, fdata))
    print("map data is : ", mdata)

    rdata = reduce(sum, mdata)
    print("reduce output is : ", rdata)




if __name__ == "__main__":
    main()
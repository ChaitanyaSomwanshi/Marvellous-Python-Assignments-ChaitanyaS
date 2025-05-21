'''
3. Write a program which contains filter(), map() and reduce() in it python application which contain one list of
numbers. list contains the number which accepted from user. filter should filter out all such numbers which
greater than or equal to 70 and less than or equal to 90. map fucntion will increase each number by 10. reduce will
return product of all that numbers.

input list = [4,34,36,76,68,24,89,23,86,90,45,70]
list after filter = [76,89,86,90,70]
list after map = [86,99,96,100,80]
output of reduce = 6538752000
'''

from functools import reduce

checknum = lambda x : x >=70 and x <=90
increase = lambda x : x + 10
multi = lambda A,B : A * B 

# def filterX(Task,value):
#     data1 = []

#     for i in value:
#         ret = Task(i)
#         if (ret == True):
#             data1.append(i)

#     return data1



# def mapx (Task,value):
#     data2 = []

#     for i in value:
#         ret = Task(i)
#         data2.append(ret)
#     return data2



# def reducex (Task,value):
#     ret = 1

#     for i in value:
#         ret =  Task(ret,i)
#     return ret


def main():
    data = []

    print("enter numbers of elements to add in list : ")
    No = int(input())

    for i in range(No):
        print("enter number to add : ")
        value = int(input())

        data.append(value)

    print(data)

    fdata = list(filter(checknum,data))
    print("fdata is : ", fdata)

    mdata = list(map(increase,fdata))
    print("mdata is : ", mdata)

    rdata = reduce(multi,mdata)
    print("rdata is : ", rdata)



if __name__ == "__main__":
    main()

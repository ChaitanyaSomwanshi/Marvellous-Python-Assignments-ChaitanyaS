# 4. Write a program which accept one number from user and return addition of its factors.


# from functools import reduce 

# redList = list()

def main():
    print("enter number")
    No = int(input())

    factors_total = 0
    i = 1
    factors = list()

    while i < No:
        if No % i == 0:
            factors.append(i)
            # redList.append(i)
            factors_total = factors_total + i
        i += 1

    print(factors_total)

    #----------------------------------------------------------
    # for loop : 

    factors1 = list()
    factors_total1 = 0

    for i in range(1,No):
        if No % i == 0:
            factors1.append(i)
            factors_total1 = factors_total1 + i
            

    print(factors_total1)

    # ---------------------------------------------------------------
    # with lambda reduce 

    # rd = reduce(lambda A, B : A + B, redList)

    # print(rd)
    

    

if __name__ == "__main__":
    main()

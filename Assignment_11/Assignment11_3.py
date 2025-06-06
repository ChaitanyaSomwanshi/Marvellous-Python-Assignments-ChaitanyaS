'''

3. Sum of Digits
Write a recursive funtion to calculate the sum of digits of a number.

'''

def SumDigit(No):
    total = 0

    while (No > 0):
        total = total + No % 10
        No = No // 10

    print(total)


total1 = 0

def rucSumDigit(num):
    global total1
    if num > 0:
        total1 = total1 + num % 10
        rucSumDigit( num // 10)
    return total1
    


def main():
    SumDigit(1234)
    ret = rucSumDigit(1234)
    print(ret)

if __name__ == "__main__":
    main()





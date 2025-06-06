'''

Q.5 Count Zeros in a number (Recursively)
write a recursive function to count how many zeros are in the give number.

count_zeros (1020300) --- 4

'''

def countZero(N):
    count = 0
    while N > 0:
        if N % 10 == 0:
            count = count + 1
        N = N // 10

    print(count)


Count = 0

def countZeros(N):
    global Count
    if N == 0:
        return 0

    if N % 10 == 0:
        Count = Count + 1
        countZeros( N // 10)
    else:
        countZeros(N // 10)

    return Count



def main():

    countZero(1020300)
    ret = countZeros(1020300)
    print(ret)


if __name__ == "__main__":
    main()
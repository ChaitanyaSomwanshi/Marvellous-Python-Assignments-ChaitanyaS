'''

Q.6 Sum of First N Natural Numbers
write a recursive function to calculate sum from 1 to N.

sum_n(5) - 15

'''

def sum_n(N):
    total = 0
    for i in range(1,N+1):
        total = total + i

    print(total)

N_total = 0

def sum_nX(N):
    global N_total
    while N > 0:
        N_total = N_total + N
        N = N - 1

    print(N_total)



def sum_nXX(N):
    if N == 0:
        return 0
    else:
        return N + sum_nXX(N-1)



def main():

    sum_n(5)
    sum_nX(5)
    ret = sum_nXX (5)
    print(ret)


if __name__ == "__main__":
    main()
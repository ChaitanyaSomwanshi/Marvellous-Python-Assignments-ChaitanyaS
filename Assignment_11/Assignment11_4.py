'''

4. Power function using Recursion

write a recursive function to calculate x^n.

'''

def power(A , B):
    ans = A ** B
    print(ans)


def powerX(A , B):
    
    if B == 0:
        return 1
    
    return A * powerX(A,B-1)



def main():
    power(2,3)
    ret = powerX(2,3)
    print(ret)
    

if __name__ == "__main__":
    main()
'''
7. write a program which contains one function that accept one number from user 
and returns true if number divisible by 5 otherwise return false.

'''

def TrueOrFalse(No):
    ans = 0
    ans = No % 5 
    print(ans)
    
    if ans == 0 :
        print("True")
    else:
        print("False")

    return ans


print("Enter Number")
Number = int(input())


TrueOrFalse(Number)


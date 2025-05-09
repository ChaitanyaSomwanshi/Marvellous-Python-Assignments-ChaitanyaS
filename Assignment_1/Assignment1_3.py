'''
3. Write a program which contains one function named as Add() which accept two numbers from
user and return addition of that two numbers.
'''

def Add(No1, No2):
    ans = 0
    ans = No1 + No2
    return ans


print("Please Enter First Number")
No1 = int(input())

print("Please Enter Second Number")
No2 = int(input())

Addition = Add(No1, No2)

print("Users two number addition is :", Addition)
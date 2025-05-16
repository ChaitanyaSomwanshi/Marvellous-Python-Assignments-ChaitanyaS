# 9. Write a program which accept number from user and return number of digits in that number.


print("Enter Number")
No = int(input())

count = 0

while No != 0:
    No  = No // 10
    count = count + 1

print(count)


#----------------------------------------------------------------------------------------------------

print("Enter Number")
No1 = int(input())

print(" number of digits :", len(str(No1)))





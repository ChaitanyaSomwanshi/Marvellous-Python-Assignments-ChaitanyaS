# 10. Write a program which accept number from user and return addition of digits in that number.

print("Enter Number")
No = int(input())

Total = 0

while No > 0:
    dig = No % 10
    Total = Total + dig
    No = No//10

print("Sum of digits of number is :", Total)
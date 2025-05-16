# 8. Write a program which accept one number and display below pattern

print("Enter Number")
No = int( input())

for i in range(1,No+1):
    for j in range(1, i + 1):
        print(j, end = " ")
        
    print()

print()

i = 1
while i < No + 1:
    j = 1
    while j < i +1:
        print(j, end = " ")
        j = j + 1
    print()
    i = i + 1
     
    
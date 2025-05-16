# 7. write a program which accept one number and display below pattern

print("Enter Number")
No = int(input())

for i in range(No):
    for j in range(1,No + 1):
        print(j, end = " ")
    print()


print()

i = 0

while i < No :
    j = 1
    while j < No + 1:
        print(j, end = " ")
        j = j + 1

    i = i + 1
    print()
    




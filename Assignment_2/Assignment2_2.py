# 2. write a program which accept one number and display below pattern.


print("Enter number")
No = int(input())

for i in range(No):
    print (No * "* ")
    

print()

i = 1
while i <= No:
    print(No * "* ")
    i = i + 1


print()

for i in range(No):
    for j in range(No):
        print("* ", end = " ")
    print()
'''
Q.3 Accept a number from the user and print its multiplication table up to 10.

'''

print("Enter a number : ")

No = int(input())


i = 1

while i <= 10:
    print(f"{No} * {i} = { No * i}")
    i = i + 1


#---------------------------------------------------------------------------------------------------------

print()

#-------------------------------------------------------------------------------------------------------------

for i in range(1,11):
    print(f"{No} * {i} = { No * i}")
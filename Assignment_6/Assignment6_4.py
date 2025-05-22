# Q4. Accept a number and print its factorial using a for loop:

print("Enter Number")
No = int(input())

Factorial = 1

for i in range(1,No+1):
    Factorial = Factorial * i

print(f"Factorial of {No} is : ", Factorial)


#------------------------------------------------------------------------------------

print()

#-------------------------------------------------------------------------------------------------------------


print("Enter Number")
No1 = int(input())

Factorial1 = 1

i = 1

while i <= No1:
    Factorial1 = Factorial1 * i
    i = i + 1

print(f"Factorial of {No1} is : ", Factorial1)

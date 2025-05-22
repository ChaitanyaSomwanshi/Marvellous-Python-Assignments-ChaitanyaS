# Q1. Print sum of even Numbers between 1 and 100. use the loop to find and print the sum of all even numbers
#     from 1 to 100

sum = 0
i = 2

while i <=100:
    sum = sum + i
    i = i + 2

print("Sum of even numbers between 1 to 100 is :", sum)

print()

#------------------------------------------------------------------------------------------------


Sum1 = 0

for i in range(2,101,2):
    Sum1 = Sum1 + i

print("Sum of even numbers between 1 to 100 is :", Sum1)
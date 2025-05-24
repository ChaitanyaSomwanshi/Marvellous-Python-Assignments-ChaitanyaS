'''
Q.5 Write a function that accept a string and checks whether it is a palindrome.

'''

print("Enter a String : ")
char = input()
print(char)

rev = char[ : : -1]
print(rev)


if char == rev:
    print("Its palindrome")
else:
    print("Its not palindrome")
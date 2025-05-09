'''
write a program which accept name from user and display length of its name.

'''

def lenName (name):
    print(name)
    print("length of UserName is ", len(name))


print("Enter your name")
UserName = input()

lenName(UserName)
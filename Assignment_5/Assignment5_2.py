'''
Q2. Vowel or Consonant Check
Accept a single character from the user and check if it is a Vowel (a,e,i,o,u). if not, print its Consonant

'''

VowelList = ["a","e","i","o","u"]

# print("Enter a character : ")
# character = input()

def checkVowel():
    print("Enter a character : ")
    character = input()

    if character in VowelList:
        print("Its Vowel")
    else:
        print("Its Consonant")

def main():
    checkVowel()

if __name__ == "__main__":
    main()
'''
Q3. Voting Eligibility Checker
Accept age  from the user and check whether the person is eligible to vote.
(Age should be 18 or above.)

'''

def CheckAge():
    print("Enter Age")
    Age = int(input())

    if Age >= 18:
        print("Eligible to vote.")
    else:
        print("Not Eligible to vote.")


def main():
    CheckAge()

if __name__ == "__main__":
    main()

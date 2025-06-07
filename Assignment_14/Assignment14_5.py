'''
5. Create a class BankAccount with account_number, name and balance. Use __init__ and create methods for deposit,
create methods for deposit, withdraw, and Displaying balance.

'''

class BankAccount:
    def __init__(self,account_number,name,balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance


    def deposit(self,amount):
        self.balance += amount
        return self.balance


    def withdraw(self,amount):
        self.balance -= amount
        return self.balance

    def DisplayBalance(self):
        return self.balance 


def main():
    obj1 = BankAccount(1234,"Chaitanya",15000)

    print(f"after deposit account balance is : {obj1.deposit(3000)}")
    print(f"after withdraw account balance is : {obj1.withdraw(1000)}")
    print(f"Current balance is : {obj1.DisplayBalance()}")


if __name__ == "__main__":
    main()




    


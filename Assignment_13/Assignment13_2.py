'''
2. Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & amount.
That class contains one class variable as ROI which is initialise to 10.5.
inside init method initialise all name and amount variable by accepting the values from user.
there are four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest().
Deposit() method will accept the amount from user and add that value in class instance variable Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable
amount.
CalculateIntrest() method calculate the intrest based on Amount by considering rate of interest which is Class Variable
as ROI.
And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects.



'''

class BankAccount:
    ROI = 10.5
    

    def __init__(self):
        self.Name = input("Enter Your Name : ")
        self.Amount = int(input("Enter Amount : "))

    def Deposit(self):
        amount = int(input("Enter Deposit amount : "))
        self.Amount += amount
        print("After Deposit total amount is :", self.Amount)

    def Withdraw(self):
        amount = int(input("Enter Withdraw amount : "))
        self.Amount -= amount
        print("After Withdraw total amount is :", self.Amount)
        
    def CalculateIntrest(self):
        intrest = self.Amount * BankAccount.ROI / 100
        print(intrest)

        
    def Display(self):
        print(self.Name , self.Amount)
        

def main():
    obj1 = BankAccount()
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateIntrest()
    obj1.Display()

    obj2 = BankAccount()
    obj2.Deposit()
    obj2.Withdraw()
    obj2.CalculateIntrest()
    obj2.Display()



if __name__ == "__main__":
    main()


    






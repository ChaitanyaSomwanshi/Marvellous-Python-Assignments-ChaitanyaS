'''

6. Create a class Calculator with methods for add, subtract, multiply, divide. Ask user input for values and call
methods accordingly.

'''


class Calculator:

    def __init__(self,Value1,Value2):
        self.Value1 = Value1
        self.Value2 = Value2


    def add(self):
        ans = 0
        ans = self.Value1 + self.Value2

        print("Addition of two numbers :", ans)


    def subtract(self):
        ans = 0
        ans = self.Value1 - self.Value2

        print("subtract of two numbers :", ans)

    def multiply(self):
        ans = 0
        ans = self.Value1 * self.Value2

        print("multiply of two numbers :", ans)

    def divide(self):
        ans = 0
        ans = self.Value1 / self.Value2

        print("divide of two numbers :", ans)


def main():

    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))

    obj1 = Calculator(No1,No2)

    obj1.add()
    obj1.subtract()
    obj1.multiply()
    obj1.divide()


if __name__ == "__main__":
    main()

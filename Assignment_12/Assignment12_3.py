'''
3. Write a program which contains one class method as Arithmetic.
Arithmetic class contains three instance variables as Value1, Value2.
Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Substraction(), Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1, Value2 and return result.
Substraction() method will perform Substraction of Value1, Value2 and return result.
Multiplication() method will perform Multiplication of Value1, Value2 and return result.
Division() method will perform Division of Value1, Value2 and return result.
After designing the above class call all instance methods by creating multiple objects.

'''

class Arithmetic:
    def __init__ (self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter First Number : "))
        self.Value2 = int(input("Enter Second Number : "))

    def Addition(self):

        ans = 0
        ans = self.Value1 + self.Value2
        return ans

    def Substraction(self):
        ans = 0
        ans = self.Value1 - self.Value2
        return ans

    def Multiplication(self):
        ans = 0
        ans = self.Value1 * self.Value2
        return ans

    def Division(self):
        ans = 0
        ans = self.Value1 / self.Value2
        return ans

def main():
    Obj1 = Arithmetic()
    Obj1.Accept()
    print( "Addition of ", Obj1.Value1 ,"and", Obj1.Value2 , "is", Obj1.Addition())
    print( "Substraction of ", Obj1.Value1 ,"and", Obj1.Value2 , "is", Obj1.Substraction())
    print( "Multiplication of ", Obj1.Value1 ,"and", Obj1.Value2 , "is", Obj1.Multiplication())
    print( "Division of ", Obj1.Value1 ,"and", Obj1.Value2 , "is", Obj1.Division())



if __name__ == "__main__":
    main()


    



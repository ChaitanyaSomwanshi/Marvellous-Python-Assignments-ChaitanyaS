'''
Q2. write a program which contains one class named as Circle.
Circle class contains three instance variables as Radius, Area, Circumference.
That class contains one class variable as PI which is initialise to 3.14
inside init method initialise all instance variable to 0.0
There are three instance method inside class as Accept(), CalculateArea(), CalculateCircumference(), Display().
Accept method will accept values of Radius from user.
CalculateArea() method will calculate area of circle and store it into instance variable area.
CalculateCircumference() method will calculate Circumference of circle and store it into instance variable Circumference.
and Display() method will display value of all the instance variable as Radius, Area, Circumference.
after desiging the above class call all instance methods by creating multiple objects.


'''

class Circle:
    PI = 3.14

    def __init__ (self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    
    def Accept(self):

        self.Radius = float(input("enter radius number :"))

        
    def CalculateArea(self):

        self.Area = Circle.PI * (self.Radius ** 2)

        

    def CalculateCircumference(self):

        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):

       print(self.Radius)
       print(self.Area)
       print(self.Circumference)


def main():
    obj1 = Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()
    



if __name__ == "__main__":
    main()





'''
Q1. Write a program which contains one class named as demo.
Demo class contains two instance variable as no1, no2.
That class contains one class variable as value.
there are two instance methods of class as fun and gun which display values of instance varaible.
Initialise instance variable in init method by accepting the values from user.

After creating the class create the two objects of demo class as
Obj1 = Demo(11,21)
Obj2 = Demo(51,101)

Now call the instance methods as

Obj1.fun()
Obj2.fun()
Obj1.Gun()
Obj2.Gun()

'''


class Demo :
    values = 0

    def __init__ (self,no1,no2):
        self.no1 = no1
        self.no2 = no2


    def fun(self):
        print("Inside fun method")
        print("firstValue: ", self.no1)
        print("secondValue: ", self.no2)
        


    def gun(self):
        print("Inside gun method")
        print("firstValue: ", self.no1)
        print("secondValue: ", self.no2)
    
def main():

    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)


    Obj1.fun()
    Obj2.fun()
    Obj1.gun()
    Obj2.gun()


if __name__ == "__main__":
    main()




    

        
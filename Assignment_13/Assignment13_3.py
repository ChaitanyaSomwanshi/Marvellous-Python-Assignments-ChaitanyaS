'''

3. Write a program which contains one class named as Numbers.
Arithmetic class contains one instance variable as Value.
Inside init method initilise that instance variable to the value which accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfct(), SumFactors(), Factors().
ChkPrime() method will return True if number is prime otherwise return False.
Factors() method will Display all factors of instance variable.
SumFactors() method will return addition of all factors. use this method in any another method as a helper method
if required.
after designing the above class call all instance methods by creating multiple objects.


'''


class Numbers:
    def __init__(self):
        self.Value = int(input("Enter Number : "))


    def ChkPrime(self):
        count = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                count = count + 1
        if count == 2:
            return True
        else:
            return False

        
        
    def ChkPerfct(self):

        if self.SumFactors() == self.Value:
            return True
        else:
            return False

        
    def SumFactors(self):
        total = 0
        for i in range(1,self.Value):
            if self.Value % i == 0:
                total = total + i

        return total


        
        
    def Factors(self):
        Data = []
        for i in range(1,self.Value + 1):
            if self.Value % i == 0:
                Data.append(i)
        
        return Data


def main():
    obj1 = Numbers()
    print(obj1.ChkPrime())
    print(obj1.Factors())
    print(obj1.SumFactors())
    print(obj1.ChkPerfct())



if __name__ == "__main__":
    main()



'''
3. Create a class Book with private attribute __price. add methods to get and set the price. show encapsulation

'''

class Book:
    def __init__(self,price):
        self.__price = price

    def getP(self):
        return self.__price

    def setP(self,Nprice):
            self.__price = Nprice
            return self.__price



def main():

    obj1 = Book(300)

    print(obj1.getP())

    print(obj1.setP(500))

if __name__ == "__main__":
    main()


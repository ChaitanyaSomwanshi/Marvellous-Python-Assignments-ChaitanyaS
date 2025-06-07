'''
2. Write a class Rectangle with length and width. Add a method to compute area and parimeter.
Area : 50, Perimeter:30

'''

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width


    def perimeter(self):
        return 2 * (self.length + self.width)

    
def main():
    obj1 = Rectangle(10,5)

    print(f" Area : {obj1.area()}, Perimeter : {obj1.perimeter()}")


if __name__ == "__main__":
    main()


'''
Q.7 Area and Perimeter of Rectangle

Accept the length and width of a Rectangle. Calculate and display the area and perimeter.
'''

def main():
    print("Enter length : ")
    length = int(input())

    print("Enter Width : ")
    Width = int(input())


    Area = length * Width
    Perimeter = 2 * (Width + length)

    print("Area is :", Area)
    print("Perimeter : ", Perimeter)


if __name__ == "__main__":
    main()

import Arithematic

# from Arithematic import *

# from Arithematic import Add, Sub, Mult, Div

# import Arithematic as A

def main():

    print("Enter First Number")
    Value1 = int(input())

    print("Enter Second Number")
    Value2 = int(input())

    Addition = Arithematic.Add(Value1, Value2)
    # Addition = Add(Value1, Value2)
    # Addition = Add(Value1, Value2)
    # Addition = A.Add(Value1, Value2)
    print("Addition of two numbers :", Addition)

    Subtraction = Arithematic.Sub(Value1, Value2)
    print("Subtraction of two numbers :", Subtraction)

    multiplication = Arithematic.Mult(Value1, Value2)
    print("multiplication of two numbers :", multiplication)

    division = Arithematic.Div(Value1, Value2)
    print("division of two numbers :", division)


if __name__ == "__main__":
    main()
   


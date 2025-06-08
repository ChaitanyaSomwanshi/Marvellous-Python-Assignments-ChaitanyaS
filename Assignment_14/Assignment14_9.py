'''

9. Create a class product with attributes name and price. Implement __eq__ method to compare two products
if they are equal in price.

'''

class Product:
    def __init__ (self,name, price):
        self.name = name
        self.price = price

    def __eq__ (self,Other):
        if isinstance(Other,Product):
            if Other.price == self.price:
                return True

        return False


def main():
    obj1 = Product("Oil",15)
    obj2 = Product("BabyOil",15)

    print( obj1 == obj2)

if __name__ == "__main__":
    main()


        
'''

9. Create a class product with attributes name and price. Implement __eq__ method to compare two products
if they are equal in price.

'''

class Product:
    def __init__ (self,name, price):
        self.name = name
        self.price = price

        
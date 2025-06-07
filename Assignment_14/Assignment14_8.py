'''
8. Create a class Vehicle with method start(). Derive class Car and override the method start() with
additional behavior. show method overriding.

'''

class Vehicle:

    def start(self):
        print("start")

class Car(Vehicle):
    def start(self):
        print("Car Started")


def main():
    obj1 = Vehicle()
    obj2 = Car()

    obj1.start()
    obj2.start()

if __name__ == "__main__":
    main()



    
'''
1. Write a program which contains one class named as BookStore.
Bookstore class contains two instance variables as Name,Author.
That class contains one class variables as NoOfBooks which is initialise to 0.
There is one instance methods of class as Display which Display Name, Author  and number of books.
Initialise instance variable in init method by accepting the values from user as name and author.
Inside init method increment value of NoofBooks by one.

after creating the class create two objects of BookStore class as
Obj1 = BookStore ("Linux System programming","Robert Love")
Obj1.Display() # Linux syayem programming by robert love. No of books : 1

Obj2 = BookStore ("C programming","Dennis Ritchie")
Obj2.Display() # C programming by Dennis Ritchie. No of books : 2


'''

class BookStore:
    NoOfBooks = 0
    def __init__ (self):
        self.Name = input("Enter Book Name :")
        self.Author = input("Enter Author Name :")
        BookStore.NoOfBooks +=  1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books : {BookStore.NoOfBooks}")

def main():
    Obj1 = BookStore()
    Obj1.Display()

    print()

    Obj2 = BookStore()
    Obj2.Display()


if __name__ == "__main__":
    main()



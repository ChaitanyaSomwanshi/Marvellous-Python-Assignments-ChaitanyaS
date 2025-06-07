'''

7. Create a base class Person with name and age. Derive a class Teacher with subject and salary.
User super() to call base class constructor and print both.

'''


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self,subject,salary,name,age):
        self.subject = subject
        self.salary = salary
        super().__init__(name,age)



def main():
    obj1 = Teacher("Python",15000,"Ramesh",23)

    print(obj1.subject)
    print(obj1.salary)
    print(obj1.name)
    print(obj1.age)


if __name__ == "__main__":
    main()


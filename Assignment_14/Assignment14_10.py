'''
10. Demonstrate private, protected and public access modifiers using a class Employee with attributes:
__salary, _department, name.

'''

class Employee:
    def __init__(self,salary,department,name):
        self.__salary = salary
        self._department = department
        self.name = name

    def Display(self):
        print(self.__salary)
        print(self._department)


def main():
    obj1 = Employee(15000,"IT","Rahul")

    #print(obj1.salary)
    #print(obj1.department)
    print(obj1.name)
    obj1.Display()

if __name__ == "__main__":
    main()

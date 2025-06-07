'''

1. Create a class Employee with attributes name, emp_id, and salary. Create objects of this class and 
print their details using a method.
Expected Output :
Name : Rohit, ID : 101, Salary : 5000


'''

class Employee:
    Name = "Rohit"
    emp_id = 101
    Salary = 50000


def main():
    obj1 = Employee()

    print(f"Name : {Employee.Name} , ID : {Employee.emp_id}, Salary : {Employee.Salary} ")



if __name__ == "__main__":
    main()

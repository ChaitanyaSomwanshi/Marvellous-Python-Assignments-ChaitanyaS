'''
4. Create a class Student with name, roll_no, and class variable school_name. print studnet details and 
school name. change the school name using class name.

'''

class Student:
    school_name = "Marvellous"
    def __init__ (self,Name,Roll_No):
        self.Name = Name
        self.Roll_No = Roll_No



    def StudentDetails(self):
        print("Name of Student : ", self.Name)
        print("Roll_No : ", self.Roll_No)
        # Student.school_name = "Marvellous New"
        print("School Name : ", Student.school_name)


def main():
    obj1 = Student("Chaitanya",33)

    obj1.StudentDetails()

    Student.school_name = "Marvellous New"

    print()

    obj1.StudentDetails()


if __name__ == "__main__":
    main()

class Person:
    roll_number = 10
    name = "Rahul"
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def display(self):
        print(self.firstname,self.lastname)
        print(self.name,self.roll_number)

    
obj  = Person("Shri","Krishan")
obj.display()

emp = Person("Ram","Chandra")
emp.display()


#count the number of objects of the class
class Student:
    count  = 0
    def __init__(self):
        Student.count = Student.count +1


obj_1 = Student()
obj_2 = Student()
obj_3 = Student()
print(Student.count)








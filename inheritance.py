# There are 4 types of inheritance in Python 
"""
1. Single Inheritance: when one class inherit the properties and methods of other class 
2. Multiple Inheritance: when one class inherit the properties and methods of more than one class 
3. Multilevel Inheritance: when 
4. Hierarchical Inheritance

"""
#Single inheritance
class Parent:
    def func_1(self):
        print("This is parent class")

class Child(Parent):
    def func_2(self):
        print("This is child class")

obj = Child()
obj.func_1()
obj.func_2()

#multiple inheritance
class Mother:
    def func_1(self):
        print("This is mother class")

class Father:
    def func_2(self):
        print("This is father class")

class Son(Mother,Father):
    def func_3(self):
        print("This is son class")

obj = Son()
obj.func_1()
obj.func_2()
obj.func_3()  

#Multilevel inheritance
class Mother:
    def func_1(self):
        print("This is mother class")

class Father(Mother):
    def func_2(self):
        print("This is father class")

class Son(Father):
    def func_3(self):
        print("This is son class")

obj = Son()
obj.func_1()
obj.func_2()
obj.func_3()  

#Hierarchical Inheritance 
class Mother:
    def func_1(self):
        print("This is mother class")

class Father(Mother):
    def func_2(self):
        print("This is father class")

class Son(Mother):
    def func_3(self):
        print("This is son class")

obj = Son()
obj.func_1()
obj.func_2()
obj.func_3()  



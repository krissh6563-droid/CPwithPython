'''Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
It describes the idea of wrapping data and the methods that work on data within one unit. 
This puts restrictions on accessing variables and methods directly and can prevent the accidental 
modification of data.'''

class Base:
    def __init__(self):
        self._a = 5


# derived class
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Protected member",self._a)


        self._a = 3
        print("Protected member after modification",self._a)

    
obj1 = Derived()
obj2 = Base()

print(obj1._a)
print(obj2._a)
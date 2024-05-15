# Python Programming
* Python is a high-level, general-purpose programming language
* It also support object oriented paradigm
* Python is dynamically typed(interpreter assigns a type to all the variables at run-time.) and garbage-collected(Garbage collection is to release memory when the object is no longer in use. ).
* Easy to use and write
* Syntax are shorter than any other programming language


# Data Structure with Python
## List 
* List is a Data Structure which is used to store multiple items in a single varialble
* List are ordered, changable and allow duplicate data items
* List can store multiple type of data in a single varialble

``` mylist = [1,"Krishna" 3.0 4,True]```

>Imortant list function

* len(mylist)
* list.append(x) - add item at the end of the list
* list.extend(iterable) - extend the list by appending all the items from the iterable
* list.insert(i,x) - add x element at ith position
* list.remove(x) - remove the x element from the list 
* list.pop(i) - pop the last element from the list
* list.clear() - remove all the items from the list 
* list.count() - return the number of element that is present in the list
* list.sort() - sort the list
* list.reverse() - reverse the element in the list
* list.copy() - make a copy of the list

## Tuple 
* Tuple is a Data Structure which is used to store multiple items in a single varialble
* List are ordered, unchangable and allow duplicate data items
* List can store multiple type of data in a single varialble

``` mytuple = (1,"Krishna" 3.0 4,True)```

## Set
* Set is a Data Structure which is used to store multiple items in a single varialble
* Set are unordered, unchangable and don't allow duplicate data items
* Set can store multiple type of data in a single varialble

``` myset = {"apple", "banana", "cherry"}```

## Dictionary
* Dictionary is a Data Structure which is used to store multiple items in a single varialble
* Dictionary items are ordered, changeable, and do not allow duplicates.
* Dictionary can store multiple type of data in a single varialble.

``` 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```

## OOPS in Python
* Object-Oriented Programming is a programming paradigm based on the concept of "objects"

### object 
 * Object is a realtime entity i.e

### class
* Blueprint of a object
* It is a logical entity

### methods
* Block of code that perform a particular task

### Inheritance 
* One class can inherit the properties and methods of another class
* In OOPS inheritance provide the idea of reusability. This meand we can add additional features to an existing class without modufying it
* Types of inheritance in python 
    1. Single Inheritance
        * When one class inherit the properties and method of another class
    2. Multiple Inheritance 
        * When a class inherit the properties and methods from two or more class
    3. Multilevel Inheritance
        * When there is child and grand child relationship between class
    4. Hierarchical Inheritance 
        * When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance
    5. Hybrid Inheritance
        * Inheritance consisting of multiple types of inheritance is called hybrid inheritance.
```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()
```

### Abstraction 
* Abstraction is used to hide the internal functionality of the function from the users.
* The users only interact with the basic implementation of the function, but inner working is hidden.
* User is familiar with that "what function does" but they don't know "how it does
* In Python, abstraction can be achieved by using abstract classes and interfaces

```
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def my_function():
        pass
    
class Person(Base):
    def my_function():
        print("This is abstract method")

```

### Polymophism
* It means having many forms
* Types of Polymorphism
    1. Compile time polymorphism or static (Method Overloading + Operator overloading)
    2. Runtime polymorphism(method overriding)
* Polymorphism is supported in Python via method overriding and operator overloading. However, Python does not support method overloading in the classic sense.

### Encapsulation
* Wrapping the data and method into a single entity is called encapsulation
* Encapsulation can be achieved by declaring the data members and methods of a class either as private or protected.
* We can declare method and variable as Protected by using single underscore ( _ ) and for Private we can use double underscore ( __ )

## Decorator 
* Decorators are a powerful and elegant feature in Python that allows you to modify or extend the behavior of functions or methods without changing their actual code
* Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

```
def outer(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@outer
def ordinary():
    print("I am ordinary function")
ordinary()
```

## Generator
* A generator in Python is a function that return an iterator using Yield keyword
```
def my_function(a,b):
    yield a
    yield b
    
result = my_function(10,20)
print(result)
print(next(result))
print(next(result))
```
* Output
```
<generator object my_function at 0x7cc7e7d0b100>
10
20
```

## Pickling 
* In Python, we sometimes need to save the object on the disk for later use. This can be done by using Python pickle
* Pickling is a way to convert a Python object (list, dictionary, etc.) into a byte stream.
* Python pickle module is used for serializing and de-serializing a Python object structure. Any object in Python can be pickled so that it can be saved on disk.






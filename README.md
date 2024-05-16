# Python Programming
* Python is a high-level, general-purpose programming language
* It also support object oriented paradigm
* Python is dynamically typed(interpreter assigns a type to all the variables at run-time.) and garbage-collected(Garbage collection is to release memory when the object is no longer in use. ).
* Easy to use and write
* Syntax are shorter than any other programming language

# Important Tricks in Python
* take multiple inputs in one line separated by space
```
arr = list(map(int,input().split()))
```

* take two input in the same line
```
a, b  = input().split()
a = int(a)
b = int(b)
print(a,b)
```

* ASCII value
```
a = 97
b = 98
A = 65
B = 66
```

* how to print ASCII value
```
print(ord('a'))
```

* how to print character from ASCII
```
print(chr(97))
```

* reversing list and string in python 
```
str = "Krishan"
arr = [1,2,3,4]
print(str[::-1])
print(arr[::-1])
```

* find max and min value 
```
print(max(2,3))  # --->3
print(min(2,3))  # --->2
arr = [2,3,1,5,6,7]
print(max(arr))
print(min(arr))
```

* Permutation and combination
```
nPr = (n!) / (n-r)!
nCr = (n!) / r!(n-r)!
```

* Convert decimal to binary
```
x = 2
print(bin(x).replace("0b",""))
```

* Convert binary to decimal
```
x = '10'
print(int(x,2))
```


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

## String 
* Collection of character is called string.
* Strings in Python are “immutable” which means they can not be changed after they are created.
* In python Strings and tuples are immutable, while lists, dictionaries, and sets are mutable.


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
![access_modifier](https://github.com/krissh6563-droid/CPwithPython/assets/56572543/4d599ea4-111d-41b3-a70b-1da991e445c7)



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
![Pickling](https://github.com/krissh6563-droid/CPwithPython/assets/56572543/c126b46b-ea36-42ad-8f41-8882c6edec1c)


## File Handling

### File Operations
* Create :- To create a file we use open() method 
```
file = open('myfile.txt', 'x')
file.close()
```
```
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
```

* Open 
```
file = open('myfile.txt', 'w')
file.close()
```

* Read 
```
f = open("demofile.txt", "r")
print(f.read())
```

* Write
```
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
```

* Close 
```
f = open("demofile.txt", "r")
print(f.readline())
f.close()
```

* Delete
```
import os
os.remove("demofile.txt")
```

* Truncate 
* Flush
* Writelines

## Exceptional Handling
* When an error occurs, or exception as we call it, Python will normally stop and generate an error message.These exceptions can be handled using the try statement
* The try block lets you test a block of code for errors.
* The except block lets you handle the error.
* The else block lets you execute code when there is no error.
* The finally block lets you execute code, regardless of the result of the try- and except blocks.
```
try:
  print(x)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")
```
![exceptional handling](https://github.com/krissh6563-droid/CPwithPython/assets/56572543/930c4ee6-af51-4935-98f5-7a32ad7bd651)

## Memory Managment
* Garbage collection is a process in which the interpreter frees up the memory when not in use to make it available for other objects.
* Assume a case where no reference is pointing to an object in memory i.e. it is not in use so, the virtual machine has a garbage collector that automatically deletes that object from the heap memory.
* Stack Memory - Reference Variable, Methods Calls
* Heap - Value Object
![memory_management](https://github.com/krissh6563-droid/CPwithPython/assets/56572543/2d0b415b-2e10-497d-9c11-294bbe9bcd81)









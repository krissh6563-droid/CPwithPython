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

### Abstraction 
* Abstraction is used to hide internal details and show only functionalities
* 

### Polymophism
* It means having many forms
* Types of Polymorphism
    1. Compile time polymorphism or static (Method Overloading + Operator overloading)
    2. Runtime polymorphism(method overriding)
* Polymorphism is supported in Python via method overriding and operator overloading. However, Python does not support method overloading in the classic sense.

### Encapsulation
* Wrapping the data and method into a single entity is called encapsulation

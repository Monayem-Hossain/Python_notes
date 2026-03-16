print('\n','Object-Oriented Programming in Python'.center(36,'-'),'\n\n')

'''
        Object-Oriented Programming (OOP) is a programming approach where programs are designed using objects and classes.
        It helps organize code in a structured, reusable and scalable way.

        Example -
          Instead of writing separate variables and functions, OOP groups data and behavior together inside objects.
'''

print("'''    1. Class and Objects    '''\n")

#  Class -
'''
        A class is a blueprint of template used to create objects.
        It defines the properties(attributes) and behaviors(methods) that objects will have.

    Example -
       class Student:
            pass
    
    Here, Student is a class
'''

#  Object -
#  An object is an instance of a class
# Example -
class Student:
    name = 'Monayem'
    age = 22

s1 = Student()
print(s1.name)
print(s1.age,'\n')
'''
    Here, 
        Student -> class
        s1 -> object created from the class
'''

print("'''    2. Attributes    '''\n")

#  Attributes are variables inside a class that store information about objects.
class Car:
    brand = 'Toyota'
    speed = 180
'''
    Attributes:
        * brand
        * speed
'''
#  Accessing attributes:
c1 = Car()
print(c1.brand,'\n')

print("'''    3. Methods    '''\n")

#     A methods is a function inside a class that defines object  behavior
#  Example -
class Car:
    def start(self): # self represents the current object.
        print('Car Started\n')
c1 = Car()
c1.start()

print("'''    4. OOP Core Concepts    '''\n")
print(" -> OOP is built on four main principles\n")
print("'''  A. Encapsulation    '''\n")
'''
    Encapsulation means restricting direct access to data and protecting it.

    Private variables are created using (__).
'''
#  Example -
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def show_balance(self):
        print(self.__balance)

acc = BankAccount(50000)
acc.show_balance()
#  Here, __balance is private.

print("'''  B. Inheritance    '''\n")
#  Inheritance allows a class to inherit properties and methods from another class

class Animal:
    def Speak(self):
        print('Animal makes sound\n')
class Dog(Animal): # Dog inherits from Animal.
    def bark(self):
        print('Dog barks\n')
    
d = Dog()
d.Speak()
d.bark()

print("'''  C. Polymorphism    '''\n")
#  Polymorphism means same method name but different behavior.

#  Example -
class Dog:
    def cound(self):
        print('Dog barks\n')
class Cat:
    def cound(self):
        print('Cat Meow\n')
    
d = Dog()
c = Cat()
c.cound()
d.cound()

print("'''  D. Abstraction    '''\n")
#  Abstraction means hiding internal details and showing only important functionality.

#  Example -
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
#  Child class:
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side
#  Usage:
s = Square(4)
print(s.area())














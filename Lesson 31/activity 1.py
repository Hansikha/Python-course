#Write a program to create a base class that consists of two functions - one to display a value, and another function is an abstract method. Next, create a subclass that consists of a method similar to the abstract method. Finally, showcase how Abstraction is being implemented in this example.

from abc import ABC, abstractmethod

class Parent:
    def display (self,x):
        print("The passed value is ", x)
    @abstractmethod
    def abs_method (self):
        print("This is an abstract method inside a parent class")

class Child(Parent):
    def abs_method (self):
        print("This is an abstract method inside a child class")

a = Child()
a.abs_method()
a.display(100)
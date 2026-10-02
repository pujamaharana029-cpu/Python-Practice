#Abstraction
"""It is used to simplifying complex systems by focusing on essential features and hiding unneccessary details.
--> It is used to define a common interface for different subclasses."""

#Abstract classes and methods
""" Abstract classes are classes that contain on one or more abstract methods.
--> A method that is defined but not implemented in the abstract class,sub classes must provide the implementation."""

from abc import ABC, abstractmethod
class Abstract(ABC): #abstract class
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def Area(self):
        pass

class Square(Abstract):
    def __init__(self,side):
        self.side=side
    def perimeter(self):
            print("I have created")
    def Area(self):
            print("I have created area")

class Circle(Abstract):
    def __init__(self,radius):
        self.radius=radius
    def perimeter(self):
        print("I have created")
    def Area(self):
        print("I have created area")
obj=Circle(7)
obj2=Square(4)



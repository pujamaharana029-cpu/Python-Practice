#Inheritance:-it allows a class(child class) to inherit properties and behaviours(attributes and methods) from another class(parent class)
"""uses of inheritance
 1. code reusability
 2.organized structure
 2.easy to maintain and extend"""

"""
class Parents: #parent class/superclass
    a="I'm an attribute inside parents"
    def mother(self):
        print("I'm a method mentioned inside Parents")
class Child(Parents): #child class/sub class
    pass
obj=Parents()
obj=Child()
print(obj.a)
print(obj2.mother())
"""

#Constructors in Inheritance

"""class Animal:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"hello your name is {self.name}")

class Human(Animal):
    def __init__(self, name,age):
        super().__init__(name) #In parent class only name is intiliased
        self.age=age
    def show(self):
        print(f"hello your name is {self.name},{self.age}")

animal1=Animal("Lion") #instance of parent class
person1=Human("amit",23) #instance of child class
person1.show()
animal1.show()
"""
#Types of Inheritance
#Single-Level Inheritance are the above examples

#Multiple inheritance
"""Two parent class and only one child class
where child class will inherit all the attributes and methods of both parents."""

"""class Animal:
    def __init__(self,name):
        pass
    
class Human:
    def __init__(self,name,age):
        pass
class Robots(Animal,Human):
    name3="Charlie123"

obj=Robots() #method resolution order(Mro)-constructor function will be inherited of the first class that have been inherited.
print(obj.name3)
"""

# Multi-level Inheritance
""" grandparent class -> parent class -> child class"""


class Factory:  #Grandparent class
    def __init__(self,materials,zips):
        self.materials=materials
        self.zips=zips

class Bhopalfactory(Factory): #parent class
    def __init__(self, materials, zips,color):
        super().__init__(materials, zips)
        self.color=color

class Punefactory(Bhopalfactory): #child class
    def __init__(self, materials, zips, color,pockets):
        super().__init__(materials, zips, color)
        self.pockets=pockets
obj=Punefactory("leather",3,"brown",2)
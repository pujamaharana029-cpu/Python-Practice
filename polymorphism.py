"""The word means many forms . In programming, it allows the same interface or method name to behave differently depending on the object or context."""
#Method overridding
"""If you have one class .i.e. parent class and another class that is child class, both class have same method name, if the object is calling the method , the child class method is called."""
"""class Animal:
    def show(self):
        print("hello I'm amit ")

class Human(Animal):
    def show(self):
        print("I'm 22 yrs ")

person1=Human() #instance of child class
person1.show()
"""
#Method Overloading doesn't exist in python.

#Duck Typing
""" If it walks like a duck and quicks like a duck, it must be duck-philosophy"""

class Animal:
    def show(self):
        print("I'm eating")
class Human:
    def show(self):
        print("I'm walking")

obj=Animal()
obj2=Human()
obj.show()
obj2.show()


#Encapsulation
"""it means putting data(variables) and code(functions) together in one place -inside a class.
it also means hiding the internal details of how things work and only showing what is needed"""
#Access modifiers in python
#1.public attributes and methods
"""Anyone can access"""
"""class Factory:
    a="pune"

    def show1(self):
        print("hello it's pune factory")

class Bhopal(Factory):
    def show(self):
        print(super().a)

obj=Bhopal()
obj.show()
"""
#Protected attributes and methods
"""naming convention to tell developers"""
"""lass Factory:
    _a="pune"

    def _show1(self):
        print("hello it's pune factory")

class Bhopal(Factory):
    def show(self):
        print(super()._a)

obj=Bhopal()
obj.show()
"""
#Private attributes and methods
"""it cannot be accessed from outside the class- only from inside the class where it is defined"""
"""class Factory:
    __a="pune"

    def __show1(self):
        print("hello it's pune factory")

obj=Factory()
print(obj.__a)
obj.__show1()""" #it canot be accessed

#to print 
"""class Factory:
    __a="pune"

    def show(self):
        print(Factory.__a)

obj=Factory()
obj.show()
"""

#DEMO EXAMPLE

class Demo:
    def __init__(self):
        self.name="public member"  #public
        self._age=21               #protected
        self.__salary=50000       #private

    def show(self):
        print("Inside the class: ")
        print("Public:", self.name)
        print("Protected:", self._age) #single underscore for protected
        print("Private:", self.__salary) #double underscore for private

obj=Demo()
obj.show()


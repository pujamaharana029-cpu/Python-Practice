#Imperative approach
"""a=12
b=13
print(a+b)"""
#Functional approach
"""def addition(a,b):
    return a+b
print (addition(13,12))
print(addition(24,67))"""
#Object-oriented programming(OOPs)approach
#1.classes in oops
"""A classes is an blueprint or template  for creating objects.
there are two types inside a class are attributes and methods."""
"""class Factory:
    a=12 #attribute

    def hello(): #method
        print("how are you")
    print("hello how are you ")
print(Factory().a)
Factory.hello()"""
#2.objects
"""class Factory:
    a=12 #attribute
    def hello(self): #method
        print("how are you")

obj=Factory() #object created
# many objects can be created
print(obj.a)
obj.hello()"""

#3.Constructors
"""A constructor is a method that runs automatically when we call a class and the constructor function will target the objects location"""
"""class Factory:
    def __init__(self,materials,zips,pockets): #initialisation function-self is parameter,where it target the location of reebok and campus
        self.materials=materials
        self.zips=zips
        self.pockets=pockets

    def show(self):
        print(f"Your materials are:- {self.materials}, {self.zips}, {self.pockets}")


reebok=Factory("leathers",3,2) #object=classname() :- object is created
campus=Factory("Nylon",3,4)
print(reebok.pockets)
print(campus.materials)
reebok.show()
campus.show()"""

#4.Attributes and Methods
class Animal():
    name="lion" #normal attribute/class attribute

    def __init__(self,age): #self keyword targets the location of object
        self.age= age #instance attribute

    def show(self): #instance method
        print(f"my age is:- {self.age}")

    @classmethod
    def hello(cls): #class method-decorated method
        print("hello brother")

    @staticmethod
    def static():
        print("I'm okay")
obj=Animal(12)
obj.show()
obj.hello()
obj.static()

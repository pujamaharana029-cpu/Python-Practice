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

#Constructors
"""A constructor is a method that runs automatically when we call a class and the constructor function will target the objects location"""
class Factory:
    def __init__(self,materials,zips,pockets): #initialisation function-self is parameter,where it target the location
        self.materials=materials
        self.zips=zips
        self.pockets=pockets

reebok=Factory("leathers",3,2)
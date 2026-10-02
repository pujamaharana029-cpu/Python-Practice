#1.Decorator
""" It is just a function that modifies another function without changing its actual code."""
'''class Animal:
    @property
    def show(self):
        print("I'm good")
obj=Animal()
obj.show'''

#example decorate

"""def decorate(func):
    def wrapper():
        print("I will print myself before function")
        func()
        print("I will print after the function")
    return wrapper

@decorate
def hello():
    print("hello I'm amit")
hello()"""


#addition example
"""def decorate(func):
    def wrapper(a,b): # wrapper catches how many parameters and  aguements are given
        print("the addition to your numbers are :")
        func(a,b)
        print(" thank you I hope you liked it")
    return wrapper

@decorate
def addition(a,b):
    print(f"your total is : {a+b}")
addition(3,5)"""

# 2. Args and Kwargs
""" They are special keywords in python used in function definitions to accept a flexible number of arguments"""
#args
"""def addition(*a):
    sum=0
    for i in a:
        sum+=i
    print(sum)
addition(12,14,13,15,16,17)"""

#kwargs-keyword arguments
"""def information(**kwargs):
    print("your information is\n\n")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")
information(name= "Amit", age=34, desination="AI/ML")
"""
#3.comprehension
'''Ternary operator'''
a=12
print("even") if a%2==0 else print("odd")

#List , Dictionary and set comprehension
""" All of these comprehensions  is used to create lists, dictionaries and set. but you don't have to write nultiple lines of code for loops and if-else statements"""
l=[i for i in range(1,21) if i%2==0]
print(l)   #list comprehension

d={ i:i**2 for i in range(1,10)}
print(d)       #dictionary comprehension



#4. Lambda functions
"--> A lambda function is an anonymous, infinite function using lambda keyword. ofen used only once temporily"
"""Even_odd=lambda a: "even" if a%2==0 else "odd"
print(Even_odd(12))"""

#5. Map filter
" Map is used for applying a function to multiple times."
"""a=[1,2,3,4,5,6,7]
result=map(lambda x:x**2,a)
print(list(result))"""

"""a=[1,2,3,4,5]
def double(x):
    return x*2
result=map(double,a)
print(list(result))"""

" Filter as the name suggest is used to filter out the stuff"
"""b=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def even(x):
    if x %2==0:
        return True
    else:
        return False   
result=filter(even,b)   #result=filter(lambda x:True if x%2==0 else False, a)
print(list(result))"""

#5. Modules and packages
import Maths
print(Maths.addition(12,12))  #Modules built-in

#package-folder 
from Model.models import hello
print(hello.hello())
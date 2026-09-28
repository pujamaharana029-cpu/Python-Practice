#Errors
"""Errors occur when the program is syntactically correct but the code is not able to execute properly. 
Errors can be of two types: Compile time errors and Runtime errors."""
#print("hello world" - syntax error
"""a=12
if a>10:
print("a is greater than 10")""" #Indentation error

#Exceptions
"""exceptions are errors that occur during the execution of a program. They can be handled using try-except blocks to prevent the program from crashing.
exceptions are unexpected events or errors that occurs during the execution of a program which disrupts the normal flow of the program"""
'''a=int(input("tell a number:"))
print(10/a)''' #ZeroDivisionError-divisible by zero

#Exception handling-keywords
""" Try, except, else, finally, raise"""
"""a=int(input("tell a number:"))
try:  #Try statement must have at least one except or finally clause
    print(10/a)
except Exception as err:
    print(f"sorry there is an err as {err}")
else:
    print("good there is an exception")
finally:
    print("I will run no matter what")
print("division done")"""

#raise: manually throw an exception
age=int(input("tell your age: "))
try:
    if age<10 or age>18:
        raise ValueError("your age must be between 10 and 18") #error is raised by the user itself
    else:
        print("welcome to the club")
except Exception as err:
    print(f"an error occured as {err}")
print("the club will start soon")
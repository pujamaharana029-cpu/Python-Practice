#User defined function
"""def greet(): # function is a block of code that can be executed by calling the function name.
    print("hello")
greet()"""

#functions parameters and arguments
'''The thing which you accept-parameters
the thing you provide to parameters-arguement'''
#positional arguments
"""def sum(a,b): #parameter
    print(f"The sum of your numbers is{a+b}")
sum(12,13) #arguement
sum(44,45)"""

#Types of arguments
#keyword argument 
"""def hello(name,age):
    print(f"your name is {name} and your age is {age}")
hello(age=22,name="akarsh") #keyword argument """

#default argument
"""def sum(a,b=45):
    print(f"sum is{a+b}")
sum(2,32) """

#Wap to check whether the string is palindrome or not using function
"""def palindrome(str):
    rev=""
    for i in range(len(str)-1,-1,-1):
        rev+=str[i]
    if rev==str:
        print("palindrome")
    else:
        print("not a palindrome")
str=input("enter a string : ")
palindrome(str) """

#return statement
def hello():
    return "hello"
print(hello())

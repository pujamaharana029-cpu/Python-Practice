#Let's print a table of 5
'''n=int(input("enter which table you want:"))
for i in range(n,n*10+1,n):{
    print(i)
}'''
#string
'''a="CODERS learns coding fast"
print(len(a))
for i in range(len(a)):
    print(a[i])
for i in a: #simple direct iteration
    print(i)'''

#Accept an integer and print hello world n times.
"""n=int(input("enter an integer:"))
for i in range(n):
    print("Hello world")"""

#Print natural number up to n
"""n=int(input("enter an integer:"))
for i in range(1,n+1):
    print(i)"""

#Reverse for loop.print n to 1
"""n=int(input("enter an integer:"))
for i in range(n,0,-1):
    print(i)"""

# print a table
"""n=int(input("which table you want:"))
for i in range(1,11):{
    print(f"{n} * {i} ={n*i}")
}"""

#sum up to n terms
"""sum=0
n=int(input("enter a number:"))
for i in range(1,n+1):
    sum+=i
print(sum)"""

#factorial of n
"""fact=1
n=int(input("enter a number:"))
for i in range(1,n+1):
    fact*=i
print(fact)"""

#print the sum of all even and odd numbers in a range seperately
"""even=0
odd=0
n=int(input("enter a number"))
for i in range(0,n+1):
    if(i%2==0):
      even+=i
    else:
     odd+=i
print(f"sum of even and odd numbers are{even},{odd}")"""

#print all the factors of a number
"""n=int(input("enter a number"))
for i in range(1,n+1):
    if(n%i==0):
        print(i)"""

#Accept a number and check if it is a perfect number or not
#a number whose sum of factors is equal to the number itself
"""sum=0
n=int(input("enter a number"))
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(sum==n):
    print("number is a perfect")
else:
    print("number is not perfect")"""

#check the number is prime or not
"""count=0
n=int(input("enter a number:"))
for i in range(1,n+1):
    if(n%i==0):
      count+=1
print(count)
if(count==2):
   print("it is a prime number")
else:
   print("it is not a prime number")"""

#reverse a string without using in build functions
"""a="Coders"
for i in range(len(a)-1,-1,-1):
    print(a[i])"""

#check the string is palindrome or not
"""str=input("enter a string:")
reverse=""
for i in range(len(str)-1,-1,-1):
    reverse+=str[i]
if(reverse==str):
    print("it is palindrome")
else:
    print("it is not a palindrome")"""

#count all letters, digits and special symbols from a given string
"""a=input("enter a string:")
char=0 #letters count
dig=0 #digit count
spchr=0 #special character
for i in a:
    if i.isdigit(): #string methods are used
        dig+=1
    elif i.isalpha():
        char+=1
    else:
        spchr+=1
print(f"your digits are{dig}\nyour alphabets are{char}\nyour special character are{spchr}")"""

#USING While loop solve the questions
#Separate each digit of a number and print it on the new line
"""a=int(input("enter a number:"))
while(a>0):
    print(a%10)
    a//=10"""

#Accept a number and print its reverse
"""rev=0
n=int(input("enter a number:"))
while(n>0):
    rev=rev*10+n%10
    n//=10
print(rev)"""

#Accept a number and check if it is a palindromic number
rev=0
n=int(input("enter a number:"))
original_number=n
while(n>0):
    rev=rev*10+n%10
    n//=10
if(rev==original_number):
    print("it is an palindromic number")
else:
    print("it is not a palindromic number")

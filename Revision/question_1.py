#User will input(3 ages).find the oldest one
"""a=int(input("Enter the first age: "))
b=int(input("Enter the second age: "))
c=int(input("Enter the third age: "))
if a>b and a>c:
    print("the oldest age is:a", a)
elif b>a and b>c:
    print("the oldest age is:b", b)
else:
    print("the oldest age is:c", c) """

#wap  that will take user input cost price and selling priceand determines whether it is loss or a profit.
"""cp=float(input("enter cost price: "))
sp=float(input("enter selling price: "))
if(cp>sp):
    print("loss")
elif sp>cp:
    print("profit")
else:
    print(" no profit and no loss")"""

#wap to find simple interest when the value of principle,rate of interest and time period is given.
"""p=float(input("enter principle rate: "))
r=float(input("enter rate of interest: "))
t=float(input("enter the time period: "))
SI=(p*t*r)/100
print("simple interest=",SI)"""

#wap to find the volume of the cylinder.also find the cost when ,when the cost of litre milk is 40rs
"""import math
r=int(input("enter radius: "))
h=int(input("enter height: "))
volume=math.pi*r**2*h
litres=volume/1000
cost=litres*40
print("total cost of milk in litres is: ",cost)"""

#wap that will tell whether the given number is divisible by 3 and 6
num=int(input("enter a number: "))
if(num%3==0 and num%6==0):
    print("number is divisible by 3 and 6")
else:
    print("not divisible by 3 and 6")
#write a program that will convert celsius value to fahrenheit
"""c=int(input("enter temperature in celsius: "))
f=(c*(9/5))+32
print("the temperature in celsius converts into faherheit: ",f,"f")
"""
#wap that will tell whether the number entered by the user is odd or even
"""n=int(input("enter a number: "))
if(n%2==0):
    print("even")
else:
    print("odd")"""

#wap  that will tell whether the number the given year is a leap year or not
"""year=int(input("enter a year: "))
if(year%100==0) and (year%400==0):
    print("it's a leap year")
elif(year%100!=0) and (year%4==0):
    print("it's leap year")
else:
    print("it's a normal year")"""

#wap to find euclidean distance between two coordinates
"""import math
x1=float(input("enter x1: "))
x2=float(input("enter x2: "))
y1=float(input("enter y1: "))
y2=float(input("enter y2: "))
distance=math.sqrt((x2-x1)**2 +(y2-y1)**2)
print("Euclidean distance = ",distance)
"""
#wap take user input three angle and chcek whether it can form triangle or not
a=int(input("enter first angle: "))
b=int(input("enter second angle: "))
c=int(input("enter third angle: "))
sum=a+b+c
if(sum==180):
    print("it forms a triangle")
else:
    print("it cannot form a triangle")
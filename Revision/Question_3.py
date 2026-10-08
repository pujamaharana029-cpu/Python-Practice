#user will input (2 numbers).write a program to swap the numbers.
"""a= int(input("enter the first number: "))
b=int(input("enter the second number: "))
print("before swapping the numbers are", a,"and",b)
temp =a
a=b
b=temp
print("after swapping the numbers are",a,"and",b)
"""

#write a program that will gives you the sum of three digits.
"""num=int(input("enter a 3 digit number: "))
sum=(num%10)+(num//10)%10+(num//100) #(144%10)+(144//10)%10 +144//100
print("sum of three digit number is: ",sum) # 4+4+1=9
"""
#wap that will reverse of a four digit number .also it check whether the reverse is true
num=int(input("enter 4 digit number: "))
reverse=0
original=num
while(num!=0):
    digit=num%10
    reverse=reverse*10+digit
    num//=10
print("reverse of 4 digit number is :",reverse)
if(original==reverse):
    print("reverse is same")
else:
    print("reverse is not same")


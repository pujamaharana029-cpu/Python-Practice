#wap to find compound interest
"""p=float(input("enter principle rate: "))
r=float(input("enter rate of interest: "))
t=float(input("enter the time period: "))
Amount=p*(1+r/100)**t
ci=Amount-p
print("compoud interest: ",ci)
print("Total amount: ", Amount)
"""

#print all factors of a given number provided by the user
"""num=int(input("Enter a number: "))
for i in range(1,num+1):
    if num%i==0:
        print(i)"""

#find the reverse of a number
num=int(input("Enter a number: "))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num//=10
print("Reverse of the number: ", reverse)
#Accept the gender from the user as char and print the respective greeting message
'''gen=input("enter your gender as character(M or F):")
if(gen=='M' or gen=='m'):{
    print("Good morning Sir")
}
elif(gen=='F' or gen=='f'):
    print("Good morning Mam")
else:
    print("Unidentified gender")'''

#Accept an integer and check whether it is an even or odd number
'''num=int(input("enter an integer:"))
if(num%2==0):
    print(f"{num} is even number")
else:
    print(f"{num}is odd number")'''

#Accept name and age from the user.check if the user is a valid voter or not
'''name=input("enter your name:")
age=int(input("enter your age:"))
if(age>=18):
    print(f"Hello {name}! you are eligible for vote")
else:
    print(f" Hello {name}! you are not eligible for vote")'''

#Accept a year and check if it is a leap year or not
'''Century year are divided by 400 if not century year then divided by 4'''
'''year=int(input("tell your year:"))
if(year%100==0 and year%400 ==0):
    print("its  a leap year")
elif (year%100!=0 and year%4==0):
    print("its leap year")
else:
    print("its a normal year")'''

#If-elif ladder question
temp=int(input("enter the temperature in c:"))
if(temp<0):
    print("Freezing cold")
elif(temp==0 and temp<10):
    print("very cold")
elif(temp>=10 and temp<20):
    print("cold")
elif(temp>=20 and temp<30):
    print("pleasant")
elif(temp>=30 and temp<40):
    print("hot")
else:
    print("very hot")
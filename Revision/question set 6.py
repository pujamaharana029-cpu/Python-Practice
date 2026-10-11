#wap to find compound interest
p=float(input("enter principle rate: "))
r=float(input("enter rate of interest: "))
t=float(input("enter the time period: "))
Amount=p*(1+r/100)**t
ci=Amount-p
print("compoud interest: ",ci)
print("Total amount: ", Amount)
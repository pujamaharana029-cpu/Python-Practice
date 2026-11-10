#hollow square
"""n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()"""

#right -aligned triangle
"""n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i+1):
        print(k,end="")
    print()
"""
#floyd's triangle
n=5
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()
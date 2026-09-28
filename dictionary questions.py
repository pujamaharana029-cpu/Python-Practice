#write a python script to merge two python dictionaries.
"""d1={"a": 1, "b": 2}
d2={"c": 3, "d": 4}
for i in d2:
    d1[i]=d2[i]
print(d1)"""

#write a python program to sum all the values in a dictionary
"""sum=0
d={"a": 1, "b": 2, "c": 3, "d": 4}
for i in d:
    sum+=d[i]
print(sum)"""

#count the frequency of each elements-usecase of dictionary
"""a=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,2,1,9,2]
d={}
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)"""

#write a python program to continue two dictionary by adding values for common keys.
d1={10:100, 20:200, 30:150}
d2={30:150, 40:400, 50:500}
for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]
print(d1)

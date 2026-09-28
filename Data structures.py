# Data structure:data is stored in structured way
"""built-in data structures:- list, tuple, dictionary, set.
Custom data structures:- stack,queue,linked list, graph."""

#List
"""Mutable,duplicates,ordered sequence,heterogenous"""
#a=[12,13,16,17,12]
"""fruits=["apple","cherry","mango"]
b=["a","b",1,2,print(),True]
print(a[0])
print(fruits[2])
print(b[0:5])
"""
#List traversing and methods
"""1st way using index"""
"""for i in range(len(a)):
    print(a[i])"""

"""2nd way directly on values"""
"""for i in a:
    print(i)"""

"""print(dir(list)) """#Methods of list
"""a.append(4) #add an item to the end
a.insert(2,14) #insert 14 at index 2
a.extend([18,19,20]) # Add multiple elements at the end
a.remove(12)#remove the first occurence of 12
a.pop(3) #removes and stores the element at index 3
a.count(12)
a[2]=15
print(a)"""

#tuple
"""Immutable,duplicates,parenthesis,ordered,heterogeneous"""
"""a=(2,5,7,3,9,2,10,2,11)
# a[0]=12 cannot change value -immutable
print(a[0])"""

#Tuple Traversing and methods
"""for i in range(len(a)):
    print(a[i])
#index method
index=a.index(7)
print(index)
#count method
count=a.count(2)
print(count)"""

#tuple unpacking
"""a,b,c,d=(1,2,3,4)
print(c)
a=(1)
print(type(a)) #output-integer"""

#Set
"""mutable,no duplicates,unordered,semi-heterogeneous,curly bracket ,no indexing """
"""s={1,2,4,5,56,2,5,"hello",23,"world"}
a=12
c=hash((1,2,4,6))
b=hash("hello")
print(c)

for i in s:
    print(i)"""

#set methods
"""a={3,8,5,1}
a.add(4) #add elemnt
a.remove(5) #remove element
a.discard(3)#same as remove element
a.pop() #removes a random element
a.clear()#removes all elements
print(a)
b={9,4,2,6}
Union_set=a.union(b) #a|b
intersection_set=a.intersection(b) #a&b
difference_set=a.difference(b) #a-b
symetric_diff=a.symmetric_difference(b) #a^b
print(Union_set)
print(intersection_set)
print(difference_set)
print(symetric_diff)
"""
#dictionary
"""semi-mutable:-key cannot be changed but value can be,no duplicates,unordered,curly bracket,key-value pair"""
"""d={1:"apple",2:"banana",3:"cherry"}
d[1]=1000 #values can be changed-updating
d.update({4:"200"}) #adding new key-value pair-creating
del d[2] #deleting key-value pair
print(d) #accessing value using key

#dictionary traversing and methods
for i in d:
    print(d[i]) #accessing value using key"""

#help(dict) #methods of dictionary
"""d.clear() #removes all key-value pairs
d.copy()
d.get(2) #returns the value for the specified key
print(d) #returns the value for the specified key"""

#deep copy:-creates a new object and copies all the values of the original object to the new object.
a=[1,2,3,4]
b=a
b[0]=100
print(a) #output-[100,2,3,4]

#shallow copy:-creates a new object but does not create copies of nested objects, instead it references the original nested objects.
a=[1,2,3,4]
b=a.copy()
b[0]=100
print(a) #output-[1,2,3,4] 
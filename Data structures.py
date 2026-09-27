# Data structure:data is stored in structured way
"""built-in data structures:- list, tuple, dictionary, set.
Custom data structures:- stack,queue,linked list, graph."""

#List
"""Mutable,duplicates,ordered sequence,heterogenous"""
a=[12,13,16,17,12]
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
a.append(4) #add an item to the end
a.insert(2,14) #insert 14 at index 2
a.extend([18,19,20]) # Add multiple elements at the end
a.remove(12)#remove the first occurence of 12
a.pop(3) #removes and stores the element at index 3
a.count(12)
a[2]=15
print(a)


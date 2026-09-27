# Print positive and negative elements of a list
"""l=[1,3,-2,5,6,-6,7,-10,2,-11]
print("postive elements are:")
for i in l:
    if i>=0:
        print(i)
print("negative numbers are")
for i in l:
    if i<0:
        print(i)"""

#Mean of List elements
"""l=[1,3,5,7,9,11,13]
mean=0
for i in l:
    mean+=i/len(l)
print(f"Mean of list elements are {mean}")"""

#Find the greatest element and print its index too
"""l=[3,12,89,11,20,1]
largest=l[0]
for i in range(len(l)):
    if(l[i]>largest):
        largest=l[i] 
        index=i
print(f"The largest number in list is {largest} at index {index}")
"""
#Find the second largest element
"""l=[3,4,7,12,34,90,76,45,32,8]
largest=l[0]
second_largest=l[0]
for i in range(len(l)):
    if(l[i]>largest):
        second_largest=largest
        largest=l[i]
    elif l[i]>second_largest and l[i] !=largest:
        second_largest=l[i]
print(f"The second largest number is{second_largest}")"""

#Check if list is sorted or not
l=[1,6,7,3,4,5,2,9,8]
#l=[1,2,3,4,5,6,7]
for i in range(len(l)-1):
    if(l[i]<l[i+1]):
        continue
    else:
        print("list is not sorted")
        break
else:
    print("your list is sorted")
# Write a Python program to find the common elements between two lists.

l1 = [1,2,3,4,5,6,8,8]
l2 = [854,6,466,456,68,4,465,1,23,2,3]
l3 = []
for element in l1:
    if element in l2:
        l3.append(element)
print(l3)
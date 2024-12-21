# using + oprator

# list1 = [1,2,3]
# list2 = [4,5,6]

# final_list = list1 + list2
# print(final_list)



# using extend function
"""
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)  
print(list1)
"""




# Using append() finction
"""
list1 = [1, 2, 3]
list2 = [4, 5, 6]

for i in list2:
    list1.append(i) 
print(list1)

"""


# usign function

def add_list(list1, list2):
    final_list = list1 + list2
    return final_list

list1 = list(input("Enter the list1: ").split())
list2 = list(input("Enter the list2: ").split())

result = add_list(list1, list2)
print(result)


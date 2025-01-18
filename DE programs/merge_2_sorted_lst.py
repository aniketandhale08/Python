# Write a program to merge two sorted lists into one sorted list.


# Using sort
"""
lst1 = [1,3,5,9,7,5,36,4,6,4]
lst2 = [4,6,8,8,9,5,4,2,6,4,4]

lst1.sort()
lst2.sort()

merged_lst = lst1+lst2

merged_lst.sort()

print(merged_lst)

"""



# using sorted

"""
lst1 = [1,3,5,9,7,5,36,4,6,4]
lst2 = [4,6,8,8,9,5,4,2,6,4,4]

sorted_lst1 = sorted(lst1)
sorted_lst2 = sorted(lst2)

merged_lst = sorted_lst1+sorted_lst2

final_lst = sorted(merged_lst)

print(final_lst)

"""


# using fun


def mer_sor_lst(lst1, lst2):
    sorted_lst1 = sorted(lst1)
    sorted_lst2 = sorted(lst2)

    merged_lst = sorted_lst1+sorted_lst2

    final_lst = sorted(merged_lst)
    return final_lst


lists1= list(map(int,input("Enter the lst1: ").split()))
lists2= list(map(int,input("Enter the lst2: ").split()))

result = mer_sor_lst(lists1 , lists2)
print(result)









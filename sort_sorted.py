"""

1. sorted(): 
Returns a new sorted list from any iterable (like lists, tuples, dictionaries, etc.) without modifying the original.
Can be used on any iterable (lists, tuples, strings, etc.).
sorted(iterable, key=None, reverse=False)

2. sort(): 
Sorts the list in place, meaning it modifies the original list and does not return anything (returns None).
Can only be used on lists.
list.sort(key=None, reverse=False)

in nutshell:
In Python, the list.sort() method does not return a new list. Instead, it modifies the original list in place and returns None.

"""

# # sorted preserve the orijinal list
list2 = [6,65,79,1,9,8,85,15,262,10,5]
new_list = sorted(list2)
print(new_list)
print(list2)





# sort change the orijinal list

# list2 = [6,65,79,1,9,8,85,15,262,10,5]
# fianl_list = list2.sort()
# print(fianl_list)

# if you still want to use sort() and want to print the list then,

# list2 = [6, 65, 79, 1, 9, 8, 85, 15, 262, 10, 5]
# list2.sort() 
# print(list2)  









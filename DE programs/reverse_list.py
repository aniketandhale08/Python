# Write a Python program to reverse a list without using the built-in reverse method.

def reverse_lst(lst):
    reverse_lst = []
    for i in range(len(lst)-1, -1, -1):
        reverse_lst.append(lst[i])
    return reverse_lst

lst= [1,2,3,4,5]
print(reverse_lst(lst))
# Write a Python program to find all the even numbers in a given list.

def even_lst(lst):
    even_list = []
    for i in lst:
        if i%2 ==0:
            even_list.append(i)
    return even_list

lst = [1,2,3,4,5,6,7,8,9,10]
print(even_lst(lst))
# Write a Python program to find the largest number in a list without using the max() function.

def largest_num(lst):
    largest_num = lst[0]
    for num in lst:
        if num > largest_num:
            largest_num = num
    return largest_num

list1 = [1,2,3,4,5]
print(largest_num(list1))
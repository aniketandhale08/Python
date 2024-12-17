# Method 1
"""
my_array = [1,2,3,4,5,6,7,8,9,10]

largest_element = my_array[0]

for i in my_array:
    if i > largest_element:
        largest_element = i
print(largest_element)

"""


# Method 2

def find_largest_element(my_array):
    largest_element = arr1[0]

    for i in my_array:
        if i > largest_element:
            largest_element = i
    return largest_element

arr1 = [1,1]
example1 = find_largest_element(arr1)
print(example1)
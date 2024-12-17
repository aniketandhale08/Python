# Method 1

# my_array = [1,2,3,4,5,6,7,8,9,10]
# print(sum(my_array))




# Method 2

# my_array = [1,2,3,4,5,6,7,8,9,10]
# total_sum = 0
# for i in my_array:
#     total_sum = total_sum + i
# print(total_sum)





# Method 3

def sum_of_array(my_array):
    total = 0
    for i in my_array:
        total = total + i
    return total

arr = [1,2,3]
example = sum_of_array(arr)
print(example)
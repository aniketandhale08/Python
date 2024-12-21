# my_list = [4,2,6,8,5,9,7,55,62,100]
# print(min(my_list))



my_list = [4,2,6,8,5,9,7,55,62,100]

min_num = my_list[0]

for i in my_list:
    if i < min_num:
        min_num = i
print(min_num)
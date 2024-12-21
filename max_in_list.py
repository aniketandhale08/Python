# my_list = [4,2,6,8,5,9,7,55,62,100]

# print(max(my_list))

my_list = [4,2,6,8,5,100,9,7,55,62,5,6,1]

max_num = my_list[0]

for i in my_list:
    if i > max_num:
        max_num = i
print(max_num)
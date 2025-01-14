def remove_duplicate(lst):
    unique_lst = []
    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)
    return unique_lst

list = [1,2,3,4,5,5,5,5]
print("unique_list is: ", remove_duplicate(list))
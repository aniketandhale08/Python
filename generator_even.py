"""A generator in Python is a special type of iterator that allows you to create an iterable sequence of values, 
but unlike a list, it generates the values lazily one by one, only when required. 
This makes generators memory efficient because they don't store the entire sequence in memory at once."""


# num = int(input("Enter the num how many even num you want: "))

# for i in range(2, num+1, 2):
#     print(i)



# num = int(input("Enter how many even numbers you want: "))
# count = 0
# i = 2
# while count < num:
#     if i % 2 == 0:  
#         print(i)
#         count += 1
#     i += 1 




# def even(num):
#     for i in range(1, num+1):
#         print(2 * i)

# num = int(input("Enter how many even numbers you want: "))
# even(num)



def even_numbers(n):
    i = 2
    count = 0
    while count < n:
        yield i
        i += 2
        count += 1

n = int(input("Enter how many even numbers you want: "))
gen = even_numbers(n)

for num in gen:
    print(num)




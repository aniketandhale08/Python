# Write a Python program to find the sum of digits of a given number.

def sum_of_dig(num):
    total = 0
    while num > 0:
        total += num%10 
        num = num // 10
    return total

num = 123
print(sum_of_dig(num))
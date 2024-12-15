# Method 1

"""
num = int(input("Enter the num till which you want to calculate the sum of cubes: "))

if num <=0:
    print("Enter the positive num!")
else:
    sum = 0
    for i in range(1, num+1):
        calc_cube = i**3
        sum = sum + calc_cube
    print(sum)

"""


# Method 2

def calculate_cube_sum(n):
    if n <=0:
        return 0
    else:
        total = sum(i**3 for i in range(1, n+1))
        return total

n = int(input("Enter the n: "))

if n<=0:
    print("Enter the positive num!")
else:
    result = calculate_cube_sum(n)
    print(f"The sum of {n} cubes is {result}")












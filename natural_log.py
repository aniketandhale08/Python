import math

num= float(input("Enter the num: "))\

if num <=0:
    print("Enter the positive num!")
else:
    result = math.log(num)

    print(f"The natural log of {num} is {result}")
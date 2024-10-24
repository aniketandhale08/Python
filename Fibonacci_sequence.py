# Method 1

limit = int(input("Enter the limit for Fibonacci series: "))

a, b = 0, 1
fibonacci_series = []
while a <= limit:
    fibonacci_series.append(a)
    a, b = b, a + b
print(f"The Fibonacci series up to {limit} is: {fibonacci_series}")



# Method 2

n = int(input("Enter the limit for Fibonacci series: "))

a, b = 0, 1
print(a, end=" ")
for i in range(1, n):
    print(b, end=" ")
    a, b = b, a + b  


# Method 3

n = int(input("Enter the limit for Fibonacci series: "))
num1 = 0
num2 = 1
next_number = num2  
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()
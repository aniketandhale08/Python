limit = int(input("Enter the limit to which you want to sum up the num: "))

sum = 0
for i in range(1, limit+1):
    sum = sum + i
print(f"The sum of numbers up to {limit} is {sum}")
num = int(input("Enter the num to check: "))

sum = 0
order = len(str(num))
copy_num = num

while(num > 0):
    digit = num % 10
    sum += digit**order
    num = num//10

if (sum == copy_num):
    print(f"{copy_num} is armstrong number!")
else:
    print(f"{copy_num} is not armstrong number!")
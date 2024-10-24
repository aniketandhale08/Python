low = int(input("Enter the num: "))
high = int(input("Enter the num: "))

for num in range(low, high+1):
    order = len(str(num))
    copy_num = num
    sum = 0

    while copy_num > 0:
        digit = copy_num % 10
        sum += digit**order
        copy_num = copy_num // 10

    if num == sum:
        print(num)
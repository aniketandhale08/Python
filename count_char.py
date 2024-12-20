my_str = str(input("Enter the string: "))
characher = str(input("Enter the characher: "))

count = 0

for i in my_str:
    if i == characher:
        count+=1
print(count)
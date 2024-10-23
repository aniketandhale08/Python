num = int(input("Enter the num for which you want to print the table: "))

if num==0:
    print("The table of 0 doesn't exist")
else:
    for i in range(1,11):
        # print(f"{num} x {i} == {num*i}")
        print(num*i)
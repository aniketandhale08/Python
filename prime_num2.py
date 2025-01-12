## Check the prime num

# num = int(input("Enter the num: "))
# if num < 2:
#     print("Not prime")
# else:
#     for i in range(2,num):
#         if num%i == 0:
#             print("Not prime")
#             break
#     else:
#         print("Prime")




## print this much of prime num 

num = int(input("How many prime numbers do you want: "))
count = 0
num_to_check = 2

while count < num:
    for i in range(2, num_to_check):
        if num_to_check % i == 0:
            break
    else:
        print(num_to_check)
        count += 1
    num_to_check += 1

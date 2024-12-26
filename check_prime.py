# A prime number is a special number that can only be divided evenly by 1 and itself, means it only have 2 divisors!

import math

def isprime(n):
    if n<=1:
        return "Not prime!"
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i ==0:
            return "Not prime!"
    else:
        return "It's Prime!"
    
num = int(input("Enter the num: "))
num = int(input("Enter the num: "))
print(isprime(num))
        


# import math

# num = int(input("Enter the num: "))
# if num <= 1:
#     print("Not Prime!")
# else:
#     for i in range(2, int(math.sqrt(num)+1)):
#         if num % i == 0:
#             print("Not Prime!")
#             break
#     else:
#         print("Prime!")






        
    
















# usign lambda

fact = lambda n: 1 if n ==0 else n*fact(n-1)
print(fact(4))


# Other implemetation using fucntion, not lambda

# num = int(input("Enter the num: "))
# fact = 1
# for i in range(1, num+1):
#     fact= fact*i
# print(fact)



# def factorial(num):
#     if num == 0 or  num == 1:
#         return 1
#     return num*factorial(num - 1)
# print(factorial(4))
    


# def calculate_factorial():
#     num = int(input("Enter a number: "))  
#     fact = 1
#     for i in range(1, num + 1): 
#         fact *= i
#     return fact  
# result = calculate_factorial()
# print(f"The factorial is: {result}")


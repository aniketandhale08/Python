num = int(input("Enter the num: "))

fact = 1
if num < 0:
    print("Factorial not exist for negrative numbers!")
else:
    for i in range(1, num+1):
        fact = fact*i
    print(f"Factorial of {num} is {fact}!")




'''
Example 
num = 5
5! = 5*4*3*2*1 = 25

'''
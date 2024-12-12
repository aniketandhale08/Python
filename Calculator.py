# Method 1
"""
operation = int(input("Enter the opration that you want to perform: ")) 

num1 = int(input("Enter teh first num: "))
num2 = int(input("Enter teh second num: "))

if operation == 1:
    add = num1 + num2
    print(add)
elif operation == 2:
    sub = num1 - num2
    print(sub)
elif operation == 3:
    mul = num1 * num2
    print(mul)
elif operation == 4:
    div = num1 / num2
    print(div)
else:
    print("Invalid input")

"""

# Method 2

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y


print("Enter the opration which you want to perform:"
      "\nAddition: 1"
      "\nSubtraction: 2"
      "\nMultiplication: 3"
      "\nDivision: 4")


while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ("1", "2", "3", "4"):
        try:
            num1 = int(input("Enter teh first num: "))
            num2 = int(input("Enter teh second num: "))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue

        if choice == "1":
            print("Your addition is: ", add(num1, num2))
        elif choice == "2":
            print("Your subtraction is: ", sub(num1, num2))
        elif choice == "3":
            print("Your multiplication is: ", mul(num1, num2))
        elif choice == "4":
            print("Your division is: ", div(num1, num2))
        
        next_calculation = input("Let's go for the next calculation? (Yes/No)\n")
        if next_calculation == "No":
            break
    else:
        print("Invalid input")
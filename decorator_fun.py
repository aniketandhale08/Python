# function decorator

def simple_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()  
        print("After the function runs")
    return wrapper

@simple_decorator
def greet():
    print("Hello, World!")
greet()



"""

def calculator(base):
    def working():
        a= int(input("Enter the 1st num: "))
        b= int(input("Enter the 2nd num: "))
        base(a,b)
        print("Well done!")
    return working

@calculator
def addition(a,b):
    print(a+b)
addition()

@calculator
def subtraction(a,b):
    print(a-b)
subtraction()

"""



"""
Decorators are used to add functionality to functions (e.g., logging, validation) without modifying their original code. 
They improve code reusability, clarity, and maintainability by separating additional behavior from core logic.

# Short Description:
This code uses a decorator to add behavior before and after the `greet` function runs. 
It prints extra messages without changing the original function.

# Flow:
1. Decorator (`simple_decorator`) wraps the function with additional behavior.
2. @simple_decorator replaces `greet` with a `wrapper` function.
3. When you call `greet()`, it:
   - Prints "Before the function runs".
   - Calls the original `greet()` → prints "Hello, World!".
   - Prints "After the function runs".

# Why Use a Decorator?
- To add extra functionality to functions without modifying them.
- For code reusability and cleaner organization.

"""


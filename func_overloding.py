"""
Function overloading is the concept of defining multiple functions with the same name 
but different parameters (number or type) to perform similar tasks with varying input. 

Function overloading in Python is not directly supported, but you can achieve it by using default arguments or
variable-length arguments (*args, **kwargs). 
You can also use @singledispatch to create overloaded functions based on the type of the first argument."""



"""
def greet(name, greeting = "Hello!"):
    return f"{greeting}, {name}!"

# str1 = greet("Anu")
# print(str1)

# OR

print(greet("Anu"))
print(greet("Hii!", "andy"))
"""



def add(*args):
    return sum(args)

print(add(1,2))
print(add(1,2,3,4,5))
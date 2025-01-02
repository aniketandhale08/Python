# class  world: 
#     x  =  10 
#     __india=  20 
# print(world.x) 
# print(world._world__india) 








class MyClass:
    def __init__(self):
        self.__private_var = 42 
    
    def get_private_var(self):
        return self.__private_var

obj = MyClass()

# print(obj.__private_var)  # AttributeError

print(obj._MyClass__private_var)

# Accessing through the method
print(obj.get_private_var())

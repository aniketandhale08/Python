# x = 10  

# def my_function():
#     y = 5  
#     print("Inside function, x:", x)  
#     print("Inside function, y:", y)  

# my_function()
# print("Outside function, x:", x)
# print("Outside function, y:", y)    # this will casue error bcz y is not a global var as x.



"""
The global x statement allows the function to modify the global variable x.

"x=%d y=%d": This is the string where %d is a placeholder for an integer value.
    
%d is used to format integers.

% (x, y): This part replaces the %d placeholders with the values of x and y."""


x  =  5  #  global  variable 
def  f1(): 
    global  x 
    x  =  15  #  global  variable  updated 
    y  =  10  #  Local  variable 
    # print("x=%d  y=%d" % (x, y))
    print(f"x={x}  y={y}")

f1() 
print(x) 
# **kwargs is used for keyword arguments, which are passed in the form key=value

# def display_info(**kwargs):
#     print("Received Information:")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# display_info(name="anu", age=22)

# display_info(name="andy", age=24, city="pune", job="Engineer")







# *args and **kwargs together

def print_details(*args, **kwargs):
    print("Positional Arguments (args):", args)
    print("Keyword Arguments (kwargs):", kwargs)

print_details(1, 2, 3, name="anu", age=22)

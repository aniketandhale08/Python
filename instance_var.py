""""
Instance member variables are specific to an object in a class.

- They store information (data) for that object.
- Each object has its own copy of these variables.
- You create them using the self keyword, usually inside the __init__ method.

"""

# Inside the __init__ Method

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# person1 = Person("John", 25)

# print(person1.name)  
# print(person1.age)   




# Inside Other Methods

# class Employee:
#     def set_details(self, id, salary):
#         self.id = id
#         self.salary = salary

# emp = Employee()
# emp.set_details(101, 50000)

# print(emp.id)     
# print(emp.salary)  




# ----------------------------------------


# practice

# class Codes1:
#     def personal_code(self, country_code, phone_num):
#         self.country_code = country_code
#         self.phone_num = phone_num

# per1 = Codes1()
# per1.personal_code(91, 8465126978)

# print(per1.country_code)
# print(per1.phone_num)



class codes1:
    def __init__(self,country_code, phone_num):
        self.country_code = country_code
        self.phone_num = phone_num

per1 = codes1(91, 1681468153)

print(per1.country_code)
print(per1.phone_num)
        
# main.py file 
import mymodule

from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('anu', 'andy'))

print(sum_two_nums(1,9))

mass = 100
weight = mass * gravity
print(weight)

print(person['firstname'])
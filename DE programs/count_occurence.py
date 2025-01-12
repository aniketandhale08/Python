# Write a Python program to count the occurrences of each character in a string.

input_str = input("Enter the string: ")
input_chra = input("Enter the charc to find: ")

count = 0
for char in input_str:
    if char == input_chra:
        count +=1
print(f"{input_chra} is present {count} times in string!")
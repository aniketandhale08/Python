# Write a Python program to check if a given string is a palindrome.

# input_str = input("Enter the string: ")

# if input_str[::-1] == input_str:
#     print("Palindrome")
# else:
#     print("Not palindrome")



def palindrome(input_str):
    return input_str[::-1]==input_str

input_str = input("Enter the string: ")
print(palindrome(input_str))

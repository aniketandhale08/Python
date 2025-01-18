# Write a Python program to check if a given string is a palindrome (reads the same forward and backward).

def palindrom_str(string1):
    string1 = string1.lower()
    return string1 == string1[::-1]

str1= "igi"
result = palindrom_str(str1)
print(f"Is this string is palindrome? {result}")



# method 2

"""

def is_palindrome(s):
    s = s.lower()  
    reverse_s = s[::-1]  
    if s == reverse_s:  
        return "Palindrome"
    else:
        return "Not a Palindrome"

s = "India"
result = is_palindrome(s)
print(f"The string is: {result}")


"""
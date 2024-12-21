str1 = str(input("Enter the 1st string: "))
str2 = str(input("Enter the 2nd string: "))

new_str1 =str1[::-1]

if str1 == new_str1:
    print("1st and 2nd string is palindrome.")
else:
    print("1st and 2nd string is not palindrome.")
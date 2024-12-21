str1 = str(input("Enter the 1st string: "))
str2 = str(input("Enter the 2nd string: "))

str1  =  str1.replace("  ","").upper() 
str2  =  str2.replace("  ","").upper() 

if sorted(str1) == sorted(str2): 
    print(f'"{str1}" and "{str2}" are anagrams.') 
else:
    print(f'"{str1}" and "{str2}" are not anagrams.')

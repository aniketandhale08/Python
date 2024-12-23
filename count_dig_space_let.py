#  The sub() function in Python comes from the re module (regular expressions) 
# and is used to replace matched patterns in a string with a specified value.

import re

# str = "Aniket have 1 cycle"

# digit_count = re.sub("[^0-9]", "", str)
# character_count = re.sub("[^a-zA-Z]", "", str)
# space_count = re.findall(r"[ \s]", str)

 
# print(len(digit_count))
# print(len(character_count))
# print(len(space_count))



# usign findall

str = "Hello 123 World 456!"
digits = re.findall(r"[0-9]", str)  
print(len(digits))

characters = re.findall(r"[a-zA-Z]", str)  
print(len(characters))
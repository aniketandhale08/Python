# str1 = "My mail id domain is @gmail.com and my 12th marks are 81%."

# sp_char  =  r"!@#$%^&*()<>?/\[]{};:~`" 
# count = 0

# for i in str1:
#     if i in sp_char:
#         count +=1
# print(count)


def special_character(str1):
    sp_char  =  r"!@#$%^&*()<>?/\[]{};:~`"
    count = 0

    for i in str1:
        if i in sp_char:
            count +=1
    return count
    
text = "My mail id domain is @gmail.com and my 12th marks are 81%."
result = special_character(text)
print(result)

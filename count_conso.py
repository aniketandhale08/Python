my_string = str(input("Enter the string: "))

vowel = ['a', 'e', 'i', 'o', 'u']

count = 0
for i in my_string:
    if i not in vowel:
        count+=1
print(count)
my_string = str(input("Enter the word: "))

vowel = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in my_string:
    if i in vowel:
        count +=1
print(count)
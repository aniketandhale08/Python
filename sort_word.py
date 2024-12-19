my_str = input("Enter a string: ")

# Break down the string into a list of words and capitalize each word
words = [word.capitalize() for word in my_str.split()]
words.sort()

print("The sorted words are:")
for word in words:
    print(word)

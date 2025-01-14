# Write a Python program to count the number of words in a given text file.

def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)
    
print("Word count: ", count_words("Output.txt"))
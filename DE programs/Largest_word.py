# Write a Python program to find the largest word in a given sentence.

def largets_words(sentence):
    words = sentence.split()
    return max(words, key=len)


sentence = input("Enter sentence: ")
print(largets_words(sentence))
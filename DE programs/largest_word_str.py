# Write a program to find the longest word in a given string.

def long_word(sent):
    words = sent.split()

    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

sentence = input("Enter the sentence: ")
print(long_word(sentence))
# Write a program to count how many times each word appears in a text file.

with open("sample.txt","w") as f:
    f.write("My name is Aniket and aniket want's to be a data engineer!")

word_count = {}
with open("sample.txt", "r") as f:
    for line in f:
        words = line.split()
        for word in words:
            word = word.strip(".,!").lower() 
            word_count[word] = word_count.get(word, 0) + 1

print("Word Frequency:", word_count)

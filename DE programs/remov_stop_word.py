# Write a program to remove common stop words (like "is", "and", "the") from a given sentence.

stop_words = {"is", "and", "the", "in", "on", "at", "a", "an"}
sentence = "My name is aniket and i want to be a data engineer."

filtered_sentence = []
for word in sentence.split():
    if word.lower() not in stop_words:
        filtered_sentence.append(word)

print("Filtered Sentence:", " ".join(filtered_sentence))
# Write a Python program to count the number of vowels (a, e, i, o, u) in a given string.


def count_vowels(string1):
    vowels = "aeiou"
    count = 0
    for char in string1:
        if char in vowels:
            count +=1
    return count

string11 = "my name is aniket"
print(count_vowels(string11))

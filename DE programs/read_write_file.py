# Write a Python program to write a list of numbers to a text file and then read it back.

def write_and_read_file():
    numbers = [10, 20, 30, 40, 50]
    with open("numbers.txt", "w") as f:
        for num in numbers:
            f.write(str(num) + "\n")
    
    print("File written. now reading them")
    with open("numbers.txt", "r") as f:
        content = f.read()
        print(content)

write_and_read_file()
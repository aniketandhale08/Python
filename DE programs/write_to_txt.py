def write_to_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(line + '\n' for line in lines)

lines = ['my name is anu', 'i live in India', 'I love India']
print("We have written to the file", write_to_file("Output.txt",lines))
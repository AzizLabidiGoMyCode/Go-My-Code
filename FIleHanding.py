# Q1: Read an entire text file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Q2: Read the first n lines of a file
n = 5  # the number of lines to read
with open('example.txt', 'r') as file:
    for i in range(n):
        line = file.readline()
        print(line)

# Q3: Read the last n lines of a file
n = 5  # the number of lines to read
with open('example.txt', 'r') as file:
    lines = file.readlines()
    last_n_lines = lines[-n:]
    for line in last_n_lines:
        print(line)

# Q4: Count the number of words in a text file
with open('example.txt', 'r') as file:
    content = file.read()
    words = content.split()
    print(len(words))

# Q5: Read the last n lines of a file (bonus)
n = 5  # the number of lines to read
with open('example.txt', 'r') as file:
    file.seek(0, 2)  # move the file pointer to the end of the file
    position = file.tell()  # get the current position of the file pointer
    lines = []
    while len(lines) < n and position > 0:
        # read the previous line
        position -= 1
        file.seek(position, 0)
        char = file.read(1)
        if char == '\n':
            lines.append(file.readline())
        elif position == 0:
            # add the first line of the file if it's not already in the list
            lines.append(file.readline())
    for line in reversed(lines):
        print(line)

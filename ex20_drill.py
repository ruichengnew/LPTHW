#Question 1
#I want to go faster.

#Question 2
#we use an expression "current_line = current_line + 1", so each time, current_line plus one, and the line go down one line.

#Question 3
#f means that this function need a file to read, open, seek, or readline.

#Question 4
#You told me before, seek(0) means finds the first byte in that file.

#Question 5
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_cout, f):
    print(line_cout, f.readline())

current_file = open(input_file)

print("Let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

#Question 1
#I can understand bits of it.

#Question 2
from sys import argv

script, filename = argv

print(f"I'm going to open the {filename}.")
file = open(filename)

print("Do you want me to read it out?")
input("Yes or No?(I would better get Yes)  ")

print("OK, let's see what is in it.")
print(file.read())

print("Woaw, that's fantasy. Do you want to close it?")
input("Yes or No")

print("OK, closing...")
file.close()

#Question 3
filename = input("Now we will do something magic. Show me any word, plz!\n >")
target = open(filename, 'x')

print("I would like to ask you for some lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

formatter = "{}\n{}\n{}\n"

print(f"Yeah, I will just put these lines into your {filename}.")
target.write(formatter.format(line1,line2,line3))

#Question 4
#'w' means we open this file to write something into it.

#Question 5
#Yes, we have to.
#'w' - open for writing, truncating the file first

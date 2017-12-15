#Question 1
#I did in ex15.py

#Question 2 - 3

#Question 4
#I ran it in bug.py

#Question 5
#I ran it in bug.py
#I think the input way is much better. Because it has a prompt, when I were a user, it has been more nicer.

#Question 6
file = open("ex15_sample.txt")
print(file.read())
#I can read the txt in above way

#Question 7
from sys import argv
script, filename = argv
file = open(filename)
print(file.close())
#close() is just like read()

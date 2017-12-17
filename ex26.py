print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input() #no height here
print("How much do you weigh?", end=' ') #no ) here
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

from sys import argv # no import here

script, filename = argv

txt = open(filename) # wrong spell

print(f"Here's your file {filename}:")#no f here
print(txt.read()) #wrong spell

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())#wrong character


print('Let\'s practice everything.') #escape sentence
print('You\'d need to know \'bout escapes')
print("\n newlines and \t tabs.") #wrong grammer line29 is a little weird

print('''You\'d need to know\'bout escapes
        with \\ \, \n newlines and \t tabs.''') #I write a new sentence here, I'm trying to guess the thoughts of that programmer

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation\n\t\twhere there is none.
"""#some more \ns and more spaces

print("--------------")#lack quote
print(poem)
print("--------------")#lack quote again


five = 10 - 2 + 3 - 6 #lack number
print(f"This should be five: {five}")#lack ) parenthesis

def secret_formula(started):#no colon here
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100 #lack divide /
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) #lack variable

#I delete the comment Zed wrote here, so that all the comments are written by me. And the comments are the mistakes.
print("With a starting point of: {}".format(start_point))

print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) #no underscore _

print("We'd have {} beans, {} jars, and {} crates".format(*formula))



people = 20
cats = 30 #wrong spell
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")#if-statement is not clear now, I will let the computer tell me later

if people < dogs:
    print("The world is drooled on!")

if people > dogs:#no colon again
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:#no colon
    print("People are less than or equal to dogs.")#lack quote


if people == dogs:
    print("People are dogs.")

#有点意思好吧，给别人改这个，就好像给学生改数学作业一样，哈哈哈哈！

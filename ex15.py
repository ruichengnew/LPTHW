#get argv from Python
from sys import argv
#Name two arguments
script, filename = argv#前三行很好理解，从外界获得两个输入，重点是文件名
#open the second argument "filename" [open means get a filename from user then give another parameter and command]
txt = open(filename)#open指令，用pydoc看了下，好长。。简单介绍，it takes a parameter and returns a value you can set to your own variable.
#print something
print(f"Here's your file {filename}:")#题目，下面是你的文件
#read the parameter from open
print(txt.read())#把我的文件展示出来了
#print another thing
print("Type the filename again: ")#打印，再给我一个文件名
#get a filename from user in another way (input way)
file_again = input('> ')#我又给了一个文件名
#open the file from the "input" user
txt_again = open(file_again)#它又把我给的文件打开了
#read again 
print(txt_again.read())#打开文件之后，读了出来

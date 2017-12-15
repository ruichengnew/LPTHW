from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).") #这个CTRL-C是什么按键啊，我怎么找不到。。感觉最后还是按回车啊
print("If you do want that, hit RETURN.")

input("?")#input的局限性就是，无论你输入什么好吧，最后都是回车执行下一个命令

print("Opening the file...")#写了代码才发现，这些话真是无聊。。不过也让代码读起来没那么无聊，hah
target = open(filename, 'w')#这个W问的好，还有b,t,r,a,x，在训练中我就用了x，这样好像省去了用argv这个feature(module)？

print("Truncating the file. Goodbye!")
target.truncate()#使用w必须先truncate

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")#这点我试过了，not readable，最后不能把写进去的东西都出来，也就是说，开头要用“+”
target.close()

#Question 1
#I did give fewer arguments, it told me "not enough values to unpack"
#we define 4 variables, so we should input four elements.

#Question 2
from sys import argv
Luffy, Sanji, Nami = argv

print("Your captain is: ", Luffy)
print("Your chef is: ", Sanji)
print("Your navigator is: ", Nami)


from sys import argv
Lawence, Tracy, Wuzong, Xiaoyuan, Kunge = argv

print("One of your best friends is: ", Lawence)
print("One of your best friends is: ", Tracy)
print("One of your best friends is: ", Wuzong)
print("One of your best friends is: ", Xiaoyuan)
print("One of your best friends is: ", Kunge)

#我在这个文件中写了两段代码，于是在运行的过程碰见了问题，第一段只需要三个argument， 第二段需要五个，提供三个太少，提供五个太多

from sys import argv
A, B, C = argv

print("Let me guess what the most valuable things are in your heart.")
print("The 1st thing is:\t", A)   #这个问题很严重，这个A难道一定是文件名么？所以第一句都是文件名字，那我就不从你开始玩，我直接把这句删了！
print("The 2nd thing is:\t", B)
print("The 3rd thing is:\t", C)

print("Now show me your thoughts.")
input("1. √ or ×   ")
input("2. √ or ×   ")
input("3. √ or ×   ")
print("Hah, I'm all right.")
#这个代码应该很符合题目意思了，不过run起来的排版真是太丑了，A的名字，第二部input的选择，以后后面不太能够随机应变，根据猜对了几个来有效的做出回应
#后面的input如果这样改一下可能更能体现编程技术
print("Now show me your thoughts.")
x = input("1. 对 or 错   ")
y = input("2. 对 or 错   ")
z = input("3. 对 or 错   ")
print(f"{x}{y}{z}, oh my god. I'm definitely genius.")
#不过，我不喜欢在这个地方用f-string，觉得很没有意义

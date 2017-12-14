types_of_people = 10
x = f"There are {types_of_people} types of people." #这里的变量x就是整个f-string

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." #这里应该是要向我展示，只有句子中（字符串string中）才能使用大括号{}形式的引用

print(x) #简单的打印一个变量
print(y) #打印另一个变量

print(f"I said: {x}") #这里值得注意，一个操作，会把这个程序中所有的format都会解释出来，并不因为他在x变量内部就不打印，也可以理解为，当你打出x的同时，所有的format就已经在程序中出现了，所以都被解释了
print(f"I also said: '{y}'")#这里应该是让我注意到，引号！！因为在define变量的时候，双引号是用来引用字符的，那作为说的话的引号就必须重新打一次

hilarious = True #这句话很有意思，让我知道了，除了数字，还有true和false也是黄色字体，也就是不需要加引号的，但是我直接用print（true）又打不出来。。比较奇怪，再看看吧
joke_evaluation = "Isn't that joke so funny?!{}" #这里最后的大括号其实没看懂，删除之后后面的.format就解释不出来啦

print(joke_evaluation.format(hilarious)) #没看懂，不太理解，就能模仿着写一写，在“.”的前面加任何字符都不行，不过能够打上空格
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e) #这个加号很有意思，我试了其他三种运算都不行，而且加号解释出来没占据空间
print（w,e) #相比“”+”，这个“，”就会占据一个空格

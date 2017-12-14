# Question 1

#Question 2
#这个问题讲道理是对英文和string的理解。。。百分百肯定的是line 11 and line 12
#不百分百肯定是原因是，一个单词，算一个string，换个角度来看，整个联系都只有6个print，最后一个完全没有f-string，第一个应该是也不是，那排除之后就是中间四个，所以回过头来看line 9， 这个string中套了一个string，说明binary和do_not都是string，开头的问题也就是迎刃而解了。

#Question 3
# I'm not sure.这问题在这等着我，上一题我是用排除法做的啊，其实排除之后清晰很多了，应该比较确定，第一个应该也是，所以有5个，10也是一个string。
#我改写了最后一个代码，这样的话应该就算6个了
w = "There is the left side of ...{}"
e = "a string of right side."
print(w.format(e)) #这句话应该是a string is put inside a string
print(w + e)
print(w , e)

#Questiong 4
我并不知道原因好吧，或许这就是python语法的一种，+可以连接string和string，并且不占用字符空间

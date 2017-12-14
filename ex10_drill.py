#Question 1: Yeah, I do.

#Question 2:
print("""
Dear, luna
\tI love you
""")            #这两个例子说明，三个双引号和三个单引号没有本质的区别，在多行打印中都可以使用
print('''
Dear, ladygod
\nI love you
''')

#Question 3:
heroA = "\n\tNevermore ShadowFiend"
heroB = "FuWang \"BieMoWo\""

print(f"Which hero just got killed by {heroB} in the mid?")
print("Which hero just got killed by Husker in the mid?{}".format(heroA))
#这两句话告诉我，f-string和.format不能在同一个句子中出现，不然就会出现f-string is empty的错误。

from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")#我的习惯，在名字前面加上逗号会更好
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")#和上个一样，总觉得文字形式的直接引用别人的回答非常傻，很不喜欢
#话说回来，书上给的例子，确实比我自己写的更加流畅自然一点，我用出来感觉有点像照搬照用
#有点想偷懒了。。。不过为了扎实的基础，还是模仿着写一个drill

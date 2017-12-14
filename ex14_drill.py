from sys import argv

script, user_name, adventure = argv
prompt = '\"never or ever\"'

print(f"Hello, {user_name}! Welcome to the {adventure}. I'm the host {script}.")
print(f"""
Now, let me introduce the rules of this game.
You will face some different questions, and you can only use {prompt} to answer them.
OK? Let's go!
""")

print("Have you ever gone abroad?")
abroad = input(f"{prompt}        ")#在这里，我不喜欢提示语和输入太接近，就用了一句话去改造提示语，但是觉得好麻烦，不知道有没有更简单的方法

print("Have you ever kissed with others?")
x = input(prompt)#我的习惯是用x，y，z来表示，在比较短的代码中比较简单，在长的代码中，为了方便阅读，可能还是需要更准确的变量，有点像做物理题

print(f"""
Alright, you said you have {abroad} gone abroad.
And you have {x} kissed, woaw. Wish you have a better life.
Thanks for coming!
""")

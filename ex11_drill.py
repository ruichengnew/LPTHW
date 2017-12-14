print("Which lane do you usually go?")
lane = input()
print("Which hero do  you like best?", end = ' ')
hero = input()
print("Which pro player do you like best?", end ='/n')
name = input()

print(f"You are a really good {lane} player, and very good at {hero}, and be a happy little {name}.")
#看起来可以写一些自己看起来好玩的语句了，创造的乐趣吧，不过能做的真的太少了，继续努力。
#对了，答案中还能输入中文哦，于是结果就会变成中英文结合体，如果我在整个print中都使用中文，肯定更有渲染力吧。

print("Just write a number you like.")
x = int(input())
print("You too, give me a number.")
y = int(input())

print("I can make them together, you guys see.",x + y)
#有一个有意思的地方，x和y是什么东西是你告诉系统的，不然就默认为字符，不能进行四则运算
#问题2，当你使用int时，如果输入的是个小数，则直接崩溃

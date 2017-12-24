#Question 1
#I convert the while-loop to a function I can call. Any number you can use to create a new range.
def new_range(n):
    i = 0
    numbers = []
    while i < n:
        numbers.append(i)
        i += 1

    return numbers
# This function it to create a new range(n)

#Question 2
from ex33_drill import *
numbers = new_range(6)
for i in numbers:
    print(i)
#只能用question 1那段script哦

#Question 3
def new_range(a, b):
    i = 0
    numbers = []
    while i < a:
        numbers.append(i)
        i += b

    return numbers
#Add another variable b

#Question 4
from bug1 import *  #这里的bug1是我用来测试自己写的任何形式的代码所用的文件名
numbers = new_range(10, 2)
for i in numbers:
    print(i)

#Question 5
def new_range(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers
#这个函数就是使用for-loop和range()函数写出来的

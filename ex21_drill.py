#Question 1
#I try to delete the "print" part of each function, and find nothing is changed.
#And then I delete all the "return"s, I get none at last. That means there is only expression but no equation, it's not a whole, complete sentence, I think that is the meaning of "return".

#Question 2
#This is really easy for a Chinese Student.

#Question 3
def puzzle(a, b, c, d):
    print(f"add({a}, subtract({b}, multiply({c}, divide({d},2))))")
    return a + b - c * d / 2

C = int(input("Show me your chest. > ")) #Chest, maybe Breast is much nicer.
W = int(input("Show me your waist. > "))
H = int(input("Show me your hips. > "))
I = int(input("Show me your IQ. > "))

print(puzzle(C, W, H, I))
#Of course, you can change the formula in "return", and then you will get another answer, the puzzle is changed.
#Maybe give the formula a more parenthesis. (a + b - c) * d / 2
def puzzle(a, b, c, d):
    return  (a + b - c) * d / 2

C = int(input("Show me your chest. > ")) #Chest, maybe Breast is much nicer.
W = int(input("Show me your waist. > "))
H = int(input("Show me your hips. > "))
I = int(input("Show me your IQ. > "))

print(puzzle(C, W, H, I))
#So now, the first answer is -5758.0, the second is 1050.0.

#Question 4
#So let's just do the second one.
def puzzle(a, b, c, d):
    print(f"divide(multiply(subtract(add({a}, {b}), {c}), {d}), 2))
    return (a + b - c) * d / 2
#That's it.

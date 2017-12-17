#Question 1
#我是写程序的人。。我当然知道怎么走啊。。。不走dead结尾的，随便出来好吧
#left - taunt bear - open door - 0 or 1 (the largest number you can take is 40)

#Question 2

#Question 3

#Question 4
#I have to move on.

#Question 5
#BUG: you can only type in a number with 0 or 1.
#if choice.digit:
#use the if-statement like above
def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

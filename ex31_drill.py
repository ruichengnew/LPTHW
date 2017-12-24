number = float(input("Show me a number, and I can tell you whether it is greater than 0 or not. > "))

if number > 0:
    print(f"Hah, {number} is greater than zero.")
elif number < 0:
    print(f"Emmm, {number} is less than zero.")
else:
    print("Definitely, you give me a Zero.")

print("""Let's play something bigger.
You just have a nonnegative integer in you own mind, and just tell me Yes or No.
I will guess your number right.""")
input("Are you ready? > ")

question1 = input("This number is less than 10. Yes or No? > ")

if question1 == "Yes" or question1 == "yes":
    question2 = input("This number is less than 5. Yes or No? > ")
    if question2 == "Yes" or question2 == "yes":
        question3 = input("This number is less than 2. Yes or No? > ")
        if question3 == "Yes" or question3 == "yes":
            print("Yah, your number is 1.")
        else:
            print("Your number must be one of 2, 3, 4.")
    else:
        question3b = input("This number is less than 7. Yes or No. > ")
        if question3b == "Yes" or question3b == "yes":
            question4b = input("This number is 5. Yes or No. >")
            if question4b == "Yes" or question4b == "yes":
                print("Aha, see.")
            else:
                print("Yep, it's 6. I'm a genius.")
        else:
            print("Your number must be one of 8, 9.")
else:
    print("OK, you have a big number, choose a closer number from the following. 50, 100, or 200.")
    bigger_number = input()
    if bigger_number == "50":
        print("Your number must be in range [10,75].")
    elif bigger_number == "100":
        print("Your number must be in range [75,150].")
    elif bigger_number == "200":
        print("Emm...Your number is so big that I give up. Sorry~")
    else:
        print("You have to give me one of the three numbers.")

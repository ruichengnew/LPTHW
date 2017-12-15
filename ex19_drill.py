def apple_game(pen, apple):
    print(f"I have a {pen};")
    print(f"I have an {apple};")
    print("Bomb!!!")
    print(f"{pen}{apple}.")

apple_game(1, 2)

apple_game("pen", "apple")

apple_game("Pang", "Yu")

Pangtou = 200
Yu = 50

apple_game(Pangtou, Yu)

apple_game(Pangtou + 200, Yu + 50)

apple_game(f"{Pangtou}Pangtou", f"{Yu}Yu")

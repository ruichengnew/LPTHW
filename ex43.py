from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yest configured.")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
    "You died. You kinda suck at this.",
    "Died",
    "Such a loser"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        The Gothon saw you.
        Now facing Gothon,
        What are you gonna do?"""))

        action = input("> ")

        if action == "run":
            print(dedent("""
            What a coward!
            You have to fight with your enemy!"""))
            return 'death'

        elif action == "shoot":
            print(dedent("""
            How overdaring you are!
            I can't believe you are the only survivor.
            Try to be smarter!"""))
            return 'death'

        elif action == "sing":
            print(dedent("""
            OK, your sing is so beautiful that your enemy lose himself in it.
            So you go and kick him out as soon as you can!
            Cool, Go on!"""))
            return 'laser_weapon_armory'

        else:
            print("Sorry, that's not expected answer.")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print("""Lucky man, come and die.
        In front of you, there is a three-digit code-lock.
        You only have 10 times to figure it out.""")

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input()
        guesses = 0

        while guess != code and guesses < 10:
            print("Wrong")
            guesses += 1
            guess = input()

        if guess == code:
            print("You are really good luck, next!")
            return 'the_bridge'
        else:
            print("Sorry, man.")
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print("""On your way, you found some other enemies.
        Now show me your intelligence""")

        action = input()

        if action == "throw the bomb":
            print("I said, coward must die.")
            return 'death'

        elif action == 'slowly place the bomb':
            print("Valour and Wisdom!")
            return 'escape_pod'

        else:
            return 'the_bridge'

class EscapePod(Scene):

    def enter():
        print(dedent(""""Finally, you come here. This will be the last chance I can kill you, I will cherish it.
        Now, there are five pods in front of you, choose one.
        Hah, only oen is right, others will blow you up"""))

        good_pod = randint(1,5)
        guess = input()

        if guess.isdigit() and int(guess) != good_pod:
            print("Bad luck, See you!")
            return 'death'

        elif guess.isdigit() and int(guess) == good_pod:
            print("Unbelievable!!! Envy your luck.")
            return 'finished'

        elif not guess.isdigit():
            print("I see, you want to die.")
            return 'death'

        else:
            return 'death'

class Finished(Scene):

    def enter(self):
        print("You won! Good job!!")
        return "finished"

class Map(object):

    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

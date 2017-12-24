from textwrap import dedent
from random import randint

class World(object):

    def enter(self):
        print("My first little World.")
        exit(1)

class World_Beginning(World):

    def enter(self):
        print(dedent("""
        Welcome to Ray's World.
        There are some interesting and challengable games.
        Plz enjoy it~
        """))
        print("Now you can choose one Island to go in.")

        user_input = input("TFC Island with '1' or WHU Island with '2'")

        if int(user_input) == 1:
            return 'tfc_island'

        elif int(user_input) == 2:
            return 'whu_island'

        else:
            print("Sorry, there are only islands now. Waiting for new..")
            return 'world_beginning'

class TFC_Island(World):

    def enter(self):
        pass

class WHU_Island(World):

    def enter(self):
        print("Welcome to Wuhan University!")
        print(dedent("""
        2010/09/06, it's a historical day in your life. You took your baggage into Guiyuan Dorm 310.
        As the moment as you stepped in 310, you met three students.
        One looks super handsome, and maybe filled with wisdom.
        One looks very brilliant, with a pair of sparkling eyes.
        The left, whose smile is very unreadable and mysterious, is smiling to you.
        You got shocked at that moment, so which one would you like to talk to first?
        Plz type in 1, 2, 3 to choose.
        """))

        user_input = input()

        if user_input == 1:
            return 'god_peng'

        if user_input == 2:
            return 'god_liang'

        if user_input == 3:
            return 'wang_tian'

class Real_Game(TFC_Island):

    def enter():
        pass

class Life_Countryside(TFC_Island):

    def enter():
        pass

class Teaching_Hours(TFC_Island):

    def enter():
        pass

class Death1(TFC_Island):

    quits = [
    'Sorry, I can\'t. I just can\'t.',
    'That is a so terrible task that I choose to quit.',
    'My parents ask me to make money, Sorry~',
    'Stupid cofellow, I don\'t want to stay with you any more.',
    'That\'s enough, the school, the local teachers, especially the stupid students. I\'m leaving.'
    ]

    def enter(self):
        print(quits[randint(1,5)])

class Death2(WHU_Island):

    fails = [
    'Hah, noobs!',
    'What a loser you are~',
    'Sha bi le ba, think more plzzzzzzz~',
    'I love you, Mr. Peng.',
    'Yeah, I remmember that night, only we three, ate instant noodles, and talked about our dreams. I\'m crying when typing this.'
    ]

    def enter(self):
        print(fails[randint(1,5)])

class Win1(TFC_Island):

    def enter(self):
        print("Congratulations! In such two years, though we were in different places, I think we went through the same challenges and had the same feelings. Happy to have you company!")
        return 'win1'

class Win2(WHU_Island):

    def enter(self):
        print("Hah, Congratulation! Miss you guys so much. I knew you gus when I was 16 years old, and now eight years passed, I really really want to hang out with you. Missing~")
        return 'win2'

class God_Liang(WHU_Island):

    def enter():
        pass

class God_Peng(WHU_Island):

    def enter(self):


class Wang_Tian(WHU_Island):

    def enter():
        pass

class Engine(object):


    def __init__(self, island):
        self.island = island#我这个地方要赋值 a_game = Island.world_island.Engine()

    def play(self):
        current_island = self.island.begin_pointer()
        final_island1 = self.island.next_island('win1')
        final_island2 = self.island.next_island('win2')

        while current_island != final_island1 and current_island != final_island2:
            current_pointer = current_island.enter()
            current_island = self.island.next_island(current_pointer)

class Island(object):

    pointers = {
        "world_beginning": World_Beginning(),
        "tfc_island": TFC_Island(),
        "whu_island": WHU_Island(),
        'real_game': Real_Game(),
        'life_countryside': Life_Countryside(),
        'teaching_hours': Teaching_Hours(),
        'god_liang': God_Liang(),
        'god_peng': God_Peng(),
        'wang_tian': Wang_Tian(),
        'death1': Death1(),
        'death2': Death2(),
        'win1': Win1(),
        'win2': Win2(),
    }

    def __init__(self, pointer):
        self.pointer = pointer

    def next_island(self, current_pointer):
        Val = self.pointers.get(current_pointer)
        return Val

    def begin_pointer(self):
        return self.next_island(self.pointer)

a_beginning = Island('world_beginning')
a_game = Engine(a_beginning)
a_game.play()

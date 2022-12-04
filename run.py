"""
Import
"""
import time


def welcome_to():
    """
    Welcome to the game message
    """
    print("\n" + r"""       __        __   _                            _
       \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___
        \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \
         \ V  V /  __/ | (__ (_) | | | | | |  __/ | |_ (_) |
          \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  """)


def logo():
    """
    Celestial Hang logo
    """
    print("\n" + r"""     ____     _          _   _       _ _
    / ___|___| | ___ ___| |_(_) __ _| | |__   __ _ _ __   __ _
   | |   / _ \ |/ _ \ __| __| |/ _` | | '_ \ / _` | '_ \ / _` |
   | |___  __/ |  __\__ \ |_| | (_| | | | | | (_| | | | | (_| |
    \____\___|_|\___|___/\__|_|\__,_|_|_| |_|\__,_|_| |_|\__, |
                                                         |___/  """)

    print(r"""      *   '      o           .       +         .        *
     .                   ~+   _______    +     |   '
        .   |       *      .  |/    |        - o -       +
     *    - o -               |   + |    .     |      .
            |      .   '      |     |        o             '
       +       ~+           * |     O    *        +    *
     .               *        |  ' /|\        '         .
            '              +  |    / \   .   ~~+     .    *
     *           o         .  |       *             o
     '    +    '       *      |    o       *     .      +
     ________________________/|\____________________________""" + "\n")


def welcome_player():
    """
    Input a name to have a more personalized response
    With a message to really welcome the visitor and give them the rules
    Choice of what level difficulty
    """
    global name
    name = input("Please enter you name here: ")
    print("\n" + f"""                            Welcome {name}
               I hope you have fun and good luck!""" + "\n")
    time.sleep(1)
    print("-----------------------------------------------------------------")
    print("\n" + "                      Here comes the rules..." + "\n")
    time.sleep(1)
    print("1. Try to see if you can guess the celestial themed word" + "\n")
    time.sleep(0.6)
    print("""2. You play by inputing one letter, if the letter is in the word -
   then you get another change but is the letter not then you lose a life""")
    time.sleep(0.6)
    print("\n" + """3. Can you guess the word before the person gets hung -
   or it's game over.""")
    time.sleep(0.6)
    print("\n" + """4. Remeber choose the difficulty level carefully -
   the higher you go the harder the word is to guess""" + "\n")
    time.sleep(1)
    print("-----------------------------------------------------------------")


def level_difficulty():
    """
    Choose level difficulty
    """
    print("""
        Choose one of the three levels to get started...""" + "\n")
    time.sleep(0.6)
    print("""                        For easy click E
                        For medium click M
                        For hard click H
    """)

    difficulty = True

    while difficulty:
        global level
        level = input(f"{name} please choose a difficulty here: ").upper()
        print("\n" + """
-----------------------------------------------------------------
        """)
        time.sleep(0.4)
        if level == "E":
            print(r"""                      _____
                     | ____|__ _ ___ _   _
                     |  _| / _` / __| | | |
                     | |___ (_| \__ \ |_| |
                     |_____\__,_|___/\__, |
                                     |___/ """ + "\n")
            lives = 5
            return lives
        elif level == "M":
            print(r"""               __  __          _ _
              |  \/  | ___  __| (_)_   _ _ __ ___
              | |\/| |/ _ \/ _` | | | | | '_ ` _ \
              | |  | |  __/ (_| | | |_| | | | | | |
              |_|  |_|\___|\__,_|_|\__,_|_| |_| |_|""" + "\n")
            lives = 7
            return lives
        elif level == "H":
            print(r"""                      _   _               _
                     | | | | __ _ _ __ __| |
                     | |_| |/ _` | '__/ _` |
                     |  _  | (_| | | | (_| |
                     |_| |_|\__,_|_|  \__,_|""" + "\n")
            lives = 10
            return lives
        else:
            print("\n Please write one of the following: E, M or H")
            print(" to choose the difficulty level you want. \n")


def choosen():
    """
    Message to show the player which level they have choosen as the game loads
    """
    print("""
-----------------------------------------------------------------
        """)
    print(f"{name} you choose {level} so let's get started!" "\n")


def game():
    """
    Function for the actul game play
    """


def main():
    """
    Run all program functions
    """
    welcome_to()
    time.sleep(0.6)
    logo()
    welcome_player()
    level_difficulty()
    time.sleep(0.5)
    choosen()
    time.sleep(0.5)


main()

"""
Import
"""
import time
import random
import string
import gspread
from google.oauth2.service_account import Credentials
from words import easy_dict, medium_dict, hard_dict
from hangman import e_lives, m_lives, h_lives

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('celestial_hang')


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
    print(r"""     ____     _          _   _       _ _
    / ___|___| | ___ ___| |_(_) __ _| | |__   __ _ _ __   __ _
   | |   / _ \ |/ _ \ __| __| |/ _` | | '_ \ / _` | '_ \ / _` |
   | |___  __/ |  __\__ \ |_| | (_| | | | | | (_| | | | | (_| |
    \____\___|_|\___|___/\__|_|\__,_|_|_| |_|\__,_|_| |_|\__, |
                                                         |___/  """)

    print(r"""      *   '      o           .       +         .        *
     .                   ~+   __________  +    |   '
        .   |       *      .  |/       |     - o -       +
     *    - o -               |   +    | .     |      .
            |      .   '      |        |     o             '
       +       ~+           * |        O  *       +    *
     .               *        |  '    /|\       '         .
            '              +  |       / \  .   ~~+     .    *
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
    print("\n" + f"""                          Welcome {name}
               I hope you have fun and good luck!""" + "\n")
    time.sleep(1)
    print("-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-")
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
    print("-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-")


def get_word():
    """
    Gets and chooses a random word from words file
    out from which difficulty has been choosen
    """
    word_e = random.choice(easy_dict)
    word_m = random.choice(medium_dict)
    word_h = random.choice(hard_dict)

    if level == "E":
        return word_e

    elif level == "M":
        return word_m

    elif level == "H":
        return word_h

    else:
        print("A mistake has happened, try again")


def game():
    """
    Function for the actul game play
    """
    global lives
    lives = level_difficulty()
    word = get_word()
    alphabet = set(string.ascii_lowercase)
    needed_letters = set(word)
    guessed_letters = set()
    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
    time.sleep(0.5)

    while len(needed_letters) > 0 and lives > 0:
        print("\nLetters already used: ", ' '.join(sorted(guessed_letters)))
        print('\n' + 'Lives left:', lives, )

        guess = [lett if lett in guessed_letters else '_' for lett in word]
        if level == "E":
            print(e_lives[lives])
        elif level == "M":
            print(m_lives[lives])
        else:
            print(h_lives[lives])

        print('The current word: ', ' '.join(guess))

        user_guessed = input("\n" + """
Please write a letter here: """).lower().strip(' ')

        if user_guessed in alphabet - guessed_letters:
            guessed_letters.add(user_guessed)
            if user_guessed in needed_letters:
                needed_letters.remove(user_guessed)
                print('\nYou are so smart,', user_guessed, 'is in the word')

            else:
                lives = lives - 1
                print("\n")
                print('Oh no,', user_guessed, 'is not in the word, try again!')

            print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)

        elif user_guessed in guessed_letters:
            print("\nYou've tried this letter already. Please try another.")

        else:
            print('\nInvalid character used! please type in a valid letter.')

    if lives == 0:
        if level == "E":
            print(e_lives[lives])
        elif level == "M":
            print(m_lives[lives])
        else:
            print(h_lives[lives])

        print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
        print(r"""      *   '      o           .       +         .        *
    .     ____ +   '    .    ~+        ___    *       '     +
        '/ ___| __ _+_ __ ___   ___ * / _ \__ . _____ _ __    '
  *     | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|'  *
    ~+ .| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |    .
         \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  *
     +   *           o     '   .  +       *       '     o    ~+
        '    +    '       *      '    o       *     .      +
        """)
        print(f"""
                  Oh no, {name}, you've been hanged!""")
        print("\n" + "                        The word was " + word + "\n")
    else:
        print(r"""      *          o           .       +         .        *
     .                  ~+ ____________   +    |   '        .
        .   |       *    .-\    _     /-.    - o -       +
     *    - o -         | (|   / |    |) | .   |      .
            |      .   ' '-|     |    |-'    o             '
       +       ~+         .\    _|_   /   *       +    *
     .               *      '.      .'  .       '         .
            '              + _`)  (`_      .   ~~+     .    *
     *           o        ._/________\_             o
     '    +    '       *  /____________\   *     .      +
        """)

        print(f"""
            Congratulations {name} you guessed the word!
                     """)
        print("                       The word was " + word + "\n")


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
        level = input(f"""
            {name} please choose a difficulty here: """).upper().strip(' ')
        print("\n" + """
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
        time.sleep(0.4)
        if level == "E":
            print(r"""                      _____
                     | ____|__ _ ___ _   _
                     |  _| / _` / __| | | |
                     | |___ (_| \__ \ |_| |
                     |_____\__,_|___/\__, |
                                     |___/ """)
            lives = 5
            return lives
        elif level == "M":
            print(r"""               __  __          _ _
              |  \/  | ___  __| (_)_   _ _ __ ___
              | |\/| |/ _ \/ _` | | | | | '_ ` _ \
              | |  | |  __/ (_| | | |_| | | | | | |
              |_|  |_|\___|\__,_|_|\__,_|_| |_| |_|""")
            lives = 7
            return lives
        elif level == "H":
            print(r"""                      _   _               _
                     | | | | __ _ _ __ __| |
                     | |_| |/ _` | '__/ _` |
                     |  _  | (_| | | | (_| |
                     |_| |_|\__,_|_|  \__,_|""")
            lives = 10
            return lives
        else:
            print("""
         Please write one of the following: E, M or H""")
            print("""
           to choose the difficulty level you want.""" + "\n")


def choosen():
    """
    Message to show the player which level they have choosen as the game loads
    """
    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
    print(f"             {name} you choose {level} so let's get started!" "\n")


def game_end():
    """
    Function loop to choose to play again or stop
    """
    global play

    if lives == 0:
        play = input(f"""
    That is to bad {name}! Want to try again? yes = y, no = n: """).strip(' ')
    else:
        play = input(f"""
        Yes {name}! Want to try again? yes = y, no = n: """).strip(' ')

    while play:
        if play == "y":
            print("\n")
            print(f"            That is great {name}. Let's get to it!")
            print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
            game()
            game_end()
        elif play == "n":
            print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
            new_words()
            print(f"""
             Thanks you {name} for playing CelestialHang""")
            print("                    Hope to see you again soon!" + "\n")
            time.sleep(1.3)
            logo()
            time.sleep(5)
            exit()
        else:
            print("\n" + """
                Sorry let's try that one more time!""" + "\n")
            play = input("""
              Want to try again? yes = y, no = n: """).strip(' ')


def new_words():
    """
    Let the visitor give own ideas for new words
    while putting them on a spreadsheet for review
    """
    # global question
    if play == "n":
        print("Wait one second please!\n")
        print("Before you go, do you have any words you want to add?\n")
        print("Maybe a word you would like to see become apart of the game")
        print("\nThen now is your change!\n")
        question = input("So do you have one? yes = y, no = n: ").strip(' ')

        while question:
            if question == "y":
                ideas = input("\nEnter your word here: ").strip(' ')
                print(f"Thank you for sending in the word: {ideas}" + "\n")
                more = input("Do you have more? yes = y, no = n: ").strip(' ')
                while more:
                    if more == "y":
                        ideas = input("\nEnter your word here: ")
                        print(f"Thank you for sending in the word: {ideas}")
                        more = input("""
Do you have more? yes = y, no = n: """).strip(' ')
                    elif more == "n":
                        print("\nThank you for sharing your words!")
                        print("Please come back soon!")
                        return
                    else:
                        print("\ninvalid character! Please try again!")
                        more = input("""
Do you have more? yes = y, no = n: """).strip(' ')
            elif question == "n":
                print("\nThen on you go!")
                break
            else:
                print("\nI am sorry I didn't get that...")
                question = input("""
            So do you have one? yes = y, no = n: """).strip(' ')
    else:
        pass


def main():
    """
    Run all program functions
    """
    welcome_to()
    time.sleep(0.6)
    logo()
    welcome_player()
    time.sleep(0.5)
    game()


main()
game_end()

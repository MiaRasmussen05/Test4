"""
Import
"""
import time
import random
import string
import colorama
from colorama import Fore, Style
# , Back, Style
import gspread
from google.oauth2.service_account import Credentials
from words import easy_words, medium_words, hard_words, special_words
from hangman import e_lives, m_lives, h_lives, s_lives
colorama.init()

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
    print(r"""       __        __   _                            _
       \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___
        \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \
         \ V  V /  __/ | (__ (_) | | | | | |  __/ | |_ (_) |
          \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ """)


def logo():
    """
    Celestial Hang logo
    """
    print(r"""     ____     _          _   _       _ _   _
    / ___|___| | ___ ___| |_(_) __ _| | | | | __ _ _ __   __ _
   | |   / _ \ |/ _ \ __| __| |/ _` | | |_| |/ _` | '_ \ / _` |
   | |___  __/ |  __\__ \ |_| | (_| | |  _  | (_| | | | | (_| |
    \____\___|_|\___|___/\__|_|\__,_|_|_| |_|\__,_|_| |_|\__, |
                                                         |___/ """)

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
    Color for the name verible
    With a message to really welcome the visitor
    Run the rules function
    """
    global name
    name_col = input("Please enter you name here: ")
    name = Fore.MAGENTA + name_col + Fore.WHITE
    print("\n" + f"""                          Welcome {name}
               I hope you have fun and good luck!""" + "\n")
    time.sleep(1)
    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
    rules()
    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-""" + "\n")
    time.sleep(1)


def rules():
    """
    Inform the player about the game rules
    Implement color for the rules function
    """
    print(Fore.CYAN + """                     Here comes the rules...""" "\n")
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
   the higher you go the harder the word is to guess""" + Fore.WHITE)


def get_word():
    """
    Gets and chooses a random word from words file
    out from which difficulty has been choosen
    """
    word_e = random.choice(easy_words)
    word_m = random.choice(medium_words)
    word_h = random.choice(hard_words)
    word_s = random.choice(special_words)

    if level == "E":
        return word_e
    elif level == "M":
        return word_m
    elif level == "H":
        return word_h
    elif level == "S":
        return word_s
    else:
        print("A mistake has happened, try again")


score = 0


def game():
    """
    Function for the actul game play
    """
    global lives
    global score
    lives = level_difficulty()
    time.sleep(1)
    choosen()
    word = get_word()
    word_col = Fore.BLUE + Style.BRIGHT + word + Fore.WHITE
    alphabet = set(string.ascii_lowercase)
    needed_letters = set(word)
    guessed_letters = set()
    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
    time.sleep(0.5)

    while len(needed_letters) > 0 and lives > 0:
        print("Letters already used: ", ' '.join(sorted(guessed_letters)))
        if level == "E":
            if lives >= 4:
                print('\n' + 'Lives left:' + Fore.GREEN, lives, Fore.WHITE)
            elif lives >= 2:
                print('\n' + 'Lives left:' + Fore.YELLOW, lives, Fore.WHITE)
            elif lives >= 0:
                print('\n' + 'Lives left:' + Fore.RED, lives, Fore.WHITE)
        elif level == "M":
            if lives >= 5:
                print('\n' + 'Lives left:' + Fore.GREEN, lives, Fore.WHITE)
            elif lives >= 3:
                print('\n' + 'Lives left:' + Fore.YELLOW, lives, Fore.WHITE)
            elif lives >= 0:
                print('\n' + 'Lives left:' + Fore.RED, lives, Fore.WHITE)
        elif level == "H":
            if lives >= 7:
                print('\n' + 'Lives left:' + Fore.GREEN, lives, Fore.WHITE)
            elif lives >= 4:
                print('\n' + 'Lives left:' + Fore.YELLOW, lives, Fore.WHITE)
            elif lives >= 0:
                print('\n' + 'Lives left:' + Fore.RED, lives, Fore.WHITE)
        elif level == "S":
            if lives >= 8:
                print('\n' + 'Lives left:' + Fore.GREEN, lives, Fore.WHITE)
            elif lives >= 4:
                print('\n' + 'Lives left:' + Fore.YELLOW, lives, Fore.WHITE)
            elif lives >= 0:
                print('\n' + 'Lives left:' + Fore.RED, lives, Fore.WHITE)
        print('Score:', score, )

        guess = [lett if lett in guessed_letters else '_' for lett in word]
        if level == "E":
            print(e_lives[lives])
        elif level == "M":
            print(m_lives[lives])
        elif level == "H":
            print(h_lives[lives])
        else:
            print(s_lives[lives])

        print('The current word: ', ' '.join(guess))

        user_guessed = input("""
Please write a letter here: """).lower().strip(' ')

        if user_guessed in alphabet - guessed_letters:
            guessed_letters.add(user_guessed)
            if user_guessed in needed_letters:
                needed_letters.remove(user_guessed)
                print('\nYou are so smart,', user_guessed, 'is in the word')

            else:
                lives = lives - 1
                print(f"""
Oh no, {user_guessed} is not in the word, try again!""")

        elif user_guessed in guessed_letters:
            print("\nYou've tried this letter already. Please try another.")

        else:
            print('\nInvalid character used! please type in a valid letter.')

        print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)

    if lives == 0:
        if level == "E":
            print(e_lives[lives])
        elif level == "M":
            print(m_lives[lives])
        elif level == "H":
            print(h_lives[lives])
        else:
            print(s_lives[lives])

        print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
        first = Fore.RED + "____" + Fore.WHITE
        second = Fore.RED + r"___" + Fore.WHITE
        third = Fore.RED + r"/ ___| __ _" + Fore.WHITE
        forth = Fore.RED + r"_ __ ___   ___" + Fore.WHITE
        fifth = Fore.RED + r"/ _ \__" + Fore.WHITE
        sixth = Fore.RED + "_____ _ __" + Fore.WHITE
        seventh = Fore.RED + r"| |  _ / _` | '_ ` _ \ / _ \ " + Fore.WHITE
        eight = Fore.RED + r"| | | \ \ / / _ \ '__|" + Fore.WHITE
        ninth = Fore.RED + r"| |_| | (_| | | | | | |  __/" + Fore.WHITE
        tenth = Fore.RED + r"| |_| |\ V /  __/ |" + Fore.WHITE
        eleventh = Fore.RED + r"\____|\__,_|_| |_| |_|\___|" + Fore.WHITE
        twelfth = Fore.RED + r"\___/  \_/ \___|_|" + Fore.WHITE
        print(f"""      *   '      o           .       +         .        *
    .     {first} +   '    .    ~+        {second}    *       '     +
        '{third}+{forth} * {fifth} . {sixth}    '
  *     {seventh}{eight}'  *
    ~+ .{ninth} {tenth}    .
         {eleventh}  {twelfth}  *
     +   *           o     '   .  +       *       '     o    ~+
        '    +    '       *      '    o       *     .      +
        """)
        print(f"""
                  Oh no, {name}, you've been hanged!

                        The word was {word_col}

                        Your score is {score}""")
    else:
        if level == "E":
            score += 100
        elif level == "M":
            score += 2
        elif level == "H":
            score += 3
        elif level == "S":
            score += 4

        if score == 5:
            first = Fore.YELLOW + ",------." + Fore.WHITE
            second = Fore.YELLOW + r'/   ,--.  "______________' + Fore.WHITE
            third = Fore.YELLOW + r"|   |    |                 |" + Fore.WHITE
            forth = Fore.YELLOW + r"\   '--'  .__||__|__||___'" + Fore.WHITE
            fifth = Fore.YELLOW + r'"------"' + Fore.WHITE
            print(f"""      *          o     .     .       +         .        *
     .                  ~+                +    |   '        .
        .   |       *     .     '     '      - o -       +
     *    - o -        {first}  *     .   .   |      .
            |      . {second}    .   '     '
       +       ~+   {third}  +    *
     .          .    {forth} '    .    .
            '        + {fifth}           .    ~~+     .    *
     *           o        .      *   '       .      o
     '    +    '       *       .    +      *     .      +
        """)
            print(f"""
       Would you look at that {name}, you found the hidden key!
          Maybe it would be worth it doing another round.
Take a closer look at the difficulties before you choose your path.

                        The word was {word_col}

                        Your score is {score}""")
        elif score == 25:
            first = Fore.CYAN + "_____   _______" + Fore.WHITE
            second = Fore.CYAN + r"|___   \|    ___|" + Fore.WHITE
            third = Fore.CYAN + r"\   |   |__" + Fore.WHITE
            forth = Fore.CYAN + r"__/   |___   \ " + Fore.WHITE
            fifth = Fore.CYAN + r"/   __/    \   |" + Fore.WHITE
            sixth = Fore.CYAN + "|   |___ ___/   |" + Fore.WHITE
            seventh = Fore.CYAN + "|_______|_____ /" + Fore.WHITE
            print(f"""      *     ,    o     .     .       +         .        *
     .           .     ~+ {first} +    |   '        .
        .   |       *    {second}   - o -       +
     *    - o -            . {third}   .   |      .
            |      .   '   {forth}   o             '
       +       ~+         {fifth}*       +    *
     .               *   {sixth}  .   '    .    .
            '          . {seventh}      ~~+     .   *
     *           o        '    .    *               o
     '    +    '       *     '   +     .   *     .      +
            """)
            print(f"""
                    You are on a roll here!

                        The word was {word_col}

                        Your score is {score}""")
        elif score == 50:
            first = Fore.CYAN + "_______  ______" + Fore.WHITE
            second = Fore.CYAN + r"|    ___|/  __  \ " + Fore.WHITE
            third = Fore.CYAN + r"|   |__ |  |  |  |" + Fore.WHITE
            forth = Fore.CYAN + r"|___   \|  |  |  |" + Fore.WHITE
            fifth = Fore.CYAN + r"\   |  |  |  |" + Fore.WHITE
            sixth = Fore.CYAN + "___/   |  |__|  |" + Fore.WHITE
            seventh = Fore.CYAN + r"|_____ / \______/" + Fore.WHITE
            print(f"""      *     ,    o     .     .       +         .        *
     .           .     ~+ {first} +    |   '        .
        .   |       *    {second}  - o -       +
     *    - o -          {third}.   |      .
            |      .   ' {forth}  o             '
       +       ~+          , {fifth}       +    *
     .               *    {sixth} .   '    .    .
            '          . {seventh}     ~~+     .   *
     *           o        '    .    *               o
     '    +    '       *     '   +     .   *     .      +
            """)
            print(f"""
     How are you doing this! Can I borrow some of that skill?

                        The word was {word_col}

                        Your score is {score}""")
        elif score == 75:
            first = Fore.CYAN + "_________ _______" + Fore.WHITE
            second = Fore.CYAN + r"|______   |    ___|" + Fore.WHITE
            third = Fore.CYAN + r"/  /|   |__" + Fore.WHITE
            forth = Fore.CYAN + r"/  / |___   \ " + Fore.WHITE
            fifth = Fore.CYAN + r"/  /" + Fore.WHITE
            sixth = Fore.CYAN + r"\   |" + Fore.WHITE
            seventh = Fore.CYAN + "/  /" + Fore.WHITE
            eight = Fore.CYAN + r"___/   |" + Fore.WHITE
            ninth = Fore.CYAN + r"/__/    |_____ /" + Fore.WHITE
            print(f"""      *     ,    o     .     .       +         .        *
     .           .    ~+ {first} +      |         .
        .   |       *   {second}     - o -    +
     *    - o -            o  {third}  .      |   .
            |      .   '     {forth}  o             '
       +       ~+         + {fifth}    . {sixth}       +    *
     .               *     {seventh} ,  {eight} .   '    .    .
            '          .  {ninth}     ~~+     .   *
     *           o        '    .    *               o
     '    +    '       *     '   +     .   *     .      +
            """)
            print(f"""
                  How high are you going to go!!!

                        The word was {word_col}

                        Your score is {score}""")
        elif score == 100:
            first = Fore.CYAN + "____  ______" + Fore.WHITE
            second = Fore.CYAN + r"______" + Fore.WHITE
            third = Fore.CYAN + r"/    |/  __  \ /  __  \ " + Fore.WHITE
            forth = Fore.CYAN + r"/_    |  |  |  |  |  |  |" + Fore.WHITE
            fifth = Fore.CYAN + r"|   |  |  |  |  |  |  |" + Fore.WHITE
            sixth = Fore.CYAN + r"|   |  |  |  |  |  |  |" + Fore.WHITE
            seventh = Fore.CYAN + "|   |  |__|  |  |__|  |" + Fore.WHITE
            eight = Fore.CYAN + r"|___|\______/ \______/" + Fore.WHITE
            print(f"""      *     ,    o     .     .       +         .        *
     .          .   ~+ {first} . {second}+      |         .
        .   |       * {third}    - o -    +
     *    - o -      {forth}.    |   .
            |      .   {fifth}   o          '
       +       ~+      {sixth}    +    *
     .               * {seventh}  '    .    .
            '          {eight}  ~~+     .   *
     *           o   '    '    .    *               o
     '    +    '       *     '   +     .   *     .      +
            """)
            print(f"""
               Not even the sky is a limit for you!

                        The word was {word_col}

                        Your score is {score}""")
        else:
            first = Fore.YELLOW + "____________" + Fore.WHITE
            second = Fore.YELLOW + r".-\    _     /-." + Fore.WHITE
            third = Fore.YELLOW + r"| (|   / |    |) |" + Fore.WHITE
            forth = Fore.YELLOW + r"'-|     |    |-'" + Fore.WHITE
            fifth = Fore.YELLOW + r"\    _|_   /" + Fore.WHITE
            sixth = Fore.YELLOW + "'.      .'" + Fore.WHITE
            seventh = Fore.YELLOW + r"_`)  (`_" + Fore.WHITE
            eight = Fore.YELLOW + r"_/________\_" + Fore.WHITE
            ninth = Fore.YELLOW + r"/____________\ " + Fore.WHITE
            print(f"""      *     .    o     .     .       +         .        *
     .           .      ~+ {first}   +    |   '        .
        .   |       *    {second}    - o -       +
     *    - o -         {third} .   |      .
            |      .   ' {forth}    o             '
       +       ~+         .{fifth}   *       +    *
     .               *      {sixth}  .       '    .    .
            '          .   + {seventh}      .   ~~+     .   *
     *           o        .{eight}             o
     '    +    '       *  {ninth}  *     .      +
            """)

            print(f"""
            Congratulations {name} you guessed the word!

                        The word was {word_col}

                        Your score is {score}""")


def level_difficulty():
    """
    Choose level difficulty
    """
    green = Fore.GREEN + "easy" + Fore.WHITE
    green_e = Fore.GREEN + "E" + Fore.WHITE
    yellow = Fore.YELLOW + "medium" + Fore.WHITE
    yellow_m = Fore.YELLOW + "M" + Fore.WHITE
    red = Fore.RED + "hard" + Fore.WHITE
    red_h = Fore.RED + "H" + Fore.WHITE
    blue = Fore.BLUE + "special" + Fore.WHITE
    blue_s = Fore.BLUE + "S" + Fore.WHITE

    if score >= 5:
        print("""
         Choose one of the four levels to get started...""" + "\n")
    else:
        print("""
         Choose one of the three levels to get started...""" + "\n")
    time.sleep(0.6)
    print(f"""                        For {green} click {green_e}
                        For {yellow} click {yellow_m}
                        For {red} click {red_h}""")
    if score >= 5:
        print(f"""                  For the {blue} level click {blue_s}""")

    difficulty = True

    while difficulty:
        global level
        global level_col
        level = input(f"""
            {name} please choose a difficulty here: """).upper().strip(' ')
        print("\n" + """
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-""")
        time.sleep(0.4)
        if level == "E":
            level_col = Fore.GREEN + level + Fore.WHITE
            print(Fore.GREEN + r"""
                      _____
                     | ____|__ _ ___ _   _
                     |  _| / _` / __| | | |
                     | |___ (_| \__ \ |_| |
                     |_____\__,_|___/\__, |
                                     |___/
            """ + Fore.WHITE)
            lives = 5
            return lives
        elif level == "M":
            level_col = Fore.YELLOW + level + Fore.WHITE
            print(Fore.YELLOW + r"""
               __  __          _ _
              |  \/  | ___  __| (_)_   _ _ __ ___
              | |\/| |/ _ \/ _` | | | | | '_ ` _ \
              | |  | |  __/ (_| | | |_| | | | | | |
              |_|  |_|\___|\__,_|_|\__,_|_| |_| |_|
            """ + Fore.WHITE)
            lives = 7
            return lives
        elif level == "H":
            level_col = Fore.RED + level + Fore.WHITE
            print(Fore.RED + r"""
                      _   _               _
                     | | | | __ _ _ __ __| |
                     | |_| |/ _` | '__/ _` |
                     |  _  | (_| | | | (_| |
                     |_| |_|\__,_|_|  \__,_|
            """ + Fore.WHITE)
            lives = 10
            return lives
        if score >= 5:
            if level == "S":
                level_col = Fore.BLUE + level + Fore.WHITE
                print(Fore.BLUE + r"""
                 ____                  _       _
                / ___| _ __   ___  ___(_) __ _| |
                \___ \| '_ \ / _ \/ __| |/ _` | |
                 ___) | |_) |  __/ (__| | (_| | |
                |____/| .__/ \___|\___|_|\__,_|_|
                      |_|
                """ + Fore.WHITE)
                lives = 11
                return lives
        else:
            if score >= 5:
                print("""
         Please write one of the following: E, M, H or S
             to choose the difficulty level you want.
                """)
            else:
                print("""
         Please write one of the following: E, M or H
           to choose the difficulty level you want.
                """)


def choosen():
    """
    Message to show the player which level they have choosen as the game loads
    """
    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
    print(f"             {name} you choose {level_col} so let's get started!")


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
        Yes {name}! Want to try again? yes = y, no = n: """).lower().strip(' ')

    while play:
        if play == "y":
            print("\n")
            print(f"              That is great {name}. Let's get to it!")
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
            print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-""")
            print(f"""
             Thanks you {name} for playing CelestialHang""")
            print("                    Hope to see you again soon!" + "\n")
            time.sleep(1.3)
            logo()
            print("""
                          Copyright ©Mia Rasmussen 2022
  Disclaimer: this game was built for a project and is not for commercial use
     I do not own the words that was used in any of the level difficulties.
            """)
            time.sleep(5)
            exit()
        else:
            print("\n" + """
                Sorry let's try that one more time!""" + "\n")
            play = input("""
              Want to try again? yes = y, no = n: """).lower().strip(' ')


def new_words():
    """
    Let the visitor give own ideas for new words
    while putting them on a spreadsheet for review
    """
    global ideas
    if play == "n":
        print("                      Wait one second please!\n")
        time.sleep(2)
        print("""      Before you go, do you have any words you want to add?
   Maybe a word you would like to see become apart of the game
                      Then now is your change!""")
        time.sleep(0.7)
        question = input("""
              So do you have one? yes = y, no = n: """).lower().strip(' ')
        print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
        time.sleep(0.3)

        while question:
            if question == "y":
                ideas = input("\nEnter your word here: ").strip(' ')
                time.sleep(0.3)
                if validatation(ideas) != ideas.isnumeric():
                    update_ideas_worksheet(ideas)
                    time.sleep(0.7)
                    print(f"Thank you for sending in the word: {ideas}\n")
                more = input("""
Do you have more? yes = y, no = n: """).lower().strip(' ')

                while more:
                    if more == "y":
                        ideas = input("\nEnter your word here: ")
                        time.sleep(0.3)
                        if validatation(ideas) != ideas.isnumeric():
                            update_ideas_worksheet(ideas)
                            time.sleep(0.7)
                            print(f"""
Thank you for sending in the word: {ideas}""")
                        more = input("""
Do you have more? yes = y, no = n: """).lower().strip(' ')
                    elif more == "n":
                        print("\nThank you for sharing your words!")
                        print("Please come back soon!")
                        return
                    else:
                        print("\ninvalid character! Please try again!")
                        more = input("""
Do you have more? yes = y, no = n: """).lower().strip(' ')
            elif question == "n":
                print("                           Then on you go!")
                break
            else:
                print("\nI am sorry I didn't get that...")
                question = input("""
            So do you have one? yes = y, no = n: """).lower().strip(' ')
    else:
        pass


def stars():
    """
    Let the visitor give stars and review of the game
    while putting them on a spreadsheet
    """


def validatation(value):
    """
    Inside of the try, all string values converts into integers.
    # Raises ValueError if strings cannot be converted into int,
    or if there is more then 1 value for one word.
    """
    try:
        if value == ideas.isnumeric():
            raise ValueError(
                f"A word is required, you provided {value}"
            )
    except ValueError:
        pass


def update_ideas_worksheet(data):
    """
    Update word ideas worksheet, add new row with the list data provided
    """
    update_words = SHEET.worksheet("ideas")
    update_words.append_row([data])
    print("\nYour word is now up for review.\n")


def main():
    """
    Run all program functions
    """
    welcome_to()
    time.sleep(0.6)
    logo()
    time.sleep(0.7)
    welcome_player()
    time.sleep(0.5)
    game()


main()
game_end()

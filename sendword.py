"""
Files to store the functions, scope and credits for the player
to be able to input their own word for review
"""
import time
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('celestial_hang')


def new_words():
    """
    Let the visitor give own ideas for new words
    while putting them on a spreadsheet for review
    Run a while loop to collect a valid string of words
    Until the string of words is valid the loop reapeats itself.
    1-5 words, separated by commas.
    """
    global ideas
    global ideas_value
    print("                      Wait one second please!")
    time.sleep(2)
    print("""
      Before you go, do you have any words you want to add?
   Maybe a word you would like to see become apart of the game
                      Then now is your change!""")
    time.sleep(0.7)
    question = input("""
          So do you have one or more? yes = y, no = n:\n""").lower().strip(' ')
    if question != "n":
        print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
    time.sleep(0.3)

    while True:
        if question == "y":
            print("""If more then one word, they should be separated by commas.
Up till 5 words is permitted.
E.g: Virgo,Libra,Aries,Leo,Cancer""")
            ideas = input("\nEnter your word/s here:\n").strip(' ')
            ideas_value = ideas.split(",")
            if len(ideas_value) < 1 or len(ideas_value) > 5:
                print("Please enter between 1 and 5 words separated by commas")
            else:
                return True
        elif question == "n":
            return False
        else:
            print("                   I am sorry I didn't get that...")
            question = input("""
          So do you have one or more? yes = y, no = n:\n""").lower().strip(' ')
            if question != "n":
                print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
        # return ideas_value


def update_ideas_worksheet():
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    if len(ideas_value) < 1 or len(ideas_value) > 5:
        print("\nPlease enter between 1 and 5 words separated by commas.\n")
        # return

    if len(ideas_value) > 2:
        print("Sending words into review...\n")
    else:
        print("Sending word into review...\n")

    worksheet_to_update = SHEET.worksheet("ideas")
    worksheet_to_update.append_row(ideas_value)

    if len(ideas_value) > 2:
        print("\nYour words is now up for review.\n")
    else:
        print("\nYour word is now up for review.\n")
    if len(ideas_value) > 2:
        print(f"Thank you for sending in the words: {ideas}\n")
    else:
        print(f"Thank you for sending in the word: {ideas}\n")


def send_new_words():
    """
    Run functions
    """
    valid = False
    while not valid:
        ideas = new_words()
        if ideas:
            valid = True
            update_ideas_worksheet()

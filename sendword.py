"""
Files to store the functions, scope and credits for the player
to be able to input their own word for review
"""
import time
import gspread
from google.oauth2.service_account import Credentials
# import review


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
    print("                      Wait one second please!")
    time.sleep(2)
    print("""
      Before you go, do you have any words you want to add?
   Maybe a word you would like to see become apart of the game
                      Then now is your change!""")
    time.sleep(0.7)
    question = input("""
           So do you have one or more? yes = y, no = n: """).lower().strip(' ')
    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
    time.sleep(0.3)

    while True:
        if question == "y":
            print("""
If more then one word then they should be separated by commas.
Up till 5 words is permitted.
E.g: Virgo,Libra,Aries,Leo,Cancer""")
            ideas = input("\nEnter your word/s here: ").strip(' ')
            ideas_value = ideas.split(",")

            if validatetion(ideas_value):
                if len(ideas) > 2:
                    print("\nThe words are valid!\n")
                else:
                    print("\nThe word is valid!\n")
        elif question == "n":
            print("\n                           Then on you go!")
            break
        else:
            print("\n                   I am sorry I didn't get that...")
            question = input("""
           So do you have one or more? yes = y, no = n: """).lower().strip(' ')
        return ideas_value


def validatetion(values):
    """
    Inside of the try, all string values converts into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there is more then 1 value for one word.
    """
    try:
        if len(values) > 5:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheets(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    if len(ideas) > 2:
        print("Sending words into review...\n")
    else:
        print("Sending word into review...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    if len(ideas) > 2:
        print("\nYour words is now up for review.\n")
    else:
        print("\nYour word is now up for review.\n")
    if len(ideas) > 2:
        print(f"Thank you for sending in the words: {ideas}\n")
    else:
        print(f"Thank you for sending in the word: {ideas}\n")


def send():
    """
    Run all program functions
    """
    data = new_words()
    ideas_value = [int(num) for num in data]
    update_worksheets(ideas_value, "ideas")
    # review.

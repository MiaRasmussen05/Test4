"""
Hi
"""
import time
import gspread
from google.oauth2.service_account import Credentials
from run import separator, play


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
#   while putting them on a spreadsheet for review
    Run a while loop to collect a valid string of words
    Until the string of words is valid the loop reapeats itself.
    1-5 words, separated by commas.
    """
    global ideas
    while True:
        if play == "n":
            print("\n                      Wait one second please!")
            time.sleep(2)
            print("""
      Before you go, do you have any words you want to add?
   Maybe a word you would like to see become apart of the game
                      Then now is your change!""")
            time.sleep(0.7)
            question = input("""
           So do you have one or more? yes = y, no = n: """).lower().strip(' ')
            separator()
            time.sleep(0.3)

            if question == "y":
                print("""
If more then one word then they should be separated by commas.
Up till 5 words is permitted.
E.g: Virgo,Libra,Aries,Leo,Cancer""")
                ideas = input("\nEnter your word/s here: ").strip(' ')
                ideas_value = ideas.split(",")

                if validatetion(ideas_value):
                    if len(ideas) > 2:
                        print("The words are valid!")
                    else:
                        print("The word is valid!")
                    break
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
    print(f"Thank you for sending in the word: {ideas}\n")


def words_main():
    """
    Run all program functions
    """
    data = new_words()
    ideas_value = [str(num) for num in data]
    update_worksheets(ideas_value, "ideas")


# def new_words():
#     """
#     Let the visitor give own ideas for new words
#     while putting them on a spreadsheet for review
#     """
#     global ideas
#     if play == "n":
#         print("                      Wait one second please!\n")
#         time.sleep(2)
#         print("""      Before you go, do you have any words you want to add?
#    Maybe a word you would like to see become apart of the game
#                       Then now is your change!""")
#         time.sleep(0.7)
#         question = input("""
#               So do you have one? yes = y, no = n: """).lower().strip(' ')
#         separator()
#         time.sleep(0.3)

#         while True:
#             if question == "n":
#                 ideas = input("\nEnter your word here: ").strip(' ')
#                 update_ideas_worksheet(ideas)
#                 time.sleep(1.2)
#                 print(f"Thank you for sending in the word: {ideas}\n")
#                 time.sleep(0.3)

#         while True:
#             if question == "y":
#                 ideas = input("\nEnter your word here: ").strip(' ')
#                 update_ideas_worksheet(ideas)
#                 time.sleep(1.2)
#                 print(f"Thank you for sending in the word: {ideas}\n")
#                 time.sleep(0.3)
#                 more = input("""
# D00o you have more? yes = y, no = n: """).lower().strip(' ')
#                 if more != "y":
#                     ideas = input("\nEnter your word here: ").strip(' ')
#                     update_ideas_worksheet(ideas)
#                     time.sleep(1.2)
#                     print(f"Thank you for sending in the word: {ideas}\n")
#                     more = input("""
# Do you have more? yes = y, no = n: """).lower().strip(' ')
#                 elif more != "n":
#                     print("\nThank you for sharing your words!")
#                     print("Please come back soon!")
#                     break

#                 else:
#                     print("\ninvalid character! Please try again!")
#                     more = input("""
# Do you have more? yes = y, no = n: """).lower().strip(' ')
#             elif question == "n":
#                 print("                           Then on you go!")
#                 break
#             else:
#                 print("\nI am sorry I didn't get that...")
#                 question = input("""
#               So do you have one? yes = y, no = n: """).lower().strip(' ')


# def stars():
#     """
#     Let the visitor give stars and review of the game
#     while putting them on a spreadsheet
#     """


# def validatation(value):
#     """
#     Inside of the try, all string values converts into integers.
#     # Raises ValueError if strings cannot be converted into int,
#     or if there is more then 1 value for one word.
#     """
#     try:
#         if value == ideas.isnumeric():
#             raise ValueError(
#                 f"A word is required, you provided {value}"
#             )
#     except ValueError:
#         pass


# def update_ideas_worksheet(data):
#     """
#     Update word ideas worksheet, add new row with the list data provided
#     """
#     update_words = SHEET.worksheet("ideas")
#     update_words.append_row([data])
#     print("\nYour word is now up for review.\n")


# new_words()

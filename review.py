"""
File to store the functions for the player to give the game stars
and a review if they want to.
"""
import time
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore
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


def stars():
    """
    Let the visitor give stars and review of the game
    while putting them on a spreadsheet
    """
    global classification
    first = Fore.WHITE + "  A" + Fore.YELLOW
    second = Fore.WHITE + r"/ \ " + Fore.YELLOW
    third = Fore.WHITE + r"_______/   \_______" + Fore.YELLOW
    forth = Fore.WHITE + r"'.                 .'" + Fore.YELLOW
    fifth = Fore.WHITE + r"'.             .'" + Fore.YELLOW
    sixth = Fore.WHITE + "'.         .'" + Fore.YELLOW
    seventh = Fore.WHITE + r"/    .^.    \ " + Fore.YELLOW
    eight = Fore.WHITE + r"/ . '     ' . \ " + Fore.YELLOW
    ninth = Fore.WHITE + r"/'             '\ " + Fore.YELLOW
    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
    print("Please take a second to give us a review!")
    print("Stars e.g: 2.7")
    classification = input("""
    Give stars here:\n""").strip(' ').replace(",", ".")
    time.sleep(0.4)
    if validate_data(classification):
        if classification >= 3:
            print(Fore.YELLOW + r"""
          A                      A                      A
         /*\                    /*\                    /*\
 _______/***\_______    _______/***\_______    _______/***\_______
'.*****************.'  '.*****************.'  '.*****************.'
  '.*************.'      '.*************.'      '.*************.'
    '.*********.'          '.*********.'          '.*********.'
    /****.^.****\          /****.^.****\          /****.^.****\
   /*. '     ' .*\        /*. '     ' .*\        /*. '     ' .*\
  /'             '\      /'             '\      /'             '\
        """ + Fore.WHITE)
        elif classification >= 2.8:
            print(Fore.YELLOW + fr"""
          A                      A                    {first}
         /*\                    /*\                    {second}
 _______/***\_______    _______/***\_______    {third}
'.*****************.'  '.*****************.'  '.*****************.'
  '.*************.'      '.*************.'      '.*************.'
    '.*********.'          '.*********.'          '.*********.'
    /****.^.****\          /****.^.****\          /****.^.****\
   /*. '     ' .*\        /*. '     ' .*\        /*. '     ' .*\
  /'             '\      /'             '\      /'             '\
    """ + Fore.WHITE)
        elif classification >= 2.5:
            print(Fore.YELLOW + fr"""
          A                      A                    {first}
         /*\                    /*\                    {second}
 _______/***\_______    _______/***\_______    {third}
'.*****************.'  '.*****************.'  {forth}
  '.*************.'      '.*************.'      {fifth}
    '.*********.'          '.*********.'          '.*********.'
    /****.^.****\          /****.^.****\          /****.^.****\
   /*. '     ' .*\        /*. '     ' .*\        /*. '     ' .*\
  /'             '\      /'             '\      /'             '\
    """ + Fore.WHITE)
        elif classification >= 2.3:
            print(Fore.YELLOW + fr"""
          A                      A                    {first}
         /*\                    /*\                    {second}
 _______/***\_______    _______/***\_______    {third}
'.*****************.'  '.*****************.'  {forth}
  '.*************.'      '.*************.'      {fifth}
    '.*********.'          '.*********.'          {sixth}
    /****.^.****\          /****.^.****\          {seventh}
   /*. '     ' .*\        /*. '     ' .*\        /*. '     ' .*\
  /'             '\      /'             '\      /'             '\
    """ + Fore.WHITE)
        elif classification >= 2:
            print(Fore.YELLOW + fr"""
          A                      A                    {first}
         /*\                    /*\                    {second}
 _______/***\_______    _______/***\_______    {third}
'.*****************.'  '.*****************.'  {forth}
  '.*************.'      '.*************.'      {fifth}
    '.*********.'          '.*********.'          {sixth}
    /****.^.****\          /****.^.****\          {seventh}
   /*. '     ' .*\        /*. '     ' .*\        {eight}
  /'             '\      /'             '\      {ninth}
    """ + Fore.WHITE)
        elif classification >= 1.8:
            print(Fore.YELLOW + fr"""
          A                    {first}                    {first}
         /*\                    {second}                   {second}
 _______/***\_______    {third}    {third}
'.*****************.'  '.*****************.'  {forth}
  '.*************.'      '.*************.'      {fifth}
    '.*********.'          '.*********.'          {sixth}
    /****.^.****\          /****.^.****\          {seventh}
   /*. '     ' .*\        /*. '     ' .*\        {eight}
  /'             '\      /'             '\      {ninth}
    """ + Fore.WHITE)
        elif classification >= 1.5:
            print(Fore.YELLOW + fr"""
          A                    {first}                    {first}
         /*\                    {second}                   {second}
 _______/***\_______    {third}    {third}
'.*****************.'  {forth}  {forth}
  '.*************.'      {fifth}      {fifth}
    '.*********.'          '.*********.'          {sixth}
    /****.^.****\          /****.^.****\          {seventh}
   /*. '     ' .*\        /*. '     ' .*\        {eight}
  /'             '\      /'             '\      {ninth}
    """ + Fore.WHITE)
        elif classification >= 1.3:
            print(Fore.YELLOW + fr"""
          A                    {first}                    {first}
         /*\                    {second}                   {second}
 _______/***\_______    {third}    {third}
'.*****************.'  {forth}  {forth}
  '.*************.'      {fifth}      {fifth}
    '.*********.'          {sixth}          {sixth}
    /****.^.****\          {seventh}         {seventh}
   /*. '     ' .*\        /*. '     ' .*\        {eight}
  /'             '\      /'             '\      {ninth}
    """ + Fore.WHITE)
        elif classification >= 1:
            print(Fore.YELLOW + fr"""
          A                    {first}                    {first}
         /*\                    {second}                   {second}
 _______/***\_______    {third}    {third}
'.*****************.'  {forth}  {forth}
  '.*************.'      {fifth}      {fifth}
    '.*********.'          {sixth}          {sixth}
    /****.^.****\          {seventh}         {seventh}
   /*. '     ' .*\        {eight}       {eight}
  /'             '\      {ninth}     {ninth}
    """ + Fore.WHITE)
        elif classification >= 0.8:
            print(Fore.YELLOW + fr"""
        {first}                    {first}                    {first}
         {second}                   {second}                   {second}
 {third}    {third}    {third}
'.*****************.'  {forth}  {forth}
  '.*************.'      {fifth}      {fifth}
    '.*********.'          {sixth}          {sixth}
    /****.^.****\          {seventh}         {seventh}
   /*. '     ' .*\        {eight}       {eight}
  /'             '\      {ninth}     {ninth}
    """ + Fore.WHITE)
        elif classification >= 0.5:
            print(Fore.YELLOW + fr"""
        {first}                    {first}                    {first}
         {second}                   {second}                   {second}
 {third}    {third}    {third}
{forth}  {forth}  {forth}
  {fifth}      {fifth}      {fifth}
    '.*********.'          {sixth}          {sixth}
    /****.^.****\          {seventh}         {seventh}
   /*. '     ' .*\        {eight}       {eight}
  /'             '\      {ninth}     {ninth}
    """ + Fore.WHITE)
        elif classification >= 0.3:
            print(Fore.YELLOW + fr"""
        {first}                    {first}                    {first}
         {second}                   {second}                   {second}
 {third}    {third}    {third}
{forth}  {forth}  {forth}
  {fifth}      {fifth}      {fifth}
    {sixth}          {sixth}          {sixth}
    {seventh}         {seventh}         {seventh}
   /*. '     ' .*\        {eight}       {eight}
  /'             '\      {ninth}     {ninth}
    """ + Fore.WHITE)
        elif classification >= 0:
            print(Fore.YELLOW + fr"""
        {first}                     {first}                    {first}
         {second}                    {second}                   {second}
 {third}     {third}    {third}
{forth}   {forth}  {forth}
  {fifth}       {fifth}      {fifth}
    {sixth}           {sixth}          {sixth}
    {seventh}          {seventh}         {seventh}
   {eight}        {eight}       {eight}
  {ninth}      {ninth}     {ninth}
    """ + Fore.WHITE)
        else:
            print("I am sorry, but that is not a valid number.")
            return stars()


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        if not values.isnumeric():
            raise ValueError("Input must be a number")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


review_text = ""


def review():
    """
    Function for input of the review
    """
    global review_text

    print("Do you want to send a review with you grade?")
    question_review = input("""
           Do you want to send one? yes = y, no = n:\n""").lower().strip(' ')
    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
    time.sleep(0.3)
    while True:
        if question_review == "y":
            review_text = input("Enter your review here:\n")
            update_review_worksheets()
        elif question_review == "n":
            update_review_worksheets()
            print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
            time.sleep(1.7)
            print("                           Then on you go!")
            break
        else:
            print("                   I am sorry I didn't get that...")
            question_review = input("""
           Do you want to send one? yes = y, no = n:\n""").lower().strip(' ')
        return review_text


def update_review_worksheets():
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print("\nSending in your review...\n")

    worksheet_to_update = SHEET.worksheet("stars")
    worksheet_to_update.append_row([classification, review_text])

    print("Thank you for sending in a review!\n")


def star_review():
    """
    Hi
    """
    stars()
    print("""
-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-
        """)
    review()


star_review()

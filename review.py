"""
File to store the functions for the player to give the game stars
and a review if they want to.
"""

import colorama
from colorama import Fore
colorama.init()


def stars():
    """
    Let the visitor give stars and review of the game
    while putting them on a spreadsheet
    """
    first = Fore.WHITE + "  A" + Fore.YELLOW
    second = Fore.WHITE + r"/ \ " + Fore.YELLOW
    third = Fore.WHITE + r"_______/   \_______" + Fore.YELLOW
    forth = Fore.WHITE + r"'.                 .'" + Fore.YELLOW
    fifth = Fore.WHITE + r"'.             .'" + Fore.YELLOW
    sixth = Fore.WHITE + "'.         .'" + Fore.YELLOW
    seventh = Fore.WHITE + r"/    .^.    \ " + Fore.YELLOW
    eight = Fore.WHITE + r"/ . '     ' . \ " + Fore.YELLOW
    ninth = Fore.WHITE + r"/'             '\ " + Fore.YELLOW
    print("Please take a second to give us a review!")
    print("Stars e.g: 2.7")
    how_many_stars = int(float(input("""
    Give stars here: """).strip(' ')))
    if how_many_stars == 3:
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
    elif how_many_stars >= 2.8:
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
    elif how_many_stars >= 2.5:
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
    elif how_many_stars >= 2.3:
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
    elif how_many_stars >= 2:
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
    elif how_many_stars >= 1.8:
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
    elif how_many_stars >= 1.5:
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
    elif how_many_stars >= 1.3:
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
    elif how_many_stars >= 1:
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
    elif how_many_stars >= 0.8:
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
    elif how_many_stars >= 0.5:
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
    elif how_many_stars >= 0.3:
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
    elif how_many_stars >= 0:
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

def main():
    """
    hi
    """
    stars()


main()

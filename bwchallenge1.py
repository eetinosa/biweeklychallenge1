#!/usr/bin/env python3
"""
Author : etinosa <etinosa@localhost>
Date   : 2020-11-04
Purpose: How old are you?
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get the inputs"""

    parser = argparse.ArgumentParser(
        description='How old are you?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

   
    parser.add_argument('name',
                        metavar='str',
                        help='What is your name?')

    
    parser.add_argument('age',
                        help='How old are you?',
                        metavar='int',
                        type=int,
                        default=0)
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Let's make magic"""

    args = get_args()
    name = args.name
    age = args.age

    DOB = 2020 - age #Calculating the Date of Birth

    age_group = ''   #Determine the Age Group
    if age < 1: 
        age_group = 'infant'
    if age < 11:
        age_group = 'child'
    if age < 18:
        age_group = 'teen'
    if age > 18:
        age_group = 'adult'
    if age > 65:
        age_group = 'elderly'

    article = "an" if age_group[0].lower() in "aeiou" else "a" #to ensure good grammar with appropriate article
    
    print (f'''Hello {name}, you are {age} years old, 
    Your year of birth is {DOB}. 
    As you are {age} years old , you are {article} {age_group}.
    ''')

    present_year = 2020
    for x in range (-10,60,10):
        year = present_year + x
        age2 = age + x
        article2 = "were" if year < present_year  else "will be"
        print (f'In {year}, you {article2}  {age2} years old.')


#--------------------------------------------------
if __name__ == '__main__':
    main()

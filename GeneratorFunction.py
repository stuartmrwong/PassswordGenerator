# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:24:11 2019

@author: Stuart
"""

"""
Challenge 56 of the Pro/g/ramming challenges v4.0
Password generator, let the user choose the options
"""

"""
password should be random and contain alphanumeric and special characters
"""

import string
import random

def createpassword(length, chars):
    return ''.join(random.choices(chars, k=length))
    
while True:
    
    print('What is the desired length of the password? 21 characters is suggested')
    desiredlength = int(input())
    print('Do you want uppercase letters, numbers and special characters? Y/N')
    case = input()
    if case.upper() == 'Y':
        print(createpassword(desiredlength, string.ascii_letters + string.digits + string.punctuation))
        break
    if case.upper() == 'N':
        print(createpassword(desiredlength, string.ascii_lowercase))
        break
    print('Something went wrong, try again')
    

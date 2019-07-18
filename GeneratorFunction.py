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

import string #importing the string module so i have more string methods
import random #importing the random module 

def createpassword(length, chars): #creating a function that takes length and chars as parameters
    return ''.join(random.choices(chars, k=length)) #return a string that is the joining of a random set of 'chars', with the length of 'length'
    
while True: #starting a while loop to create user choices
    
    print('What is the desired length of the password? 21 characters is suggested')
    desiredlength = int(input()) #create the desiredlength variable by converting the response to a integer
    print('Do you want uppercase letters, numbers and special characters? Y/N')
    case = input()
    if case.upper() == 'Y': #if they say yes then print a complicated password
        print(createpassword(desiredlength, string.ascii_letters + string.digits + string.punctuation))
        break #end the loop
    if case.upper() == 'N': #if they say no then print a simple password
        print(createpassword(desiredlength, string.ascii_lowercase + string.digits))
        break 
    print('Something went wrong, try again') #if the user doesn't respond y or n print this message and start the loop over
    

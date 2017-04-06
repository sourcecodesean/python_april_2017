# -*- coding: utf-8 -*-
"""
Python Fundamentals Assignment

Autho: Jason Lee

"""


### Prints out *

def draws_stars(list):
    for element in list:
        number_of_stars =""
        for i in range(element):
            number_of_stars += "*"
        
        print number_of_stars
        
        
### Print out alphabets & stars

def draw_starsTwo(list):
    number_of_literals = ""
    
    for element in list:
        if(type(element) == int):
            for i in range(element):
                number_of_literals += "*"
            
        if(type(element) == str):
            for i in range(len(element)):
                number_of_literals += element[0].lower()
        print number_of_literals
            

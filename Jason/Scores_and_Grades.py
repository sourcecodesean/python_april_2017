# -*- coding: utf-8 -*-
"""
Python Fundamentals Assignment

Autho: Jason Lee

"""
import random



print("Scores and Grades")

for scores in range(0,10):
    random_score = round(random.random()*40+60) 
    if(random_score >= 90 and random_score <= 100):
        grade = "A"
    elif(random_score >= 80 and random_score<89):
        grade = "B"
    elif(random_score >= 70 and random_score<79):
        grade = "9"
    elif(random_score >= 60 and random_score<69):
        grade = "D"
        
        
        
    print "Score: " + str(random_score) + "; Your grade is " + grade

print "End of the program. Bye!"


                          



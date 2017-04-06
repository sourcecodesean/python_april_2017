# -*- coding: utf-8 -*-
"""
Python Fundamentals Assignment

Autho: Jason Lee

"""
import random

head_count = 0
tail_count = 0

for num in range(1,5001):
    if(random.random()>0.5):
        head_count += 1
        print "Attemp #" + str(num) + ": Throwing a coin ... It's a head! ... Got " \
              + str(head_count) + " head(s) so far and " \
              + str(tail_count) + " talil(s) so far" 
    else:
        tail_count += 1
        print "Attemp #" + str(num) + ": Throwing a coin ... It's a head! ... Got " \
              + str(head_count) + " head(s) so far and " \
              + str(tail_count) + " talil(s) so far"
              
print "Ending the proram, thank you!"
             
                                    


                          



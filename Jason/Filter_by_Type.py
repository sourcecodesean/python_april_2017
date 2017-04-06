# -*- coding: utf-8 -*-
"""
Python Fundamentals Assignment

Autho: Jason Lee

"""
from types import *

def filter_by_type(item):
    
    if(isinstance(item,type(1))==True):
        if(item >= 100):
           print "That's a big number."
        else:
            print "That's a small number."
            
    if(isinstance(item,type(" "))==True):
        if(len(item) >= 50):
            print "Long sentence."
        else:
            print "Short sentence."
        
    if(isinstance(item, type([]))==True):
        if(len(item) >= 10):
            print "Big list!"
        else:
            print "Short list."
    
    int
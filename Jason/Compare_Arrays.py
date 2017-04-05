# -*- coding: utf-8 -*-
"""
Python Fundamentals Assignment

Autho: Jason Lee

"""

def compare_arrays(arr1, arr2):
    count = 0
    if(len(arr1)!=len(arr2)):
        print "The lists are not the same"
        return
    
    else:
        for i in range(0,len(arr1)):
            if(arr1[i]==arr2[i]):
                count += 1

    if(count!=0):
        print "The lists are the same."
    
    elif(count==0):
        print "The lists are not the same."
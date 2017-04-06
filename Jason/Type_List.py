# -*- coding: utf-8 -*-
"""
Python Fundamentals Assignment

Autho: Jason Lee

"""


def type_list(list):
    
    sum = 0
    string = ""
    for element in list :
        if(isinstance(element,type("abd)"))):
            string+=element
            
        if(isinstance(element,type(1))):
            sum += element
            
    


    if(len(string)!=0 and sum!=0):
            return ("The array you entered is of mixed type","String: " + string ,  "Sum: " + str(sum)) 
            
    if(len(string)==0 and sum!=0):
            return ("The array you entered is of intger type", '',  "Sum: " + str(sum))
        
    if(len(string)!=0 and sum==0):
            return ("The array you entered is of string type", "String: " + string ,'')


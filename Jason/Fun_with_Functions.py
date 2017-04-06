# -*- coding: utf-8 -*-
"""
Python Fundamentals Assignment

Autho: Jason Lee

"""
### Odd/Even

odd_even = ""

for num in range(1,2001):
    if(num%2 == 0):
        odd_even = "even"
    elif(num%2 !=0):
        odd_even = "odd"    
    print("Number is " + str(num) +". This is an " + odd_even + "number.")
    

def multiply(list, number):
    for element in list:
        element=element*number
    return list

def multiplyOne(list, number):
    new_list=[]
    for element in list:
        new_list.append(element*number)
    return new_list


def binary(num):
    binary_num =""
    power = 1
    while power < num/2:
        power *= 2
    
    while power > 0:    
        if(num < power):
            binary_num += "0"
            power /= 2
        
        else:
            binary_num += "1"
            num -= power
            power /= 2
        
    return binary_num 


def layered_multiples(arr):
    for index in range(len(arr)):
        arr[index] = binary(arr[index])
    return arr
    

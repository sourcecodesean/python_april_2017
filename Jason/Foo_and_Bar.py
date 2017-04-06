# -*- coding: utf-8 -*-
"""
Python Fundamentals Assignment

Autho: Jason Lee

"""
def isPrime(n):
    multiple = 2
    count = 0
    while(multiple*multiple <= n):
        if(n%multiple == 0):
            count +=1
        multiple +=1
    if(count == 0):
        print "Prime"
        return True
    else:
        print "not prime"
        return False
        
isPrime(7)

def prime_and_perfect_squares():
    for number in range(100,100001):
        if (isPrime(number)==True):
            print "Foo"
        
        elif (number in [ix**2 for ix in range(1,101)]):
            print "Bar"
            
            
        else:
            print "FooBar"

        
    


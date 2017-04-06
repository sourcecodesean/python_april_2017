# -*- coding: utf-8 -*-
"""
Python Fundamentals Assignment

Autho: Jason Lee

"""

### Print multiples

for num in range(1,1000):
    if(num%2 != 0):
        print num
i = 1
while(5*i <1000000):
    print 5*i
    i+=1
    


### Sum list
a = [1, 2, 5,10, 255,30]
sum = 0    
for num in a:
    sum += num


### Average List
a = [1, 2, 5,10, 255,30]
sum = 0    
for num in a:
    sum += num

avg = sum/len(a)
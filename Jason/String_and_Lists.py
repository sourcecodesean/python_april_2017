# -*- coding: utf-8 -*-
"""
Python Fundamentals Assignment
String and List Practice

Autho: Jason Lee

"""

### Find the first instance fo the world "day" & creat a new string replacing word "day" with the word "month"
str = "It's thanksgiving day. It's my birthday, too!" 
pieces = [x.strip() for x in str.split(' ')]
str.find("day")
str.replace("day","month")


### Min and Max
x = [2, 54, -2, 7, 12, 98]
max = x[0]
min = x[0]

for i in range(1,len(x)-1):
    if(max < x[i]):
        max = x[i]
    if(min > x[i]):
        min = x[i]
print max, min

### First and Last
x = ["hello", 2, 54, -2,7,12,98, "world"]
first = x[0]
last = x[len(x)-1]
print first, last


new_list=x[len(x)/2-1:len(x)-1]
new_list.insert(0,x[0:len(x)/2])


# -*- coding: utf-8 -*-
"""
Python Fundamentals Assignment

Autho: Jason Lee

"""

Profile = {}
Profile["name"] = "Batman"

Profile["age"] = "101"

Profile["country of birth"] = "Gotham"

Profile["favorite language"] = "Python"

info = ["name","age","country of birth","favorite language"]
       
for information in info:
    print "My "+ information + "is " + Profile[information]
       


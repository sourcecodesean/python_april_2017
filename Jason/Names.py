# -*- coding: utf-8 -*-
"""
Python Fundamentals Assignment

Autho: Jason Lee

"""

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for dictionary in students:
    print dictionary["first_name"] + " " + dictionary["last_name"]

       

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


for layerOne in ["Students","Instructors"]:
    print layerOne
    for key in range(len(users[layerOne])):
        print str(key+1) + " - " + users[layerOne][key]["first_name"].upper() + " " + users[layerOne][key]["last_name"].upper() \
              + " - " + str(len(users[layerOne][key]["first_name"]) + len(users[layerOne][key]["last_name"]))
              
  


          


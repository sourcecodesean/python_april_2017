# -*- coding: utf-8 -*-
"""
Python OOP Assignment

Author: Jason Lee

"""

class Animal(object):
	def __init__(self, name, health=100):
		self.name = name
		self.health = health

	def walk(self):
		self.health -= 1


	def run(self):
		self.health -= 5


	def displayHealth(self):
		print "this is a " + self.name + "!"
		print self.health

class Dog(Animal):
	def __init__(self,name, health=150, color=""):
		super(Animal, self).__init__(self,name,health)
		self.color = color

	def pet(self):
		self.health += 5


class Dragon(Animal):
	def __init__(self,name, health=170):
		Animal.__init__(self,name,health)

	def fly(self):
		self.health -= 10




Animal1=Animal("Zebra",120)
Animal1.walk()
Animal1.walk()
Animal1.walk()
Animal1.run()
Animal1.run()
Animal1.displayHealth()

Dragon1=Dragon("Red Dragon",120)
Dragon1.walk()
Dragon1.walk()
Dragon1.walk()
Dragon1.run()
Dragon1.run()
Dragon1.fly()
Dragon1.fly()
Dragon1.displayHealth()

Animal2 = Animal("Elephant",100)
Animal2.pet()
Animal2.fly()


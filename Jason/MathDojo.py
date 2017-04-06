# -*- coding: utf-8 -*-
"""
Python OOP Assignment

Author: Jason Lee

"""

class MathDojo(object):
	def __init__(self):
		self.result=0
	def add(self, *args):
		for arg in args:
			if(type(arg)==int):
				self.result += arg
			elif type(arg) in (list,tuple):
				self.result += sum(arg)

		return self

	def subtract(self, *args):
		for arg in args:
			if(type(arg)==int):
				self.result -= arg
			elif type(arg) in (list,tuple):
				self.result -= sum(arg)

		return self
	def result(self):
		print self.result

print MathDojo().add(1).add(2,4.3,1.25).subtract(1.1,2.3).result

print MathDojo().add(1).add([2,4.3,1.25]).subtract((1.1,2.3)).result

# MathDojo().add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3])


# -*- coding: utf-8 -*-
"""
Python OOP Assignment

Author: Jason Lee

"""

class Call(object):
	def __init__(self, id, name, phone_num, time, reason):
		self.id = id
		self.name = name
		self.phone_num = phone_num
		self.time = time
		self.reason = reason
	
	def display(self):
		print self.id
		print self.name
		print self.phone_num
		print self.time
		print self.reason


Call1 = Call(123,"Jason", "405-339-3086", "14:00 AM" , "emergency")
Call2= Call(123,"Jason", "405-339-3086", "14:00 AM" , "emergency")
Call3 = Call(123,"Jason", "405-339-3086", "14:00 AM" , "emergency")
Call4 = Call(123,"Jason", "405-339-3086", "14:00 AM" , "emergency")
print Call1.time
Call1.display()

class CallCenter(Call):
	def __init__(self, *calls):
		print calls
		self.call_list = calls
		self.queue_size = len(self.call_list)

	def add(self,new):
		self.call_list.append(self.new)

	def remove(self):
		self.call_list.pop(0)

	def info(self):
		for call in call_list:
			print "{} {}".format(call.name, call.phone_num)
		print self.queue_size

import random

list =[1,2,3,4]
print random.shuffle(list)


# # class CallCenter(object):
# # 	def __init__(self, )

CallCenter1=CallCenter(Call1,Call2,Call3,Call4)
CallCenter1.call_list
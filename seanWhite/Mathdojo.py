class MathDojo(object):
	"""docstring for MathDojo"""
	def __init__(self):
		self.sum = 0

	def add(self, *numbers):
		for x in numbers:
			self.sum += x
		return self

	def subtract(self, *numbers):
		for x in numbers:
			self.sum -= x
		return self

	def result(self):
		print self.sum

md = MathDojo()
md.add(2).add(2, 5).subtract(3, 2).result()

#this is part two of the MathDojo

class MathDojo2(object):
	def __init__(self):
		self.sum = 0
	def add(self, *args):
		for x in args:
			if type(x) is list:
				for i in x:
					self.sum += i
			elif type(x) is int:
				self.sum += x
		return self
	def subtract(self, *args):
		for x in args:
			if type(x) is list:
				for i in x:
					self.sum -= i
			elif type(x) is int:
				self.sum -= x
		return self
	def result(self):
		print self.sum

md2 = MathDojo2()
md2.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()



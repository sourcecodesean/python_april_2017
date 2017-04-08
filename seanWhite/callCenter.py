class call(object):
	"""docstring for call_center"""
	def __init__(self, idNum, name, phoneNumber, time, reason):
 		self.idNum = idNum
		self.name = name
		self.phoneNumber = phoneNumber
		self.time = time
		self.reason = reason

	def display_all(self):
		print self.idNum
		print self.name
		print self.phoneNumber
		print self.time
		print self.reason

samsquanch = call(123, "Mr. Samsquanch", 888555444, "noon", "on fire")
samsquanch2 = call(124, "Mrs. Samsquanch", 888555444, "noon:30", "hungry")
samsquanch3 = call(125, "Dr. Samsquanch", 888555444, "12:05 AM", "cat in tree")
samsquanch4 = call(126, "Md. Samsquanch", 888555444, "4:20 PM", "lost in my own head")
samsquanch.display_all()

class call_center(call):
	"""second class with the inheritence of class call()"""
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


this1 = call_center(samsquanch,samsquanch2,samsquanch3,samsquanch4)
this1.call_list
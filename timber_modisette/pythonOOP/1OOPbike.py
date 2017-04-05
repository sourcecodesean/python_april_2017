class Bike(object):
	def __init__(self, price, max_speed, miles=0):
		self.price =price
		self.max_speed =max_speed
		self.miles =miles

	def displayinfo(self):
		print "Price:{} Max speed:{} Miles:{}".format(self.price, self.max_speed, self.miles)

	def ride(self,num):
		print "riding "*num
		self.miles = self.miles + (10*num) 
	
		
	def reverse(self, num):
		print "reversing " * num
		self.miles = self.miles - (5*num)
		if self.miles < 0:
			self.miles = 0



bicycle = Bike("400", "20",)
bicycle.ride(3)
#bicycle.ride()
#bicycle.ride()
bicycle.reverse(1)
bicycle.displayinfo()

bicycle2 = Bike("500", "20")
bicycle2.ride(2)
#bicycle2.ride()
#bicycle2.reverse()
bicycle2.reverse(2)
bicycle2.displayinfo()

bicycle3 = Bike("1000", "20")

bicycle3.reverse(3)
#bicycle3.reverse()
#bicycle3.reverse()
bicycle3.displayinfo()

class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		

		if self.price < 10000:
			self.tax = "0.12%"
		else:
			self.tax = "0.15%"
		self.displayAll()
	def displayAll(self):
		print "price:${} speed: {}mph fuel: {} mileage: {}mpg the tax will be {}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)



car1 = Car(10, "200", "unleaded", "30" )
car2 = Car(20, "150", "unleaded", "30")
car3 = Car(30, "300", "unleaded", "30")
car4 = Car(40, "1500", "diseal", "10")
car5 = Car(250, "1520", "unleaded", "30")
car6 = Car(29000, "15", "unleaded", "30")
#car1.displayAll()


#if price is > 10,000 tax will be 15% else tax will be 12%
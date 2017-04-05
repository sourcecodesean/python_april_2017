class Bike(object):
  # the  __init__method is called every time a new object is created

  def __init__(self, price, speed, fuel, mileage):
  	#set some instances variables
  	self.price = price
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage

  	# set so


  def displayinfo(self):
  	print self.price
  	print self.max_speed
  	print self.miles
  	return self

  def ride(self):
  	print "Riding"
  	self.miles += 5
  	return self
  	
  def reverse(self):
  	print "Reversing"
  	self.miles -= 5
  	return self

Bike1 = Bike(200,"25mph")
Bike1.ride()
Bike1.ride()
Bike1.ride()
Bike1.reverse()
Bike1.displayinfo()
Bike1.ride().displayinfo()
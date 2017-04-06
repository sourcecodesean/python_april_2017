class Car(object):
  # the  __init__method is called every time a new object is created

	def __init__(self, price, item_name, weight, brand, cost, status= "for sale"):
  	#set some instances variables
 
		self.price = price
	  	self.item_name = item_name
	  	self.weight = weight
	  	self.brand = brand
	  	self.cost = cost
	  	self.status = status
	  	return self

  	# set so


  	def sell(self):
	  	self.Status = "sold"
		return self

  	def add_tax(self):
  		self.tax = 0.05*self.price
  		return self.price + self.tax

  	def Return(self,reason):
	  	if(self.reason.lower.find("defective") != -1):
	  		self.status = "defective"
	  		self.price = 0
	  	elif all(check in reason for check in ["box","returned"]):
	  		self.status = "for sale"
	  		self.price = 0
	  	elif all(check in reason for check in ["box","opened"]):
	  		self.status = "used"
	  		self.price = self.price*(1-0.2)
	  	return self

	def diplay_info(self):
	  	print self.Price
	  	print self.Item_Name
	  	print self.Weight
	  	print self.Brand
	  	print self.Cost
	  	print self.Status
	  	return self



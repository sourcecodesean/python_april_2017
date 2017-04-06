# -*- coding: utf-8 -*-
"""
Python OOP Assignment

Author: Jason Lee

"""

### Create class of Product
class Product(object):

	def __init__(self, price, item_name, weight, brand, cost, status= "for sale"):
 		self.price = price
	  	self.item_name = item_name
	  	self.weight = weight
	  	self.brand = brand
	  	self.cost = cost
	  	self.status = status

  	def sell(self):
	  	self.Status = "sold"
		return self

  	def add_tax(self):
  		self.tax = 0.05*self.price
  		return self.price + self.tax

  	def Return(self,reason):
	  	if self.reason.lower.find("defective") != -1:
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
	  	print self.price
	  	print self.item_name
	  	print self.weight
	  	print self.brand
	  	print self.cost
	  	print self.status
	  	return self

product1=Product(10,"apple",1,"Sun",6,)
product2=Product(20,"orange",2,"Moon",7,)
product2=Product(30,"TV",3,"Retail",20,)


class Store(object):
	def __init__(self,products,location,owner):
		self.products = products
		self.location = location
		self.owner = owner

	def add_product(self,product):
		self.products.append(product)

	def remove_product(self,product):
		self.products.remove(product)

	def inventory(self):
		for product in products:
			print "{} {} {}".format(product.price,product.item_name,product.weigh,product.brand,product.cost,product.status)

store1 = Store([],"Dallas","LEE")
store1.add_product(product1)
store1.add_product(product2,product3)
print "{} {} {}".format(store1.products,store1.location,store1.owner)




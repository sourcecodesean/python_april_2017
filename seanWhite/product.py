class product(object):
    
    def display_all(self):
        print "Price: $" + str(self.price)
        print "Name: " + str(self.name)
        print "Weight: " + str(self.weight) + "lbs"
        print "Brand: " + str(self.brand)
        print "Cost: $" + str(self.cost)
        print "Status: " + str(self.status)
        print " "

    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"

        self.display_all()

    def sell(self):
        self.status = "Sold"
        return self

    def addtax(self, tax):
        self.price *= (tax + 1)
        return self

    def weeturn(self, p):
        if p == "defective":
            self.status = "Defective Item"
            self.price = 0
        elif p == "opened":
            self.status = "Used"
            self.price *= .8
        else:
            self.status = "For Sale"
        return self

Product1 = product(1.99, "taco", 1, "soyrizo", 2.00)
Product2 = product(15.49,  "Alaskan TF", 0.125, "Hybrid", 45)
Product3 = product(10.00,  "T-shirt", 0, "Haitian Slave Labor", "your soul")


Product1.addtax(.1).sell().weeturn("opened").display_all()
Product2.addtax(.51).sell().weeturn("okay").display_all()
Product3.addtax(.2).sell().weeturn("defective").display_all()


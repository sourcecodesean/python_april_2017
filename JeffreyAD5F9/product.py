
class Product(object):

    def display(self):
        print "Price: $" + str(self.price)
        print "Name: " + str(self.name)
        print "Weight: " + str(self.weight) + "lbs"
        print "Brand: " + str(self.brand)
        print "Cost: $" + str(self.cost)
        print "Status: " + str(self.status)
        print " "

    def __init__(self,x, y, z, o, s):
        self.price = x
        self.name = y
        self.weight = z
        self.brand = o
        self.cost = s
        self.status = "For Sale"


    def sell(self):
        self.status = "Sold"
        return self

    def addtax(self, t):
        self.price *= (t + 1)
        return self

    def ret(self, ex):
        if ex == "defective":
            self.status = "Defective Item"
            self.price = 0
        elif ex == "opened":
            self.status = "Used"
            self.price *= .8
        else:
            self.status = "For Sale"
        return self


Product1 = Product(120.00, "TV", 10.6, "Samsung", 78.00)
Product2 = Product(10.00,  "Goggles", 1.8, "Hydro", 4.50)
Product3 = Product(5.69,  "Shoes", 2.0, "Siker", 2.10)


Product1.addtax(.1).sell().ret("opened").display()
Product2.addtax(.51).sell().ret("okay").display()
Product3.addtax(.2).sell().ret("defective").display()

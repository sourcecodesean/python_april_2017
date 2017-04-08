class Bike(object):
    def __init__(self,price, speed, miles):
        self.price = price
        self.speed = speed
        self.miles = miles

    def display(self):
        print "Price: $" + str(self.price)
        print "Maximum Speed: " + str(self.speed) + " mph"
        print "Miles: " + str(self.miles)


    def ride(self):
        print "Riding VRROOOOOM"
        self.miles += 20
        return self

    def reverse(self):
        print "Reversing, watch out..."
        self.miles -= 20
        if self.miles<0:
            self.miles = 0
        return self

Bike1 = Bike(120, 45, 0)
Bike2 = Bike(200, 55, 0)
Bike3 = Bike(99, 40, 0)

Bike1.ride().ride().ride().reverse().display()
Bike2.ride().ride().reverse().display()
Bike3.reverse().reverse().reverse().display()
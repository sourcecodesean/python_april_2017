class Car(object):
    
    def display_all(self):
        print "Price: $" + str(self.price)
        print "Speed: " + str(self.speed) + " mph"
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage)
        print "Goverments cut: " + str(self.tax)
        print " "

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = .12
        if self.price>10000:
            self.tax = .15
        self.display_all()
                

car1 = Car(30000, 60, "the most fuel", 500)
car2 = Car(5000, 200, "fumes", 50)
car3 = Car(34000, 190, "half-fuel", 500)
car3 = Car(32000, 167, "yo, get some gas", 50)
car4 = Car(18000, 122, "3/4 fuel", 500)
car5 = Car(6000, 640, "half empty", 50)
car6 = Car(60000, 600, "half empty", 500)



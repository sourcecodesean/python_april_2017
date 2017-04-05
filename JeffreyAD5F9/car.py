
class Car(object):

    def display(self):
        print "Price: $" + str(self.price)
        print "Speed: " + str(self.speed) + " mph"
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + " mpg"
        print "Tax: " + str(self.tax)
        print " "

    def __init__(self,x, y, z, o):
        self.price = x
        self.speed = y
        self.fuel = z
        self.mileage = o
        self.tax = .12
        if self.price>10000:
            self.tax = .15

        self.display()

Car1 = Car(12000, 45, "Full", 15)
Car2 = Car(10000, 35, "Not Full", 12)
Car3 = Car(9000, 15, "Kind of Full", 10)
Car4 = Car(22000, 50, "Full", 25)
Car5 = Car(9900, 30, "Empty", 13)
Car6 = Car(10200, 19, "Half Full", 16)





#Bike1.ride().ride().ride().reverse().display()

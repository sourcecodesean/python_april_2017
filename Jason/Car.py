class Car(object):
  # the  __init__method is called every time a new object is created

  def __init__(self, price, speed, fuel,mileage):
    #set some instances variables
    self.price = price
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage
    if self.price > 10000:
      self.tax = 0.15
    else:
      self.tax = 0.12

    # set so


  def display_all(self):
    print self.price
    print self.speed
    print self.fuel
    print self.mileage
    print self.tax


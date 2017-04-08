class Animal(object):
    def display_health(self,):
        print "Animal name: " + str(self.name)
        print "Health: " + str(self.health)
        return self

    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
        self.display_health()
        
    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self


class Dog(Animal):
    def __init__(self, name, health = 150):
        super(Dog, self).__init__(name, health)
    
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health = 170):
        super(Dragon, self).__init__(name, health)
    
    def fly(self):
        self.health -= 10
        return self


samsquanch = Animal("sammy")
samsquanch.walk().walk().walk().run().run().display_health()

doggie = Dog("Barky")
doggie.walk().walk().walk().run().run().pet().display_health()

dragon = Dragon("Rex")
dragon.walk().walk().walk().run().run().fly().fly().display_health()
from random import random

def getReading(min, max):
    range = abs(max - min)
    return (random() * range) + min

class Sensor:
    def __init__(self,id,location):
        self.id = id
        self.location = location
    def getId(self):
        return self.id
    def printLocation(self):
        print("Location: ", self.location)
    def printReading(self):
        reading = int(getReading(0, 100))
        print("Sensor reading:  ", reading)



sensor1 = Sensor("sensor1", "Lahti")

sensor1.printLocation()

sensor1.printReading()
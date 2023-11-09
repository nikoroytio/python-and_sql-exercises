from operator import truediv
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

class TempSensor(Sensor):

    def printTemp(self):
        reading = float(getReading(-99, -1))
        print("Temp: {:.1f} °C".format(reading))

class Humiditysensor(Sensor):

    def printHumidity(self):
        reading = int(getReading(0, 100))
        print("humidity: ", reading, "%")

class PIR_sensor(Sensor):

    def printPIR(self):
        reading = int(getReading(0, 100))
        if reading < 50:
            print("Movement NO")
        else:
            print(" Movement: YES")

    def printReading(self):
        reading = int(getReading(0, 100))
        if reading < 50:
            print("Movement NO")
        else:
            print("Movement: YES")
        
class Multisensor(Sensor):
    
    def ping(self):
        self.ping = True
        if self.ping == True:
            print("PING: OK ")

    def printMulti(self):
        reading1 = float(getReading(-99, -1))
        reading2 = int(getReading(0, 100))
        reading3 = int(getReading(0, 100))
        if reading3 < 50:
            reading3 = "NO"
        else:
            reading3 = "YES"

        print ("Multisensor - Temp: {:.1f}°C, Hum: {}% Mov: {}".format(reading1,reading2,reading3)  )
        


sensor1 = Sensor("sensor1", "Lahti")
temp1 = TempSensor("ff-ee-gg-77-88-99", "Kitchen- temp")
hum1 = Humiditysensor("aa-bb-cc-dd-ee-ff", "Kitchen-hum")
pir1 = PIR_sensor("Liikesensori", "Kitchen-pir")
multisensor = Multisensor("1a-2b-3c-4d-5e-6f", "Kitchen-multisensor")

sensor1.printLocation()
sensor1.printReading()

temp1.printLocation()
temp1.printTemp()

hum1.printLocation()
hum1.printHumidity()

pir1.printLocation()
pir1.printPIR()
pir1.printReading()

multisensor.ping()
multisensor.printMulti()
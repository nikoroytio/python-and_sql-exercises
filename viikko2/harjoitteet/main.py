from car import Car 

class ECar(Car):
    def __del__(self):
        print(self.haeRekisterinumero, " destroyed...")

####### PÄÄOHJELMA #####

def kaynnistaAuto(car):
    car.start()

def sammutaAuto(car):
    car.stop()

def toottaa(car):
    car.honk()

def haeRekisteriNumero(car):
    car.getLicensePlate()

def tuhoa(car):
    car.destroy()

#Luodaan oliot luokkiin

car1 = Car("ABC-123","red", 110)
car2 = Car("DEF-246,","blue", 120)
car3 = Car("GHI-369", "yellow", 150)
car4 = Car("MOI-100","green", 170)
ecar = ECar("MOI-200","", 0)


kaynnistaAuto(car1)
kaynnistaAuto(car2)
kaynnistaAuto(car1)
sammutaAuto(car2)
sammutaAuto(car1)
sammutaAuto(car1)

haeRekisteriNumero(car3)
print("Car ", car3._plate, " crashed.")

haeRekisteriNumero(car4)
print(car4._plate, " going too fast.")

tuhoa(ecar)



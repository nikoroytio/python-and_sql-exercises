class Car: # 1st Parent class
    def drive(self):
        print("brum brum!")

class Plane: # 2nd Parent class
    def fly(self):
        print("whoosh...")

# Multiple inheritance
class AeroMobil(Car, Plane): # Child class
    def __init__(self):
        print("driving, then flying")
        self.fly()
        self.drive()

# main program
AeroMobil()
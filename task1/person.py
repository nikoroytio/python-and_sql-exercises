import datetime

class Person:
    def __init__(self, fname, lname, age, birthd):
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.birthd = birthd
    def full_name(self):
        print (self.first_name + " " + self.last_name)
    def birthday(self):
        self.age += 1
    def get_birthday(self):
        aika = datetime.datetime
        return (aika)
# Yläluokka
class Animal:
    def __init__(self, sound='no_sound'):
        # Poistamalla alemmista komennoista kommentit näemme yläluokan ajon aikana aktiivisena
        # print("sound get's initialized here")
        # print("sound for this animal is:",sound)
        self.sound = sound
    def makeSound(self):
        print(self.sound)

# Alaluokka - perii yläluokan Animal
class Cat(Animal):
    def __init__(self):
        # Muodostinfunktiossa kutsutaan usein heti perittyä luokkaa
        Animal.__init__(self, 'Meow...')
        # Näin saamme kutsuttua yläluokan muodostinfunktiota

class Dog(Animal):
    def __init__(self):
        # Muodostinfunktiosta yläluokkaa voidaan kutsua myös "super" metodin avulla
        super().__init__('Woof!')
    def makeSound(self):
        print("I am overriding this method")
        # Tätä lähestymistä ei voi suositella moniperintään

# Pääohjelma
cat1 = Cat()
cat1.makeSound()
dog1 = Dog()
dog1.makeSound()

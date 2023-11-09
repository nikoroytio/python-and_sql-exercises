# yläluokka
class Animal:
    def makeSound(self):
        print(self.sound)

# alaluokka - perii yläluokan Animal
class Cat(Animal):
    sound = 'Meow'

# alaluokka - perii yläluokan Animal
class Dog(Animal):
    sound = 'Bark'

# Kissan ominaisääni on "Meow"
# Kissa on perinyt äänen käyttö toiminnallisuuden Animal kantaluokasta
Cat().makeSound() # Meow


Dog().makeSound()

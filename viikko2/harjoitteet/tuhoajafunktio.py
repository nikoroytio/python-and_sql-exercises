# Tuhoajafunktiosta

class Kakku:

    #Tämä on parametrisoitu muodostinfunktio
    def __init__(self, nimi, koko):
        self.nimi = nimi
        self.koko = koko
        print(self.nimi, " on luotu ja se on kooltaan ", self.koko, " litraa")

    #Tämä on tuhoajafunktio
    def __del__(self):
        print(self.nimi, " tilanvaraus vapautettu")


###### PÄÄOHEJLMA ######

taatelikakku = Kakku("Taatelikakku", 1.0)
maustekakku = Kakku("Maustekakku", 0.75)

del taatelikakku
del maustekakku
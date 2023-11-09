import datetime

 # Luokasta Olioita

 # Luokan määrittely

class Opiskelija:
    
    laskuri = 0 #luokkamuuttuja

    #parametrisoitu muodostinfunktio - constructor

    def __init__(self, num, enimi, snimi, sv, losoite, pnro, ptp, sp1, sp2, puhnro):
        self.opiskelijanumero = num     #instanssimuuttuja
        self.etunimi = enimi            #instanssimuuttuja
        self.sukunimi = snimi           #  jne jne...
        self.syntymavuosi = sv
        self. lahiosoite = losoite
        self.postinumero = pnro
        self.postitoimipaikka = ptp
        self.sposti1 = sp1
        self.sposti2 = sp2
        self.puhelin = puhnro
        Opiskelija.laskuri += 1

    # Jäsenfunktio, metodi
    def tulostaOpiskelijantiedot(self):
        print ("\nOpiskelijanumero: ", self.opiskelijanumero, 
                "\nNimi: ", self.etunimi, " ", self.sukunimi,
                "\nOsoite: ", self.lahiosoite, ", ",self.postinumero, " ", self.postitoimipaikka,
                "\nOyhteystiedot: ", self.sposti1, " ", self.sposti2, " ", self.puhelin )

                
#########  PÄÄOHJELMA #########

# "Tavallinen" funktio
def tulostaObjekti(op):
    op.tulostaOpiskelijantiedot()

# Muodostetaan ajanhetkestä "nyt" vuosiluku iän laskentaa varten
nyt = datetime.datetime.now()

# Luodaan ensimmäinen opiskelijaolio
op1 = Opiskelija("3101123", "Kalle", "Virtanen", 2000, "Vapaudenkatu 11 B 23", "15110",
                    "Lahti", "kalle.virtanen@student.lab.fi", "kale@gmail.com", "0451234567")


print("Opiskelijoita on nyt %d kappaletta." % Opiskelija.laskuri)
print(op1.etunimi, " on ", int(nyt.year) - op1.syntymavuosi, " vuotias.")

#Luodaan toinen opiskelijaolio
op2 = Opiskelija("3101234", "Jaakko", "Nieminen", 1999, "Harjunkuja 17 C", "15200",
                    "Lahti", "jaakko.nieminen@student.lab.fi", "jaskan@live.com", "0409876543")

print("Opiskelijoita on nyt %d kappaletta." % Opiskelija.laskuri)
print(op2.etunimi, " on ", int(nyt.year) - op2.syntymavuosi, " vuotias.")

tulostaObjekti(op1)
tulostaObjekti(op2)

import datetime

 # Luokasta Olioita

 # Luokan määrittely

class Opiskelija:
    
    laskuri = 0 #luokkamuuttuja

    #parametrisoitu muodostinfunktio - constructor

    def __init__(self):
        self.opiskelijanumero = "1234567"     #instanssimuuttuja
        self.etunimi = "Maija"            #instanssimuuttuja
        self.sukunimi = "Meikäläinen"           #  jne jne...
        self.syntymavuosi = 2000
        self. lahiosoite = "Vesijärvenkatu 14 C 24"
        self.postinumero = "15100"
        self.postitoimipaikka = "Lahti"
        self.sposti1 = "maija.meikalainen@student.lab.fi"
        self.sposti2 = ""
        self.puhelin = ""
        Opiskelija.laskuri += 1

    # Jäsenfunktio, metodi

    def tulostaOpiskelijanTiedot(self):
        print("`\nOpiskelijanumero: ", self.opiskelijanumero,
                "\nNimi: ", self.etunimi, " ", self.sukunimi,
                "\nOsoite: ", self.lahiosoite, ", ", self.postinumero, " ", self.postitoimipaikka,
                "\nYhteystiedot: ", self.sposti1, " ", self.sposti2, " ", self.puhelin)


###### PÄÄOHJELMA ######

# "Tavallinen" funktio
def tulostaObjekti(op): 
    op.tulostaOpiskelijanTiedot()

#muodostetaan ajanhetkestä "nyt" vuosiluku iän laskentaa varten
nyt = datetime.datetime.now()

#Luodaan ensimmäinen opiskelijaolio

op1 = Opiskelija()

print("Opiskelijoita on nyt %d kappaletta." % Opiskelija.laskuri)
print(op1.etunimi, " on ", int(nyt.year) - op1.syntymavuosi, " vuotias")

#Luodaan toinen opiskelijaolio
op2 = Opiskelija()

op2.etunimi = "Raija"
op2.sukunimi = "Riipinen"
op2.lahiosoite = "Hollolankatu 42 as. 9"
op2.postinumero = "15210"
op2.postitoimipaikka = "Lahti"
op2.sposti1 = "raija.riipinen@student.lab.fi"


print("Opiskelijoita on nyt %d kappaletta." % Opiskelija.laskuri)
print(op2.etunimi, " on ", int(nyt.year) - op2.syntymavuosi, " vuotias")

tulostaObjekti(op1)
tulostaObjekti(op2)

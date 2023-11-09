#############################################
# Author: Rönkkönen                         #
# Year: 2022                                #
# Program: DB Connection (contact book)     #
#############################################

from pathlib import Path
from datetime import datetime
import sqlite3

# CONSTANT GLOBAL VARIABLES
DB_CONF = {
    "FILEPATH" : Path().joinpath(".\kanta.db")
}


# Tapoja testailla että tuo konstruktio tiedoston suhteen lähti liikkelle
#print(DB_CONF)
#print(DB_CONF["FILEPATH"])
#print(DB_CONF.get("FILEPATH"))

# Classes - Luokat
class Yhteystieto:
    """
    Henkilön yhteystiedot.
    !Huom. katso GDPR Artikla 4.
    Toimii tietosäiliönä -> luo "tieto olio"
    :etunimi: Henkilön etunimi 
    :sukunimi: Henkilön sukunimi
    :syntymapaiva: Aikaleima (Epoch, eli sekunteja 1970, n. 10 numero tänäpäivänä)
    :sposti: Sähköpostiosoite: esim. etunimi.sukunimi@example.com
    """
    def __init__(self, etunimi: str, sukunimi : str, syntymapaiva: datetime, sposti: str):
        try:
            self.etunimi = str(etunimi)
            self.sukunimi = str(sukunimi)
            self.syntymapaiva = str(syntymapaiva.timestamp())
            self.sposti = str(sposti)
        except Exception as virhe:
            print("Yhteystieto virhe: Exception -- " + str(virhe))
            del self
            return None
        
class YhteystietoKirja:
    @staticmethod
    def muodostaTaulu() -> bool:
        try:
            yhteys = luoYhteysTietokantaan(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor() # kyselyiden hallintaan kursori
            sql_lause = "CREATE TABLE IF NOT EXISTS yhteystiedot("
            sql_lause += "sposti varchar(255) PRIMARY KEY NOT NULL,"
            sql_lause += "etunimi varchar(255) NOT NULL,"
            sql_lause += "sukunimi varchar(255) NOT NULL,"
            sql_lause += "syntymapaiva INTEGER NOT NULL "
            sql_lause += ");"
            kursori.execute(sql_lause)
            yhteys.close()
            return True

        except Exception as virhe:
            print("Yhteystietokirja alustusvirhe: Exception - " + str(virhe))
            return False

    @staticmethod
    def haeYhteystiedot():
        try:
            yhteys = luoYhteysTietokantaan(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor() # kyselyiden hallintaan kursori
            sql_lause = "SELECT * FROM yhteystiedot;"
            kursori.execute(sql_lause)
            tulosjoukko = kursori.fetchall()
            print(tulosjoukko)
            yhteys.close()

        except Exception as virhe:
            print("Yhteystietokirja haeYhteystiedot: Exception - " + str(virhe))
            return False


    @staticmethod
    def syotaTietue():
        try:
            sposti = input("Syötä sposti:  ")
            etunimi = input("Syötä etunimi: ")
            sukunimi = input("Syötä sukunimi: ")
            syntymavuosi = datetime.fromisoformat(input("Syötä syntymavuosi muodossa YYYY-MM-DD: "))
            yhteystieto = Yhteystieto(etunimi, sukunimi, syntymavuosi, sposti,)

            yhteys = luoYhteysTietokantaan(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor() # kyselyiden hallintaan kursori
            sql_lause = "INSERT INTO yhteystiedot (sposti, etunimi, sukunimi, syntymapaiva) VALUES (?, ?, ?, ?);"
            sql_data = [yhteystieto.sposti, yhteystieto.etunimi, yhteystieto.sukunimi, yhteystieto.syntymapaiva]
            kursori.execute(sql_lause, sql_data)
            print("Syöte onnistui. ")
            yhteys.commit() # INSERT yhteydessä oltava vahvistus
            yhteys.close()

        except Exception as virhe:
            print("Yhteystietokirja tietueen syöttövirhe: Exception -" + str(virhe))
        return None

#Aliohjelmat
def luoYhteysTietokantaan(polku: str):
    """
    :polku: tietokanta tiedostoon
    """

    try:
        yhteys = sqlite3.connect(polku)
        return yhteys
    except sqlite3.Error as sqliteVirhe:
        print(sqliteVirhe)
    except Exception as virhe:
        print(virhe)
    return None

def valikko():
    print("Syötä haluamasi toiminto: ")
    print("(0) Sulje ohjelma")
    print("(1) Hae yhteystiedot")
    print("(2) Syötä yhteystieto")
    print("(3) Etsi yhteystieto")
    valinta = -1
    try: 
        syote = input("Syötä Valintasi: ")
        valinta = int(syote)
    except ValueError:
        print("Käytä numeroa")
        return valinta
    return valinta


#Pääphjelma
def paaohjelma():
    print ("Tervetuloa ohjelmaan.")
    if YhteystietoKirja.muodostaTaulu() == True:
        print("Ohjelma valmis käyttöön")
    else:
        print("Yhteystietokirjan muodostaminen epäonnistui.")
        print("Lopetetaan ohjelma. ")
        return -1

    while True:
        valinta = valikko()
        print("Valintasi: " + str(valinta))
        if valinta == 1:
            print("Hae yhteystiedot")
            YhteystietoKirja.haeYhteystiedot()
        elif valinta == 2:
            print("Syötä yhteystieto")
            YhteystietoKirja.syotaTietue()
        elif valinta == 3:
            print("Etsi yhteystieto")
        elif valinta == 0:
            print("Lopetetaan ohjelma")
            break
        else:
            print("Tunnistamaton syöte. Yritä uudelleen.")
        print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
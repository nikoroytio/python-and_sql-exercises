"""
Tämä luokka osaa käsitellä tiedoston tulostuksen,
sekä osaa toteuttaa alkeellisia muokkausia tiedostoihin käyttäjän syötteiden perusteella.
Tiedostolla demonstroidaan, miten tiedostoja voidaan käsitellä olioparadigman keinoin.
"""
class ResurssienHallinta:
    def __init__(self) -> None:
        print("Resurssien hallinta luotu")
    
    def tulostaKaikki(self, tiedoston_nimi: str):
        tiedosto = open(tiedoston_nimi, 'r')
        print("\nTiedosto:", tiedoston_nimi, sep=' ')
        print("\n#---TIEDOSTO_ALKAA---#")
        print(tiedosto.read(), end='') # poistetaan \n ohjainmerkki "end" parametristä
        print("\n#---TIEDOSTO_LOPPUU---#")

    def tulostaRivitNumeroineen(self, tiedoston_nimi: str):
        # print("Ei toimi vielä.")
        tiedosto = open(tiedoston_nimi, 'r').readlines()
        print("\nTiedosto:", tiedoston_nimi, sep=' ')
        print("\n#---TIEDOSTO_ALKAA---#")
        for riviIndeksi in range(len(tiedosto)):
            # otetaan huomioon, että rivien lopussa on \n määrittely, ettei tule toistona tulosteeseen
            print("RIVI " + str(riviIndeksi + 1) + ": " + tiedosto[riviIndeksi], end='')
        print("\n#---TIEDOSTO_LOPPUU---#")    
    def tulostaYksiRivi(self, tiedoston_nimi: str, rivi_indeksi: int):
        # print("Ei toimi vielä.")
        tiedosto = open(tiedoston_nimi, 'r').readlines()
        print("\nTiedosto:", tiedoston_nimi, sep=' ')
        for i in range(len(tiedosto)):
            if i == rivi_indeksi:
                print(tiedosto[i])
        print("")

    def jatketaanTiedostoa(self, tiedoston_nimi: str, merkkijono: str):
        # print("Ei toimi vielä.")
        tiedosto = open(tiedoston_nimi, 'a')
        tiedosto.write('\n' + merkkijono)
        print("Rivi lisätty!")
    
    """
    Muokataan tiedoston riviä X. Jos riviä ei ole olemassa, tehdään se rivi.
    Ylikirjoitukseen käytetään parametriä "merkkijono", jolla korvataan tiedoston riveistä
    se, mihin osoitetaan "riviIndeksi" parametrillä.
    """
    def ylikirjoitaRivi(self, tiedoston_nimi: str, muokattavanRivinIndeksi: int, merkkijono: str):
        """
        'w' tarkoittaa tiedoston ylikirjoitusta
        'r' tarkoittaa tiedoston lukemista 'read'
        Kahta tilaa ei voida sekoittaa keskenään. Joko luetaan tai kirjoitetaan.
        """
        tiedosto = open(tiedoston_nimi, 'r')
        rivit = tiedosto.readlines()
        muokattuRivi = merkkijono

        """
        Luodaan rivi, jos sitä ei ole olemassa.
        Jos rivi on viimeinen kirjoitettava rivi, niin
        Tällöin tulee muistaa, että viimeisen rivin indeksi on yhden
        pienempi kuin rivilistan pituus "len(rivit)".
        Esim. rivit[5] on viimeinen listan esine, tällöin "len(rivit)" on 6
        """
        if (muokattavanRivinIndeksi >= (len(rivit))):
            # arvojoukon koko on myös huomioitava
            for rivinIndeksi in range(muokattavanRivinIndeksi + 1):
                if (len(rivit) <= rivinIndeksi):
                    rivit.append('\n') # lisätään puuttuva tyhjä rivi
                # elseä ei tarvita, koska kyseessä olemassa oleva rivi
        # Tehdään muokkaus käyttäjän tahtomalle riville
        rivit[muokattavanRivinIndeksi] = '\n' + muokattuRivi
        tiedosto.close() # closing the read handle
        tiedostoon = open(tiedoston_nimi, 'w')

        for rivi in rivit:
            tiedostoon.write(rivi)
        
        tiedostoon.close()

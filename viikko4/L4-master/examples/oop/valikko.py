from typing import List
from resurssien_hallinta import ResurssienHallinta

class Valikko:
    """
    Luokka toimii ja muistaa valittuja asioita,
    sekä tarjoaa valikkotoiminnallisuuden
    """
    tiedostot: List[str] = []

    # tiedostoIndeksi on ominaisuus, eli olion "muuttuja"
    tiedostoIndeksi = -1
    resurssien_hallinta: ResurssienHallinta

    def __init__(self, tiedostot) -> None:
        # print(self.tiedostot)
        self.tiedostot = tiedostot
        # print(self.tiedostot)
        self.resurssien_hallinta = ResurssienHallinta()
    
    def tiedostonNimi(self):
        return self.tiedostot[self.tiedostoIndeksi]

    def tiedostonValinta(self):
        """
        Tällä valikon metodilla valitaan tiedosto
        """
        print("Valitse tiedosto, mitä haluat käsitellä: ")
        for i in range(len(self.tiedostot)):
            print(str(i + 1) + ") " + self.tiedostot[i])
        # talletetaan tieto valinnasta olioon. Tiedon voisi myös palauttaa
        self.tiedostoIndeksi = int(input("Syötä valinta: ")) - 1
        print("Valitsit tiedoston: " + self.tiedostot[self.tiedostoIndeksi])

    def operaatioValinta(self):
        """
        Tällä valikon metodilla valitaan tiedostolle tehtävä operaatio
        """
        print("\nValitse opeeratio:")
        print("1) Tulosta tiedoston sisältö")
        print("2) Tulosta tiedoston sisältö rivinumeron kera")
        print("3) Tulosta yksittäinen rivi")
        print("4) Lisää rivi tiedoston perään")
        print("5) Ylikirjoita rivi")
        self._tiedostoOpeeratio = int(input("Syötä valinta: ")) - 1
        print("Valitsemasi operaatio: " + str(self._tiedostoOpeeratio + 1))
    
    def operaatioAjo(self, ulkoa=-1):
        """
        _operaatio ilman "self alkua tarkoittaa,
        että ominaisuus on käytössä vain metodin "operaatioAjo" aikana
        """
        _operaatio = self._tiedostoOpeeratio
        if (ulkoa != -1): # ajo ulkoa
            _operaatio = ulkoa
        
        # Alempana määritellään tarvittavat parametrit tarkasti, kerätään jos puuttuu
        # Kokeillaan valintarakennetta "match":llä "if-elif-elif" sijasta
        match _operaatio:
            case 0: # 0 = 1) Tulosta tiedoston sisältö
                self.resurssien_hallinta.tulostaKaikki(self.tiedostot[self.tiedostoIndeksi])
            case 1: # 1 = 2) Tulosta tiedoston sisältö rivinumeroiden kera
                self.resurssien_hallinta.tulostaRivitNumeroineen(self.tiedostonNimi())
            case 2: # 2 = 3) Tulosta yksittäinen rivi
                riviIndeksi = int(input("Syötä rivin numero: ")) - 1
                self.resurssien_hallinta.tulostaYksiRivi(self.tiedostonNimi(), riviIndeksi)
            case 3: # 3 = 4) Lisää rivi tiedoston perään
                syote = input("Anna rivin sisältö: ")
                self.resurssien_hallinta.jatketaanTiedostoa(self.tiedostonNimi(), syote)
            case 4: # 4 = 5) Ylikirjoita rivi
                syote = input("Anna rivin sisältö: ")
                riviIndeksi = int(input("Syötä rivin numero: ")) - 1
                self.resurssien_hallinta.ylikirjoitaRivi(self.tiedostonNimi(), riviIndeksi, syote)
            case _:
                print("Operaatio ei ole tuettujen listalla")


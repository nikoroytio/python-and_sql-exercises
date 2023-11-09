# Tämä ohjelma käsittelee tiedostoja olio-ohjelma paradigman avulla
# ---- Pääohjelman alustusta ----
from valikko import Valikko

# Määritellään tiedostot
tiedostot = [ 'file1.txt', 'file2.txt', 'file3.txt' ]

# Luodaan olio "valikko" luokasta Valikko
valikko = Valikko(tiedostot)

# ---- Pääohjelma alkaa ----
# Kysellään käyttäjältä käsiteltävää tiedostoa
valikko.tiedostonValinta()
valikko.operaatioValinta()
valikko.operaatioAjo()

# ---- Pääohjelma päättyy ----
print("Ohjelma päättyy")
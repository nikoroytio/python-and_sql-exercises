import sqlite3
from pathlib import Path


#Yhteyksiä tietokantaan
Path().absolute().joinpath("test.db")

yhteys = sqlite3.connect(Path().joinpath("tietokanta.db"))


kursori = yhteys.cursor()

#Taulukon luonti Pythonilla sqlite3
sql_lause = "CREATE TABLE IF NOT EXISTS contacts("
sql_lause += " email varchar (255) PRIMARI KEY NOT NULL,"
sql_lause += " fname varchar (20) NOT NULL,"
sql_lause += "lname varchar (20) NOT NULL,"
sql_lause += "dob INTEGER NOT NULL"
sql_lause += ");"

kursori.execute(sql_lause)

yhteys.close

# Laitetaan sql insertioon kysymysmerkin placeholderiksi
sql_lause = "INSERT INTO contacts (emai, fname, lname, dob) VALUES (?, ?, ?, ?);"
# Tällöin ite järjestelmä hoitaa muotoilun, painaa vaan tietoja sisään
sql_tiedot = ["jane.berry@example.com", "Jane", "Berry", 1234567891]

kursori.execute(sql_lause, sql_tiedot)

from models.BaseModel import BaseModel
from db import DB

class ITehtava:
    jarjestysnumero: int
    tila: str
    nimi: str

class Tehtava(ITehtava):
    def __init__(self, jarjestysnumero: int, tila: str, nimi: str):
        self.jarjestysnumero = jarjestysnumero
        self.tila = tila
        self.nimi = nimi

class TodoModel(BaseModel):
    def __init__(self, db: DB) -> None:
        super().__init__(db)
        return None
    def lisaaTehtava(self, nimi: str) -> bool:
        onnistui = True
        try:
            lauseke = "INSERT INTO todos (status, name) VALUES(?,?);"
            tehtava = Tehtava(-1, ' ', nimi)
            tiedot = (tehtava.tila, tehtava.nimi,)
            print(tehtava)
            print(lauseke)
            print(tiedot)
            self.createRecord(lauseke, [tiedot])
        except Exception as err:
            onnistui = False
            print("TodoMalli - Virhe tehtävän luonnissa.")
            print(err)
        return onnistui
            
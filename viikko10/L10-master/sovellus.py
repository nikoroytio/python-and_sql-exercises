from models.BaseModel import BaseModel
from models.TodoModel import TodoModel
from db import DB

TAULUKOT="""
CREATE TABLE IF NOT EXISTS todos(
    order_num INTEGER PRIMARY KEY AUTOINCREMENT,
    status CHAR(1) NOT NULL,
    name TEXT NOT NULL UNIQUE
);
"""

class TehtavaKontrolleri:
    db: DB
    todo_model: TodoModel
    def __init__(self, db: DB) -> None:
        self.db = db
        self.todo_model = TodoModel(db)
        return None
    def lisaaTehtava(self) -> None:
        tehtavanimi = input("Syötä tehtävän nimi: ")
        onnistu = self.todo_model.lisaaTehtava(tehtavanimi)
        if onnistu == True:
            print("Tehtävän lisäys onnistui.")
        else:
            print("Tehtävän lisäys epäonnistui.")
        return None

class Valikko:
    valinta: int = -1
    def suorita(self) -> None:
        try:
            print("Valintasi:")
            print("1) Lisää tehtävä")
            print("2) Lue tehtävät")
            print("0) Poistu ohjelmasta")
            syote = input("Valintasi: ")
            self.valinta = int(syote)
        except:
            self.valinta = -1
        return None

class Main(Valikko):
    print("Tervetuloa ohjelmaan.")
    db: DB
    kontrolleri: TehtavaKontrolleri
    def __init__(self) -> None:
        super().__init__()
        self.db = DB()
        # Quick and dirty
        self.base_model = BaseModel(self.db)
        self.base_model.createRecord(TAULUKOT, [])
        # Quick and dirty ends
        self.kontrolleri = TehtavaKontrolleri(self.db)
        self.menu()
    def menu(self) -> None:
        while True:
            self.suorita()
            if self.valinta == 1:
                self.kontrolleri.lisaaTehtava()
            elif self.valinta == 2:
                print("Toka")
            elif self.valinta == 0:
                print("Ohjelma päättyy.")
                break
            else:
                print("Tuntematon valinta, yritä uudelleen.")
            print()
        print("Kiitos ohjelman käytöstä.")
        return None

if __name__ == '__main__':
    app = Main()
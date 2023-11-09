import sqlite3

DB_CONF = {
    "FILEPATH": "kanta.db"
}

class DB:
    _conn: sqlite3.Connection = None
    def __init__(self) -> None:
        self._path = DB_CONF["FILEPATH"]
        self._createConnection()
        return None
    def _createConnection(self) -> None:
        try:
            if self._conn == None:
                self._conn = sqlite3.connect(self._path)
        except Exception as virhe:
            print("Virhe tietokantayhteyden muodostamisessa.")
            print(virhe)
        return None

from db import DB

class BaseModel:
    db: DB = None
    def __init__(self, db: DB) -> None:
        self.db = db
    #region Create
    def createRecord(self, sql_query, sql_datas: list[tuple] = []) -> None:
        try:
            cursor = self.db._conn.cursor()
            if len(sql_datas) == 0:
                cursor.execute(sql_query)
            elif len(sql_datas) == 1:
                print(sql_datas)
                cursor.execute(sql_query, sql_datas[0])
            else: # if many insertions for example
                cursor.executemany(sql_query, sql_datas)
            self.db._conn.commit()
        except Exception as err:
            print("Virhe lisättäessä rivejä tietokantaan.")
            print(err)
        return None
    #endregion Create
    #region Read
    def readRecords(self, sql_query, sql_datas: list[tuple] = []) -> list[tuple]:
        records = []
        try:
            cursor = self.db._conn.cursor()
            if len(sql_datas) == 0:
                cursor.execute(sql_query)
            elif len(sql_datas) == 1:
                cursor.execute(sql_query, sql_datas)
            else: # if many insertions for example
                cursor.executemany(sql_query, sql_datas)
            self.db._conn.commit()
            records = cursor.fetchall()
        except Exception as err:
            print("Virhe lisättäessä rivejä tietokantaan.")
            print(err)
        return records
    #endregion Read
    #region Update

    #endregion Update
    #region Delete

    #endregion Delete
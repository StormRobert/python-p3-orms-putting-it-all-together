import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    
    all = []

    def __init__(self, name, breed) :
        self.name = name
        self.breed = breed
        self.id = None 

    @classmethod
    def create_table(cls):
     sql = """
              CREATE TABLE IF NOT EXISTS dogs(
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  breed TEXT
              )
        """
     CURSOR.execute(sql)
     CONN.commit()

    @classmethod
    def drop_table(cls):
     sql = """
              DROP TABLE IF EXISTS DOGS
       """
     CURSOR.execute(sql)
     CONN.commit()

    def save(self):
        sql = """
                INSERT INTO dogs (name, breed)
                VALUES(?, ?)

          """
        CURSOR.execute(sql,(self.name, self.breed))
        CONN.commit()
        self.id = CURSOR.lastrowid

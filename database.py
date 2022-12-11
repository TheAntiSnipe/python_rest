import os
import psycopg2

"""
This code uses a Borg singleton database connection handler,
that is used by a bunch of subsystems operating under a
facade pattern. REALLY unnecessary, considering psycopg2 is
thread safe and does not necessitate a singleton, and a facade 
with a bunch of subsystems is REALLY overkill for a simple crud op.

A very good example of why NOT to use design patterns when stuff is 
already simple. However, this is for the sake of practice.
"""

class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

class Database(Borg):
    def __init__(self) -> None:
        Borg.__init__(self)

        self.connection = psycopg2.connect( host = "postgres_db",
        user = os.getenv("db_user"),
        password = os.getenv("db_password"),
        dbname = os.getenv("db_user"))
        self.cursor = self.connection.cursor()
        initial_query = """CREATE TABLE IF NOT EXISTS records_store(log_id SERIAL PRIMARY KEY,album_name VARCHAR(255) NOT NULL,price REAL,year INT,label VARCHAR(255))"""
        self.cursor.execute(initial_query)
        self.connection.commit()
    
    def __del__(self):
        self.connection.close()

class Create:
    def __init__(self):
        self.database = Database()

    def create_one(self,entry):
        query = """INSERT INTO records_store(album_name, price, year, label)
        VALUES (%s, %s, %s, %s)"""
        try:
            self.database.cursor.execute(query,entry)
            self.database.connection.commit()
            return True
        except:
            return False

class Read:
    def __init__(self):
        self.database = Database()

    def read_all(self):
        query = """SELECT * FROM records_store"""
        try:
            self.database.cursor.execute(query)
            records = self.database.cursor.fetchall()
            return records
        except:
            return None
class Update:
    def __init__(self):
        self.database = Database()
    
    def update_year(self,entry):
        query = """UPDATE records_store SET year = %s WHERE log_id = %s"""
        try:
            self.database.cursor.execute(query,entry)
            self.database.connection.commit()
            return True
        except:
            return False

class Delete:
    def __init__(self):
        self.database = Database()
    
    def delete_one(self,entry):
        query = """DELETE FROM records_store WHERE log_id = %s"""
        try:
            self.database.cursor.execute(query,entry)
            self.database.connection.commit()
            return True
        except:
            return False

class QueryProcessor:
    def __init__(self,create: Create, read: Read, update: Update, delete: Delete) -> None:
        self._create = create or Create()
        self._read = read or Read()
        self._update = update or Update()
        self._delete = delete or Delete()

    def create_one(self,entry):
        return self._create.create_one(entry)
    
    def read_all(self):
        return self._read.read_all()
    
    def update_year(self,entry):
        return self._update.update_year(entry)

    def delete_one(self,entry):
        return self._delete.delete_one(entry)

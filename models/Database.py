import sqlite3


class Database:
    db_name = 'game_leaderboard_v2.db'  # Andmebaasi nimi
    table = 'ranking'   #Tabeli nimi

    def __init__(self):
        """Konstruktor"""
        self.conn = None    # Ühendus
        self.cursor = None #
        self.connect()  # Loo ühendus

    def connect(self):
        """Loob ühenduse andmebaasiga"""
        try:
            if self.conn:
                self.conn.close()
                print('Varasem andmebaasi ühendus suletud')
            self.conn = sqlite3.connect(self.db_name)   #Loo ühendus
            self.cursor = self.conn.cursor()
            print(f'Uus ühendus andmebaasiga {self.db_name} loodud')
        except sqlite3.Error as error:
            print(f'Tõrge andmebaasi ühenduse loomisel: {error}')
            self.conn = None
            self.cursor = None

    def close_connection(self):
        """Sulgeb andmebaasi ühenduse"""
        try:
            if self.conn:
                self.conn.close()
                print(f'Ühendus andmebaasiga {self.db_name} suletud')
        except sqlite3.Error as error:
            print(f'Tõrge ühenduse sulgemisel: {error}')

    def read_records(self):
        """Loeb andmebaasist kogu edetabeli"""
        if self.cursor:
            try:
                sql = f'SELECT * FROM {self.table};'
                self.cursor.execute(sql)
                data = self.cursor.fetchall()   # kõik kirjed muutujasse data
                return data
            except sqlite3.Error as error:
                print(f'Kirjete lugemisel ilmnes tõrge: {error}')
                return []   #Tagastab tühja listi
            finally:
                self.close_connection()
        else:
            print('Ühenduse andmebaasiga puudub. Loo ühendus andmebaasiga')

    def add_record(self, name, steps, pc_nr, cheater, seconds):
        # """Lisab mängija andmed tabelisse"""
        if self.cursor:
            try:
                sql = f'INSERT INTO {self.table} (name, steps, quess, cheater, game_length) VALUES (?,?,?,?,?);'
                self.cursor.execute(sql, (name, steps, pc_nr, cheater, seconds))
                self.conn.commit()      # See lisab reaalselt tabelisse(save)
            except sqlite3.Error as error:
                print(f'Mängija lisamisel tekkis tõrge')
            finally:
                self.close_connection()
        else:
            print('Ühendus puudub! Palun loo ühendus andmebaasiga')


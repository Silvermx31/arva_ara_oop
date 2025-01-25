import sqlite3

class Database:
    db_name = 'game_leaderboard_v2.db'  # Andmebaasi nimi
    table = 'ranking'   # Tabeli nimi

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
            self.conn = sqlite3.connect(self.db_name)   # Loo ühendus
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

    def add_record(self, name, steps, pc_nr, cheater, seconds):
        """Lisab mängija andmed tabelisse"""
        if self.cursor:
            try:
                sql = f'INSERT INTO {self.table} (name, steps, quess, cheater, game_length) VALUES (?, ?, ?, ?, ?);'
                self.cursor.execute(sql, (name, steps, pc_nr, cheater, seconds))
                self.conn.commit()
                print("Andmed lisati edukalt tabelisse.")
            except sqlite3.Error as error:
                print(f'Mängija lisamisel tekkis tõrge: {error}')
            finally:
                self.close_connection()
        else:
            print('Ühendus puudub! Palun loo ühendus andmebaasiga.')

    def no_cheater(self):
        """Loeb ausalt mänginud mängijate top 10 edetabeli"""
        if self.cursor:
            try:
                sql = (f"""
                    SELECT name, quess, steps, game_length 
                    FROM {self.table} 
                    WHERE cheater = ? 
                    ORDER BY steps ASC, game_length ASC, name ASC 
                    LIMIT 10;
                """)
                self.cursor.execute(sql, (0,))
                data = self.cursor.fetchall()   # kõik kirjed muutujasse data
                return data
            except sqlite3.Error as error:
                print(f'Kirjete lugemisel ilmnes tõrge: {error}')
                return []   # Tagastab tühja listi
            finally:
                self.close_connection()
        else:
            print('Ühenduse andmebaasiga puudub. Loo ühendus andmebaasiga')

    def for_export(self):
        """Tagastab kogu andmebaasi sisu sorteerituna"""
        if self.cursor:
            try:
                sql = (f"""
                    SELECT name, quess, steps, game_length, game_time 
                    FROM {self.table} 
                    ORDER BY steps ASC, game_length ASC, name ASC;
                """)
                self.cursor.execute(sql)
                data = self.cursor.fetchall()   # kõik kirjed muutujasse data
                return data
            except sqlite3.Error as error:
                print(f'Kirjete lugemisel ilmnes tõrge: {error}')
                return []   # Tagastab tühja listi
            finally:
                self.close_connection()
        else:
            print('Ühendus andmebaasiga puudub. ')

# Export
class ExportToFile:
    def __init__(self, model):
        self.model = model
        db = Database()
        self.data = db.for_export()

    def export(self):
        """Eksportib tabeli sisu faili"""
        if not self.data:
            print("Andmeid ei leitud.")
            return

        file_name = Database.db_name.replace('.db', '.txt')
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write("name;quess;steps;game_length;game_time\n")
                for row in self.data:
                    formatted_time = self.model.format_time(row[3])
                    file.write(f"{row[0]};{row[1]};{row[2]};{formatted_time};{row[4]}\n")
            print(f"Andmed eksporditi faili: {file_name}")
        except Exception as e:
            print(f"Tekkis viga faili kirjutamisel: {e}")

from datetime import datetime
from models.Database import Database

class ExportToFile:
    def __init__(self, model):
        self.model = model
        db = Database()
        self.data = db.for_export()  # Laeme andmed edetabelist

    def export(self):
        """Eksportib tabeli andmed faili"""
        if not self.data:
            print("Edetabel on tühi. Andmeid ei leitud eksportimiseks.")
            return

        file_name = Database.db_name.replace('.db', '.txt')
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write("name;quess;steps;game_length;game_time\n")
                for row in self.data:
                    formatted_time = self.format_time(row[3])
                    formatted_game_time = self.format_datetime(row[4])
                    file.write(f"{row[0]};{row[1]};{row[2]};{formatted_time};{formatted_game_time}\n")
            print(f"Andmed eksporditi faili: {file_name}")
        except Exception as e:
            print(f"Tekkis viga faili kirjutamisel: {e}")

    @staticmethod
    def format_time(seconds):
        """Vormindab sekundid kujule HH:MM:SS"""
        try:
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            return f"{hours:02}:{minutes:02}:{seconds:02}"
        except Exception:
            return "--:--:--"

    @staticmethod
    def format_datetime(datetime_str):
        """Vormindab kuupäeva ja kellaaja kujule PP.KK.AAAA HH:MM:SS"""
        try:
            dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
            return dt.strftime("%d.%m.%Y %H:%M:%S")
        except Exception:
            return "--:--:--"

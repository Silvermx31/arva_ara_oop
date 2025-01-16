from random import randint

from models.Database import Database
from models.Stopwatch import Stopwatch


class Model:
    #Defineerime klassi muutujad
    pc_nr = randint(1, 100)     # random nr
    steps = 0       # sammude arv
    game_over = False   #mäng läbi
    cheater = False   # mängija ei cheadi
    stopwatch = Stopwatch() # Loome stopperi ojekti

    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.pc_nr = randint(1, 100)  # random nr
        self.steps = 0  # sammude arv
        self.game_over = False  # mäng läbi
        self.cheater = False  # mängija ei cheadi
        self.stopwatch.reset()  #nullib stopperi
        #self.stopwatch.start()  #käivitab stopperi

    def ask(self):
        """küsib nr ja kontrollib"""
        user_nr = int(input('Sisesta nr'))
        self.steps += 1     # Sammude arv kasvab ühe võrra

        if user_nr == 1000:     #Tagauks
            self.cheater = True     #Cheater
            self.game_over = True       #mäng läbi
            self.stopwatch.stop()       #peata aeg
            print(f'Leidsid mu nõrga koha. Õige nr oli {self.pc_nr}.')
        elif user_nr > self.pc_nr:
            print('Väiksem')
        elif user_nr < self.pc_nr:
            print('Suurem')
        elif user_nr == self.pc_nr:
            self.game_over = True
            self.stopwatch.stop()
            print(f'Leidsid õige nr {self.pc_nr} sammuga.')

    def lets_play(self):
        """Mängime mängu avalik meetod"""
        while not self.game_over:
            self.ask()
        # Näita mängu aega
        print(f'Mäng kestis {self.stopwatch.format_time()}')
        self.what_next()    # mis on järgmiseks
        self.show_menu()

    def what_next(self):
        """Küsime mängija nime ja lisame info andmebaasi"""
        name = self.ask_name()
        db = Database()     # Loo andmebaasi objekt
        db.add_record(name, self.steps, self.pc_nr, self.cheater, self.stopwatch.seconds)


    @staticmethod
    def ask_name():
        """Küsib nime ja tagastab korrektse nime"""
        name = input('Kuidas on mängija nimi? ')
        if not name.strip():
            name = 'Teadmata'
        return name.strip()

    def show_menu(self):
        """Näita mängu menüüd"""
        print('1 - Mängima')
        print('2  Edetabel')
        print('3 - Välju programmist')
        user_input = int(input('Sisesta nr [1, 2 või 3]: '))
        if 1 <= user_input <= 3:
            if user_input == 1:
                self.reset_game()       #Algseadista mäng
                self.stopwatch.start()  #Käivita stopper
                self.lets_play()        #lähme mängima
            elif user_input == 2:
                self.show_leaderboard()     #näita edetabelit
                self.show_menu()        #Näita menüüd
            elif user_input == 3:
                print('Bye')        #Väljasta tekst
                exit()      #Skripti töö lõppeb
        else:
            self.show_menu()

    @staticmethod
    def show_leaderboard():
        """Näita edetabelit"""
        db = Database()
        data = db.read_records()
        if data:
            for record in data:
                print(record)   # name -> record[1]

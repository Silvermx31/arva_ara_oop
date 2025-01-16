from random import randint

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
        self.stopwatch.start()  #käivitab stopperi

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
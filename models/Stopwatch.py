import threading
import time


class Stopwatch:
    def __init__(self):
        self.seconds = 0        #aeg sekundites
        self.running = False    # kas aeg töötab
        self.thread = None      # aeg eraldi threadi, et mängides samal ajal aeg jookseks

    def start(self):
        #Käivita stopper:
        if not self.running:
            self.running = True # Aeg jookseb
            self.thread = threading.Thread(target=self._run)    # Lisatud threadi
            self.thread.start()     # Käivita thread

    def _run(self):
        """ Aeg jookseb threadis"""
        while self.running:
            time.sleep(1)   # oota 1 sekund
            self.seconds += 1   # suurenda sekundit ühe võrra

    def stop(self):
        """Peata stopper"""
        self.running = False

    def reset(self):
        self.stop()     #aeg peatada
        self.seconds = 0    #aeg nullida

    def format_time(self):
        hours = self.seconds // 3600
        minutes = (self.seconds % 3600) // 60
        seconds = self.seconds % 60
        #return "%02d:%02d:%02d" % (hours, minutes, seconds)
        return f'{hours:02}:{minutes:02}:{seconds:02}'


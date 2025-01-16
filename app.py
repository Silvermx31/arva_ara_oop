#import time
#from models.Database import Database
from models.Model import Model
#from models.Stopwatch import Stopwatch

if __name__ == '__main__':
    model = Model()
    model.show_menu()
    # TODO Järgnev rida oli enne show_menu osa
    #model.lets_play()



#if __name__ == '__main__':
 #    model = Model()
  #   print(model.pc_nr)  #arvuti mõeldud nr, käivitati ka stopper
   #  time.sleep(2)   # oota 2 sekki
    # model.stopwatch.stop()  #jäta stopper seisma
     #print(model.stopwatch.format_time())    #Aega 2 sekki





#from models.Stopwatch import Stopwatch
#if __name__ == '__main__':
 #   stopper = Stopwatch()
  #  stopper.start()
   # input("Oota. .")
    #stopper.stop()
    #print(stopper.format_time())

#    stopper.reset()
 #   stopper.start()
  #  input("Oota. .")
   # stopper.stop()
    #print(stopper.format_time())
#"""

#"""
 #__name__ == '__main__':
  #  db = Database()
   # data = db.read_records()
   # if data:
    #    for record in data:
     #       print(record)"""



from models.Database import Database
from models.Stopwatch import Stopwatch

"""
from models.Stopwatch import Stopwatch

if __name__ == '__app__':
    stopper = Stopwatch()
    stopper.start()
    input("Oota. .")
    stopper.stop()
    print(stopper.format_time())

    stopper.reset()
    stopper.start()
    input("Oota. .")
    stopper.stop()
    print(stopper.format_time())

"""
if __name__ == '__main__':
    db = Database()
    data = db.read_records()
    if data:
        for record in data:
            print(record)
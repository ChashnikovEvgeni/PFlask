import pickle
import sys


class FileIO:
    def __init__(self, city):
        self.city = city

    def save(self):
       try:
        pickle.dump((self.city.maxID, self.city.citizens), open("data.dat", "wb"))
        print("Данные успешно сохраненны")
       except:
           print("Непредвиденная ошибка:", sys.exc_info()[0])

    def load(self):
        try:
            maxID = 0
            citizens = []
            (maxID, citizens) = pickle.load(open("data.dat", "rb"))
            print(citizens)
            return citizens
            print("Данные успешно загружены")
        except:
            print("Непредвиденная ошибка:", sys.exc_info()[0])
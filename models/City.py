from IO.FileIO import FileIO
from IO.Utils import Utils_console, Utils_web

from IO.DataBaseIO import FDataBase


class City:
    def __init__(self, source):
        self.citizens = dict()
        self.storageFile = FileIO(self)
        self.storageDB = FDataBase(self)
        if source == "console":
            self.utils = Utils_console(self)
        elif source == "web":
            self.utils = Utils_web(self)
        self.maxID = 0

    def add(self, data=None, db=None):
        """Добавление нового жителя в список населения города"""
        self.utils.add(data, db)  # добавление в локальный список жителей города
        #self.storageDB.add(data,db)

    def write(self):
        """Вывод списка жителей города"""

        if self.empty_check():
                return
        for id, citizen in self.citizens.items():
            print("----------------------------------------")
            citizen.write()
        print("----------------------------------------")

    def save(self):
        """Сохрание данных о городе в файл с расширением .dat"""

        if self.empty_check():
            return
        self.storageFile.save()

    def load(self, source, db):
        """Загрузка данных о населении города из файла"""

        if source == "File":
            print("не на месте")
            citizens =self.storageFile.load()
            for key in citizens:
                self.maxID+=1
                citizens[key].id = self.maxID
                self.storageDB.addin_database(citizens[key], db)
        elif source == "DB":
            print("на месте")
            self.storageDB.load(db)
       # self.storageDB.getData(db)

    def delete(self, citizen_id = None, db=None):
        """Удаление данных одного из жителей"""
        self.utils.delete_citizen(citizen_id, db)

    def full_delete(self, db):
        """Удаление данных о всех жителях"""

        if self.empty_check():
                return False
        self.citizens.clear()
        self.maxID = 0
        self.storageDB.dell_all_data(db)
        print("Данные успешно удалены")
        return True

    def edit_data(self, data=None, db=None):
        """Редактирование данных одного из жителей"""
        print("Мы тут")
        self.utils.editing(data, db)


    def empty_check(self):
        """Проверка на пустоту списка жителей"""

        if not self.citizens:
            print("Список жителей пуст")
            return True
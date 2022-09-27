from asm2204.st27.IO.FileIO import FileIO
from asm2204.st27.IO.Utils import Utils_console, Utils_web


class City:
    def __init__(self, source):
        self.citizens = dict()
        self.storage = FileIO(self)
        if source == "console":
            self.utils = Utils_console(self)
        elif source == "web":
            self.utils = Utils_web(self)
        self.maxID = 0

    def add(self, data=None):
        """Добавление нового жителя в список населения города"""
        self.utils.add(data)

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
        self.storage.save()

    def load(self):
        """Загрузка данных о населении города из файла"""

        self.storage.load()

    def delete(self, citizen_id = None):
        """Удаление данных одного из жителей"""
        self.utils.delete_citizen(citizen_id)

    def full_delete(self):
        """Удаление данных о всех жителях"""

        if self.empty_check():
                return False
        self.citizens.clear()
        print("Данные успешно удалены")
        return True

    def edit_data(self, data=None):
        """Редактирование данных одного из жителей"""
        print("Мы тут")
        self.utils.editing(data)


    def empty_check(self):
        """Проверка на пустоту списка жителей"""

        if not self.citizens:
            print("Список жителей пуст")
            return True
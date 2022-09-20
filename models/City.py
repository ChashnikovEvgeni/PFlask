from asm2204.st27.IO.FileIO import FileIO
from asm2204.st27.IO.Utils import Utils

class City:
    def __init__(self):
        self.citizens = dict()
        self.storage = FileIO(self)
        self.utils = Utils(self)
        self.maxID = 0

    def add(self):
        """Добавление нового жителя в список населения города"""

        self.utils.add()

    def write(self):
        """Ввывод списка жителей города"""

        if self.empty_check():
                return
        for id, human in self.citizens.items():
            print("----------------------------------------")
            human.write()
        print("----------------------------------------")

    def save(self):
        """Сохрание данных о городе в файл с расширением .dat"""

        if self.empty_check():
            return
        self.storage.save()

    def load(self):
        """Загрузка данных о населении города из файла"""

        self.storage.load()

    def delete(self):
        """Удаление данных одного из жителей"""

        if self.empty_check():
            return
        self.write()
        while True:
            try:
                id =  int(input("Укажите ID жителя для удаления его данных: "))
                del self.citizens[id]
                print("Данные о жителе успешно удалены")
                break
            except:
                print("Некорректное значение")


    def full_delete(self):
        """Удаление данных о всех жителях"""

        if self.empty_check():
                return
        while True:
            try:
                if int(input("""Вы точно хотите удалить всю картотеку?
                [1] Да
                [0] Отмена
                """)):
                    self.citizens.clear()
                    print("Данные успешно удалены")
                    break
                break
            except:
                print("Некорретное значение")

    def edit_data(self):
        """Редактирование данных одного из жителей"""

        if self.empty_check():
                return
        self.write()
        while True:
            try:
                id =  int(input("Укажите ID жителя, данные которого вы желаете изменить: "))
                self.utils.editing(self.citizens[id])
                break
            except:
                print("Некорректное значение")

    def empty_check(self):
        """Проверка на пустоту списка жителей"""

        if not self.citizens:
            print("Список жителей пуст")
            return True
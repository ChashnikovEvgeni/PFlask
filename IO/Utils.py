from asm2204.st27.models.Citizen import Citizen
from asm2204.st27.models.Doctor import Doctor
from asm2204.st27.models.Soldier import Soldier


class Utils:

    def __init__(self, city):
        self.city = city

    def editing(self, citizen):
        """Редактирование данных одного из жителей"""

        while True:
            print("------------- Информация о жителе ------------")
            citizen.write()
            choice = str(input("""
            Введите 0 для выхода или введите название поля,
            которое хотите изменить. Без пробела: """)).lower()
            if choice == "0":
                break
            elif choice == "id":
                print("Извините, значение поля ID изменить нельзя")
            elif citizen.fields.get(choice) == None:
                print("Введёно неверное имя поля")
            else:
                exec(f"citizen.{citizen.fields[choice]} = input('Введите значение поля: ')")


    def add(self):
        """Добавление данных одного жителя по вводу"""

        while True:
            print("""
        Данные о ком вы хотите добавить?
        [0] Вернуться назад
        [1] Обычный житель
        [2] Врач
        [3] Солдат
            """)

            choice = int(input())

            if choice == 0:
                break
            elif choice == 1:
                self.city.maxID += 1
                citizen = Citizen(id=self.city.maxID)
                citizen.read()
                self.city.citizens[citizen.id] = citizen
            elif choice == 2:
                self.city.maxID += 1
                doctor = Doctor(id=self.city.maxID)
                doctor.read()
                self.city.citizens[doctor.id] = doctor
            elif choice == 3:
                self.city.maxID += 1
                soldier = Soldier(id=self.city.maxID)
                soldier.read()
                self.city.citizens[soldier.id] = soldier
            else:
                print("Некорректное значение")
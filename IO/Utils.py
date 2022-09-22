from flask import flash

from asm2204.st27.models.Citizen import Citizen
from asm2204.st27.models.Doctor import Doctor
from asm2204.st27.models.Soldier import Soldier


class Utils_console:

    def __init__(self, city):
        self.city = city

    def delete_citizen(self, citizen=None):
        """Удаление данных одного из жителей"""
        if self.city.empty_check():
            return
        self.city.write()
        while True:
            try:
                id = int(input("Укажите ID жителя для удаления его данных: "))
                del self.city.citizens[id]
                print("Данные о жителе успешно удалены")
                break
            except:
                print("Некорректное значение или удаление невозможно")

    def editing(self, citizen):
        """Редактирование данных одного из жителей из консоли"""

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


    def add(self, data=None):
        """Добавление данных одного жителя по вводу из консоли"""

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



class Utils_web:

    def __init__(self, city):
         self.city = city


    def add(self, data):
        """Добавление данных нового жителя на основе данных от web-приложения"""


        if data["citizen_type"] == "Житель":
            citizen = Citizen()
            citizen.id = data["id"]
            citizen.first_name = data["first_name"]
            citizen.last_name = data["last_name"]
            citizen.age = data["age"]
            self.city.citizens[citizen.id] = citizen
            flash("Данные успешно внесены")
        elif data["citizen_type"] == "Врач":
            doctor = Doctor()
            doctor.id = data["id"]
            doctor.first_name = data["first_name"]
            doctor.last_name = data["last_name"]
            doctor.age = data["age"]
            doctor.hospital = data["hospital"]
            doctor.specialization = data["specialization"]
            self.city.citizens[doctor.id] = doctor
        elif data["citizen_type"] == "Солдат":
            soldier = Soldier()
            soldier.id = data["id"]
            soldier.first_name = data["first_name"]
            soldier.last_name = data["last_name"]
            soldier.age = data["age"]
            soldier.military_unit = data["military_unit"]
            soldier.rank = data["rank"]
            self.city.citizens[soldier.id] = soldier



    def delete_citizen(self, citizen_id=None):
        """Удаление данных одного из жителей из консоли"""

        if self.city.empty_check():
            return
        else:
            del self.city.citizens[citizen_id]

    def editing(self, data):
        """Редактирование данных одного из жителей из web-приложения"""

        if data["citizen_type"] == "Житель":
            citizen = Citizen()
            citizen.first_name = data["first_name"]
            citizen.last_name = data["last_name"]
            citizen.age = data["age"]
            self.city.maxID += 1
            citizen.id = self.city.maxID
            self.city.citizens[citizen.id] = citizen
            flash("Данные успешно внесены")
        elif data["citizen_type"] == "Врач":
            doctor = Doctor()
            doctor.first_name = data["first_name"]
            doctor.last_name = data["last_name"]
            doctor.age = data["age"]
            doctor.hospital = data["hospital"]
            doctor.specialization = data["specialization"]
            self.city.maxID += 1
            doctor.id = self.city.maxID
            self.city.citizens[doctor.id] = doctor
        elif data["citizen_type"] == "Солдат":
            soldier = Soldier()
            soldier.first_name = data["first_name"]
            soldier.last_name = data["last_name"]
            soldier.age = data["age"]
            soldier.military_unit = data["military_unit"]
            soldier.rank = data["rank"]
            self.city.maxID += 1
            soldier.id = self.city.maxID
            self.city.citizens[soldier.id] = soldier


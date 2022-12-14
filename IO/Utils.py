from flask import flash

from models.Citizen import Citizen
from models.Doctor import Doctor
from models.Soldier import Soldier


class Utils_web:

    def __init__(self, city):
         self.city = city

    def add(self, data, db):
        """Добавление данных нового жителя на основе данных от web-приложения"""

        if data["citizen_type"] == "Житель":
            citizen = Citizen()
            citizen.first_name = data["first_name"]
            citizen.last_name = data["last_name"]
            citizen.age = data["age"]
            self.city.maxID += 1
            citizen.id = self.city.maxID
            try:
                self.city.citizens[citizen.id] = citizen
                self.city.storageDB.addin_database(citizen, db)
            except:
                print("Ошибка сохранения данных")
            flash("Данные успешно внесены локально")
        elif data["citizen_type"] == "Доктор":
            doctor = Doctor()
            doctor.first_name = data["first_name"]
            doctor.last_name = data["last_name"]
            doctor.age = data["age"]
            doctor.hospital = data["hospital"]
            doctor.specialization = data["specialization"]
            self.city.maxID += 1
            doctor.id = self.city.maxID
            try:
                self.city.citizens[doctor.id] = doctor
                self.city.storageDB.addin_database(doctor, db)
            except:
                print("Ошибка сохранения данных")
            flash("Данные успешно внесены локально")
        elif data["citizen_type"] == "Солдат":
            soldier = Soldier()
            soldier.first_name = data["first_name"]
            soldier.last_name = data["last_name"]
            soldier.age = data["age"]
            soldier.military_unit = data["military_unit"]
            soldier.rank = data["rank"]
            self.city.maxID += 1
            soldier.id = self.city.maxID
            try:
                self.city.citizens[soldier.id] = soldier
                self.city.storageDB.addin_database(soldier, db)
            except:
                print("Ошибка сохранения данных")
            flash("Данные успешно внесены локально")



    def editing(self, data, db):
        """Редактирование данных одного из жителей из web-приложения"""

        if data["type"] == "Житель":
            citizen = Citizen()
            citizen.id = int(data["id"])
            citizen.first_name = data["first_name"]
            citizen.last_name = data["last_name"]
            citizen.age = data["age"]
            print(citizen)
            self.city.storageDB.update_database(citizen, db)
            self.city.citizens[citizen.id] = citizen
            flash("Данные успешно изменены локально!")
        elif data["type"] == "Доктор":
            doctor = Doctor()
            doctor.id = int(data["id"])
            doctor.first_name = data["first_name"]
            doctor.last_name = data["last_name"]
            doctor.age = data["age"]
            doctor.hospital = data["hospital"]
            doctor.specialization = data["specialization"]
            print(doctor)
            self.city.storageDB.update_database(doctor, db)
            self.city.citizens[doctor.id] = doctor
            flash("Данные успешно изменены!")
        elif data["type"] == "Солдат":
            soldier = Soldier()
            soldier.id = int(data["id"])
            soldier.first_name = data["first_name"]
            soldier.last_name = data["last_name"]
            soldier.age = data["age"]
            soldier.military_unit = data["military_unit"]
            soldier.rank = data["rank"]
            print(soldier)
            self.city.storageDB.update_database(soldier, db)
            self.city.citizens[soldier.id] = soldier
            flash("Данные успешно изменены!")


    def delete_citizen(self, citizen_id, db):
        """Удаление данных одного из жителей из консоли"""

        if self.city.empty_check():
            return
        else:
            if self.city.citizens[citizen_id].type == "Житель":
                table = "Citizen"
            elif  self.city.citizens[citizen_id].type == "Доктор":
                table = "Doctor"
            elif self.city.citizens[citizen_id].type == "Солдат":
                table = "Soldier"
            del self.city.citizens[citizen_id]
            self.city.storageDB.dell_data(table, citizen_id, db)



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

    def editing(self, data= None):
        """Редактирование данных одного из жителей из консоли"""

        if self.city.empty_check():
            return
        self.city.write()
        print("a yt nfv ult na")
        while True:
            try:
                id = int(input("Укажите ID жителя, данные которого вы желаете изменить: "))
                citizen = self.city.citizens[id]
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
                        self.city.citizens[id] = citizen
                break
            except:
                print("Некорректное значение")


    def add(self, data=None, db=None):
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




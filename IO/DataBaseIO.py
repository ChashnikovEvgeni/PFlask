from flask import flash

from asm2204.st27.models.Citizen import Citizen
from asm2204.st27.models.Doctor import Doctor
from asm2204.st27.models.Soldier import Soldier


class FDataBase:
    def __init__(self, city):
        self.city = city

    def setdb(self, db):
        """Привязкак курсора"""

        self.__db = db
        self.__cur = db.cursor()

    def addin_database(self, new_citizen, db):
        """Добавление в базу данных информации о новом жителя на основе данных от web-приложения"""

        self.setdb(db)
        try:
            if new_citizen.type == "Житель":
                self.__cur.execute("INSERT INTO Citizen VALUES( ?, ?, ?, ?, ?, ?)",
                                   (new_citizen.id, new_citizen.type, new_citizen.first_name, new_citizen.last_name,
                                    new_citizen.age, 1))
                self.__cur.execute("UPDATE City set maxID = ? where id =?", (new_citizen.id, 1) )
                self.__db.commit()
                flash("Данные успешно внесены в БД")
            elif new_citizen.type == "Доктор":
                self.__cur.execute("INSERT INTO Doctor VALUES( ?, ?, ?, ?, ?, ?, ?, ?)", (
                    new_citizen.id, new_citizen.type, new_citizen.first_name, new_citizen.last_name, new_citizen.age,
                    new_citizen.hospital,
                    new_citizen.specialization, 1))
                self.__cur.execute("UPDATE City set maxID = ? where id =?", (new_citizen.id, 1))
                self.__db.commit()
                flash("Данные успешно внесены в БД")
            elif new_citizen.type == "Солдат":
                self.__cur.execute("INSERT INTO Soldier VALUES( ?, ?, ?, ?, ?, ?, ?, ?)", (
                    new_citizen.id, new_citizen.type, new_citizen.first_name, new_citizen.last_name,
                    new_citizen.age, new_citizen.military_unit,
                    new_citizen.rank, 1))
                self.__cur.execute("UPDATE City set maxID = ? where id =?", (new_citizen.id, 1))
                self.__db.commit()
                flash("Данные успешно внесены в БД")

        except Exception as e:
            flash("Ошибка добавления данных в БД")
            print(e)

    def update_database(self, citizen_data, db):
        """Обновление данных одного из жителей в БД"""

        self.setdb(db)
        try:
            if citizen_data.type == "Житель":
                self.__cur.execute("UPDATE Citizen set first_name=? , last_name=? , age=? where id=? ", (citizen_data.first_name, citizen_data.last_name, citizen_data.age, citizen_data.id) )
                self.__db.commit()
                flash("Данные жителя успешно изменены в БД")
            elif citizen_data.type == "Доктор":
                self.__cur.execute("UPDATE Doctor set first_name=? , last_name=? , age=?, hospital=?,specialization=? where id=? ",
                                   (citizen_data.first_name, citizen_data.last_name, citizen_data.age, citizen_data.hospital, citizen_data.specialization, citizen_data.id))
                self.__db.commit()
                flash("Данные доктора успешно изменены в БД")
            elif citizen_data.type == "Солдат":
                self.__cur.execute(
                    "UPDATE Soldier set first_name=? , last_name=? , age=?, military_unit=?, rank=? where id=? ",
                    (citizen_data.first_name, citizen_data.last_name, citizen_data.age, citizen_data.military_unit,
                     citizen_data.rank, citizen_data.id))
                self.__db.commit()
                flash("Данные солдата успешно изменены в БД")
        except Exception as e:
            flash("Ошибка добавления данных в БД")
            print(e)


    def dell_data(self, table, citizen_id, db):
        """Удаление данных одного жителя из БД"""

        try:
            self.setdb(db)
            sql_query = "DELETE from " + table + " where id=?"
            self.__cur.execute(sql_query, (citizen_id,))
            self.__db.commit()
            print(self.city.maxID)
            flash("Данные успешно удалены из БД")
        except Exception as e:
            flash("Ошибка при удалении данных из БД")
            print(e)

    def dell_all_data(self, db):
        """Удаление всех данных города """

        try:
            self.setdb(db)
            self.__cur.execute("""DELETE from Citizen""")
            self.__cur.execute("""DELETE from Doctor""")
            self.__cur.execute("""DELETE from Soldier""")
            self.__cur.execute("UPDATE City set maxID = 0 where id =?", (1,))
            self.__db.commit()
            flash("БД отчищена")
        except Exception as e:
            flash("Ошибка отчистки БД")
            print(e)

    def load(self, db):
        """Импорт всех данных из БД"""

        self.setdb(db)
        city_data_select = '''SELECT * FROM City'''
        citizens_data_select = '''SELECT * FROM Citizen'''
        doctors_data_select = '''SELECT * FROM Doctor'''
        soldiers_data_select = '''SELECT * FROM Soldier'''
        try:
            self.__cur.execute(city_data_select)
            city_data = self.__cur.fetchone()  # получить выборку полученную в ходе выполнения sql запроса
            self.city.maxID = city_data[1]
            print("Данные города успешно получены")
            self.__cur.execute(citizens_data_select)
            citizens_data = self.__cur.fetchall()
            for row in citizens_data:
                citizen = Citizen()
                citizen.id = row[0]
                citizen.first_name = row[2]
                citizen.last_name = row[3]
                citizen.age = row[4]
                self.city.citizens[citizen.id] = citizen
            print("Данные простых жителей успешно получены")
            self.__cur.execute(doctors_data_select)
            doctors_data = self.__cur.fetchall()
            for row in doctors_data:
                doctor = Doctor()
                doctor.id = row[0]
                doctor.first_name = row[2]
                doctor.last_name = row[3]
                doctor.age = row[4]
                doctor.hospital = row[5]
                doctor.specialization = row[6]
                self.city.citizens[doctor.id] = doctor
            print("Данные докторов успешно получены")
            self.__cur.execute(soldiers_data_select)
            soldiers_data = self.__cur.fetchall()
            for row in soldiers_data:
                soldier = Soldier()
                soldier.id = row[0]
                soldier.first_name = row[2]
                soldier.last_name = row[3]
                soldier.age = row[4]
                soldier.military_unit = row[5]
                soldier.rank = row[6]
                self.city.citizens[soldier.id] = soldier
            print("Данные солдат успешно получены")
        except Exception as e:
            flash("Ошибка чтение данных из БД")
            print(e)

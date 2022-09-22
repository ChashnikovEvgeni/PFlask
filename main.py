from flask import Flask, render_template, request, flash
from asm2204.st27.models.Citizen import Citizen
from asm2204.st27.models.City import City
from asm2204.st27.models.Doctor import Doctor
from asm2204.st27.models.Soldier import Soldier

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'


city = City("web")


@app.route("/")
def index():
    print("я тут")
    return render_template('index.html')


@app.route("/load")
def load_population():
    city.load()
    city.write()
    flash("Данные успешно загружены")
    return render_template('population.html', population=city.citizens)


@app.route("/save")
def save_population():
    city.save()
    flash("Данные успешно сохранены")
    return render_template('index.html')


@app.route("/population")
def show_population():
    city.write()
    return render_template('population.html', population=city.citizens)


@app.route("/add1", methods=['POST', 'GET'])
def add1():
    if request.method == 'POST':
        try:
            if request.form["citizen_type"] == "Житель":
                citizen = Citizen()
                citizen.first_name = request.form["first_name"]
                citizen.last_name = request.form["last_name"]
                citizen.age = request.form["age"]
                city.add(citizen)
                flash("Данные успешно внесены")
            elif request.form["citizen_type"] == "Врач":
                doctor = Doctor()
                doctor.first_name = request.form["first_name"]
                doctor.last_name = request.form["last_name"]
                doctor.age = request.form["age"]
                doctor.hospital = request.form["hospital"]
                doctor.specialization = request.form["specialization"]
                city.add(doctor)
            elif request.form["citizen_type"] == "Солдат":
                soldier = Soldier()
                soldier.first_name = request.form["first_name"]
                soldier.last_name = request.form["last_name"]
                soldier.age = request.form["age"]
                soldier.military_unit = request.form["military_unit"]
                soldier.rank = request.form["rank"]
                city.add(soldier)
        except:
            flash("Во время сохранения данных произошла ошибка")

    return render_template('add.html', title="Добавление жителя")


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        try:
           city.add(request.form)
        except:
            flash("Во время сохранения данных произошла ошибка!")

    return render_template('add.html', title="Добавление жителя")


@app.route("/edit/<cititzen_id>")
def edit(citizen_id):
    if request.method == 'POST':
        try:
            city.add(request.form)
        except:
            flash("Во время сохранения данных произошла ошибка!")

    return render_template('add.html', title="Редактирование жителя")


@app.route("/dell/<int:citizen_id>")
def dell_citizen(citizen_id):
    city.delete(citizen_id)
    flash("Данные жителя успешно удалены")
    return render_template('population.html', population=city.citizens)

@app.route("/dell_all")
def dell_all():
    if city.full_delete():
        flash("Данные о всех жителях успешно удалены")
    else:
        flash("Список жителей пуст. Нет данных для удаления")
    return render_template('index.html')


def main():
    main_menu = [
        ["Выход", ],
        ["Показать список жителей", city.write],
        ["Добавить нового жителя", city.add],
        ["Редактировать данные жителя", city.edit_data],
        ["Удалить данные о жителе", city.delete],
        ["Удалить всю картотеку", city.full_delete],
        ["Сохранить данные о жителях в файл", city.save],
        ["Загрузить данные о жителях из файла", city.load],
    ]

    while True:
        print("----------------------------------------")
        for i, menuItem in enumerate(main_menu, 1):
            print(f"[{i - 1}] {menuItem[0]}")
        print("----------------------------------------")
        m = int(input("Введите номер действия: "))
        if m == 0:
            break
        else:
            try:
                main_menu[m][1]()
            except:
                print("Некорректное значение")

# while True:
#    choice = input("""
#    Режим запуска
#    [0] Выход
#    [1] Консоль
#    [2] Web-приложение
#    """)
#    if choice == "0":
#        break
#    elif choice == "1":
#        city = City("console")
#        if __name__ == '__main__':
#            main()
#    elif choice == "2":
#       print("Начали")
#       break
#    else:
#        print("Некорректное значение")



if __name__ == "__main__":
    app.run(debug=True)

if __name__ == '__main__':
    from group import group
else:
    from .group import group



def main():
    city = City()
    stop = False
    main_menu = [
        ["Выход", ],
        ["Показать список жителей", city.write],
        ["Добавить нового жителя", city.add],
        ["Редактировать данные жителя", city.edit_data],
        ["Удалить данные о жителе", city.delete],
        ["Удалить всю картотеку", city.full_delete],
        ["Сохранить данные о жителях в файл", city.save],
        ["Загрузить данные о жителях из файла", city.load],
    ]

    while stop == False:
        print("----------------------------------------")
        for i,menuItem in enumerate(main_menu, 1):
            print(f"[{i-1}] {menuItem[0]}")
        print("----------------------------------------")
        m = int(input("Введите номер действия: "))
        if m == 0:
            break
        else:
            try:
                main_menu[m][1]()
            except:
                print("Некорректное значение")
    group().f()



if __name__ == '__main__':
	main()



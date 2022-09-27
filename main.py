from flask import Flask, render_template, request, flash, redirect, url_for
from asm2204.st27.models.Citizen import Citizen
from asm2204.st27.models.City import City
from asm2204.st27.models.Doctor import Doctor
from asm2204.st27.models.Soldier import Soldier

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'

city = City("web")


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/load")
def load_population():
    city.load()
    city.write()
    flash("Данные успешно загружены")
    return redirect(url_for('show_population'))


@app.route("/save")
def save_population():
    city.save()
    flash("Данные успешно сохранены")
    return redirect(url_for('show_population'))


@app.route("/population")
def show_population():
    city.write()
    return render_template('population.html', population=city.citizens)


@app.route("/add/<citizen_type>", methods=['POST', 'GET'])
def add_citizen(citizen_type):
    if request.method == 'POST':
        try:
            city.add(request.form)
            return redirect(url_for('show_population'))
        except:
            flash("Во время сохранения данных произошла ошибка!")

    return render_template('add.html', title="Добавление жителя", citizen_type=citizen_type)


@app.route("/edit/<citizen_id>", methods=['POST', 'GET'])
def edit(citizen_id):
    if request.method == 'POST':
        try:
            city.edit_data(request.form)
        except:
            flash("Во время сохранения данных произошла ошибка!")
    citizen = city.citizens[int(citizen_id)]
    return render_template('edit.html', title="Редактирование жителя", citizen=citizen)


@app.route("/dell/<int:citizen_id>")
def dell_citizen(citizen_id):
    city.delete(citizen_id)
    flash("Данные жителя успешно удалены")
    return redirect(url_for('show_population'))


@app.route("/dell_all")
def dell_all():
    if city.full_delete():
        flash("Данные о всех жителях успешно удалены")
    else:
        flash("Список жителей пуст. Нет данных для удаления")
    return redirect(url_for('show_population'))


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title="Страница не найдена"), 404



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
    group().f()


if __name__ == '__main__':
    main()

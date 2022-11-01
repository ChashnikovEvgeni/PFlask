import os
import sqlite3

from flask import Flask, render_template, request, flash, redirect, url_for, g, current_app
from models.City import City


DATABASE = '/tmp/cities.db'
DEBUG = True
SECRET_KEY = 'fdgdfgdfggf786hfg6hfg6h7f'


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'cities.db')))

def connect_db():
    """Установка соединения с БД"""

    conn = sqlite3.connect(app.config['DATABASE'], check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    """Запуск sql-скрипта для создания БД"""

    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    """Соединение с БД, если оно ещё не установлено"""

    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db





city = City("web")


@app.route("/")
def index():
    db = get_db()
   # dbase = FDataBase(db)
    #listdb = dbase.getData()
    return redirect(url_for('show_population'))


@app.route("/load/<source>")
def load_population(source):
    db = get_db()
    city.load(source, db)
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
            db = get_db()
            city.add(request.form, db)
            return redirect(url_for('show_population'))
        except:
            flash("Во время сохранения данных произошла ошибка!")
    return render_template('add.html', title="Добавление жителя", citizen_type=citizen_type)

@app.route("/edit/<citizen_id>", methods=['POST', 'GET'])
def edit(citizen_id):
    if request.method == 'POST':
        try:
            db = get_db()
            city.edit_data(request.form, db)
        except:
            flash("Во время сохранения данных произошла ошибка!")
    citizen = city.citizens[int(citizen_id)]
    return render_template('edit.html', title="Редактирование жителя", citizen=citizen)


@app.route("/dell/<int:citizen_id>")
def dell_citizen(citizen_id):
    db = get_db()
    city.delete(citizen_id, db)
    flash("Данные жителя успешно удалены")
    return redirect(url_for('show_population'))


@app.route("/dell_all")
def dell_all():
    db = get_db()
    if city.full_delete(db):
        flash("Данные о всех жителях успешно удалены")
    else:
        flash("Список жителей пуст. Нет данных для удаления")
    return redirect(url_for('show_population'))


@app.teardown_appcontext
def close_db(error):
    """Закрываем соединение с бд, если оно было установлено"""

    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title="Страница не найдена"), 404



if __name__ == "__main__":
    app.run(debug=True)
    #city.load()



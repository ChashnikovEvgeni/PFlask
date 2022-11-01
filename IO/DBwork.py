import sqlite3

class DBwork:
    def __init__ (self, app):
        self.app = app

    def connect_db(self):
        conn = sqlite3.connect(self.app.config['DATABASE'])
        conn.row_factory = sqlite3.Row
        return conn

    def create_db(self):
        db = self.connect_db()
        with self.app.open_resource('sq_db.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        db.close()

    def get_db(self, g):
        """Соединение с бд, если оно ещё не установлено"""

        if not hasattr(g, 'link_db'):
            g.link_db = self.connect_db()
        return g.link_db
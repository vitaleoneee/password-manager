import os

import sqlite3


class Database:
    """ Implementation of CRUD operations of sqlite database """

    def __init__(self):
        os.makedirs('db', exist_ok=True)
        self.db = sqlite3.connect('db/passwords.db')
        self.cursor = self.db.cursor()
        self.init_db()

    def init_db(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT UNIQUE, password TEXT)")

    def get_passwords(self):
        self.cursor.execute("SELECT title, password FROM passwords")
        return self.cursor.fetchall()

    def create_password(self, title, password):
        self.cursor.execute("INSERT INTO passwords (title, password) VALUES (?, ?)", (title, password))
        self.db.commit()

    def delete_password(self, title):
        self.cursor.execute("DELETE FROM passwords WHERE title = ?", (title,))
        self.db.commit()

    def update_password(self, old_title, new_title, new_password):
        self.cursor.execute("UPDATE passwords SET title = ?, password = ? WHERE title = ?",
                            (new_title, new_password, old_title))
        self.db.commit()

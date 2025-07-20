import os

import sqlite3


class Database:
    def __init__(self):
        os.makedirs('database', exist_ok=True)
        self.db = sqlite3.connect('database/passwords.db')
        self.cursor = self.db.cursor()
        self.init_db()

    def init_db(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT, password TEXT)")

    def get_password(self, title):
        self.cursor.execute("SELECT title, password FROM passwords WHERE title = ?", (title,))
        return self.cursor.fetchone()

    def get_passwords(self):
        self.cursor.execute("SELECT title, password FROM passwords")
        return self.cursor.fetchall()

    def create_password(self, title, password):
        self.cursor.execute("INSERT INTO passwords (title, password) VALUES (?, ?)", (title, password))
        self.db.commit()

    def delete_password(self, title):
        self.cursor.execute("DELETE FROM passwords WHERE title = ?", (title,))
        self.db.commit()

    def update_password(self, record_id, new_title, new_password):
        self.cursor.execute("UPDATE passwords SET title = ?, password = ? WHERE id = ?",
                            (new_title, new_password, record_id))
        self.db.commit()

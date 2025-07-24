import os

import sqlite3
from cryptography.fernet import Fernet


class Database:
    """ Implementation of CRUD operations of sqlite database """

    def __init__(self):
        os.makedirs('db', exist_ok=True)
        self.db = sqlite3.connect('db/passwords.db')
        self.cursor = self.db.cursor()
        self.key = self._load_or_generate_key()
        self.cipher_suite = Fernet(self.key)
        self._init_db()

    def _init_db(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT UNIQUE, password TEXT)")

    def _load_or_generate_key(self):
        try:
            with(open('db/key.txt', 'rb')) as key_file:
                return key_file.read()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open('db/key.txt', 'wb') as key_file:
                key_file.write(key)
            return key

    def decrypt_password(self, encrypted_password):
        return self.cipher_suite.decrypt(encrypted_password).decode()

    def get_passwords(self):
        self.cursor.execute("SELECT title, password FROM passwords")
        encrypted_passwords = self.cursor.fetchall()
        decrypted_passwords = []
        for title, encrypted_password in encrypted_passwords:
            try:
                decrypted = self.decrypt_password(encrypted_password)
                decrypted_passwords.append((title, decrypted))
            except:
                decrypted_passwords.append((title, "DECRYPTION ERROR"))
        return decrypted_passwords

    def create_password(self, title, password):
        encrypted_password = self.cipher_suite.encrypt(password.encode())
        self.cursor.execute("INSERT INTO passwords (title, password) VALUES (?, ?)", (title, encrypted_password))
        self.db.commit()

    def delete_password(self, title):
        self.cursor.execute("DELETE FROM passwords WHERE title = ?", (title,))
        self.db.commit()

    def update_password(self, old_title, new_title, new_password):
        self.cursor.execute("UPDATE passwords SET title = ?, password = ? WHERE title = ?",
                            (new_title, new_password, old_title))
        self.db.commit()

import sqlite3

from PySide6.QtWidgets import QMessageBox

from ui_password_list import PasswordListWindow


def handle_save_password(parent_window, db, title, password):
    if not title or not password:
        QMessageBox.warning(parent_window, "Warning", "Please fill in all fields.")
        return
    try:
        db.create_password(title, password)
        QMessageBox.information(parent_window, 'Success', 'Password saved successfully!')
    except sqlite3.IntegrityError:
        QMessageBox.critical(parent_window, 'Error', 'The password with this title already exists!')


def open_password_list_window(parent_window):
    parent_window.password_list_window = PasswordListWindow()
    parent_window.password_list_window.show()

import sqlite3

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox


def handle_save_password(parent_window, db, title, password):
    if not title or not password:
        QMessageBox.warning(parent_window, "Warning", "Please fill in all fields.")
        return
    try:
        db.create_password(title, password)
        QMessageBox.information(parent_window, 'Success', 'Password saved successfully!')
    except sqlite3.IntegrityError:
        QMessageBox.critical(parent_window, 'Error', 'The password with this title already exists!')


def delete_password(parent_window, table, db, dispatcher):
    counter = 0
    for i in range(0, table.rowCount()):
        if table.item(i, 0).checkState() == Qt.Checked:
            db.delete_password(table.item(i, 0).text())
            counter += 1
    if counter == 0:
        QMessageBox.warning(parent_window, "Warning", "You have not chosen any passwords.")
        return
    QMessageBox.information(parent_window, 'Success', f'Removed {counter} password(s)')
    parent_window.hide()
    dispatcher.show_password_list()


def change_password():
    print(2)


def copy_password():
    print(3)

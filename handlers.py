import sqlite3

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QMessageBox, QApplication, QTableWidget


def handle_main_save_password(parent_window, db, title, password):
    if not title or not password:
        QMessageBox.warning(parent_window, "Warning", "Please fill in all fields.")
        return
    try:
        db.create_password(title, password)
        QMessageBox.information(parent_window, 'Success', 'Password saved successfully!')
        parent_window.input_name.clear()
        parent_window.input_password.clear()
    except sqlite3.IntegrityError:
        QMessageBox.critical(parent_window, 'Error', 'The password with this title already exists!')


def handle_change_password(parent_window, db, old_title, new_title, new_password, dispatcher):
    if not new_title or not new_password:
        QMessageBox.warning(parent_window, "Warning", "Please fill in all fields.")
        return
    try:
        db.update_password(old_title, new_title, new_password)
        QMessageBox.information(parent_window, 'Success', 'The changed password has been saved successfully!')
        parent_window.close()
        dispatcher.show_password_list()
    except sqlite3.IntegrityError:
        QMessageBox.critical(parent_window, 'Error', 'The password with this title already exists!')


def handle_delete_password(parent_window, table, db):
    counter = 0
    for i in range(0, table.rowCount()):
        if table.item(i, 0).checkState() == Qt.Checked:
            db.delete_password(table.item(i, 0).text())
            counter += 1
    if counter == 0:
        QMessageBox.warning(parent_window, "Warning", "You have not chosen any passwords.")
        return
    QMessageBox.information(parent_window, 'Success', f'Removed {counter} password(s)')
    parent_window.refresh_passwords_table()


def handle_list_button_change_password(parent_window, table, dispatcher, passwords):
    counter = 0
    selected_row = -1

    for i in range(table.rowCount()):
        item = table.item(i, 0)
        if item and item.checkState() == Qt.Checked:
            counter += 1
            if counter >= 2:
                QMessageBox.warning(parent_window, "Warning", "You have selected more than 1 password.")
                return
            selected_row = i

    if counter == 0:
        QMessageBox.warning(parent_window, "Warning", "You have not chosen any passwords.")
        return
    title = table.item(selected_row, 0).text()
    password = passwords[selected_row][1]

    dispatcher.show_password_details(parent_window, title, password)


def handle_password_details(parent_window, dispatcher, curr_title, curr_password):
    dispatcher.show_password_details(parent_window, curr_title, curr_password)


def handle_copy_password(row, password):
    QApplication.clipboard().setText(password)


def handle_search_item(parent_window, field_text, table):
    parent_window.refresh_passwords_table()
    for i in range(0, table.rowCount()):
        table_item = table.item(i, 0)
        if table_item.text() == field_text:
            table_item.setForeground(QColor("#ffeaa7"))
            table.scrollToItem(table_item, QTableWidget.PositionAtTop)
            return
    QMessageBox.warning(parent_window, 'Error', f'The password with title "{field_text}" does not exist.')

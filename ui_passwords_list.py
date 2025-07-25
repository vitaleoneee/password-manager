from PySide6.QtGui import QIcon, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout,
    QTableWidget, QHeaderView, QTableWidgetItem
)

from handlers import handle_delete_password, handle_copy_password, handle_list_button_change_password, \
    handle_search_item, handle_password_details
from styles import BUTTON_STYLE


class PasswordListWindow(QWidget):
    def __init__(self, db, dispatcher):
        super().__init__()
        self.setWindowTitle("Password list")
        self.setWindowIcon(QIcon("icons/icon.png"))
        self.resize(800, 400)
        self.db = db
        self.dispatcher = dispatcher

        self.search_input = QLineEdit()
        self.search_button = QPushButton("Search")
        self.search_button.setStyleSheet(BUTTON_STYLE)

        self.passwords_table = QTableWidget()
        self.passwords_table.setColumnCount(3)
        self.passwords_table.setHorizontalHeaderLabels(['Title', 'Password', 'Clipboard'])
        self.passwords_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.passwords_table.resizeRowsToContents()

        self.search_button.clicked.connect(
            lambda: handle_search_item(self, self.search_input.text(), self.passwords_table))

        self.delete_button = QPushButton("Delete")
        self.delete_button.setStyleSheet(BUTTON_STYLE)
        self.delete_button.clicked.connect(
            lambda: handle_delete_password(self, self.passwords_table, self.db))

        self.selected_objects_button = QPushButton("Change")
        self.selected_objects_button.setStyleSheet(BUTTON_STYLE)
        self.selected_objects_button.clicked.connect(
            lambda: handle_list_button_change_password(self, self.passwords_table, self.dispatcher, self.passwords))

        self.search_layout = QHBoxLayout()
        self.search_layout.addWidget(self.search_input)
        self.search_layout.addWidget(self.search_button)

        self.button_layout = QVBoxLayout()
        self.button_layout.addWidget(self.delete_button)
        self.button_layout.addWidget(self.selected_objects_button)

        self.table_layout = QHBoxLayout()
        self.table_layout.addWidget(self.passwords_table)
        self.table_layout.addLayout(self.button_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.search_layout)
        self.main_layout.addLayout(self.table_layout)
        self.setLayout(self.main_layout)

        self.refresh_passwords_table()

    def refresh_passwords_table(self):
        self.passwords = self.db.get_passwords()
        self.passwords_table.setRowCount(len(self.passwords))

        for i, db_object in enumerate(self.passwords):
            title, password = db_object

            item_title = QTableWidgetItem(str(title))
            item_title.setBackground(QColor("#454444"))
            item_title.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
            item_title.setCheckState(Qt.Unchecked)

            password_button = QPushButton('Password detail')
            password_button.setStyleSheet(BUTTON_STYLE)
            password_button.clicked.connect(
                lambda _, t=title, p=password: handle_password_details(self, self.dispatcher, str(t), str(p)))

            copy_button = QPushButton("Copy")
            copy_button.setStyleSheet(BUTTON_STYLE)
            copy_button.clicked.connect(
                lambda _, row=i, p=password,: handle_copy_password(row, str(p)))

            self.passwords_table.setItem(i, 0, item_title)
            self.passwords_table.setCellWidget(i, 1, password_button)
            self.passwords_table.setCellWidget(i, 2, copy_button)

    def closeEvent(self, event):
        self.dispatcher.show_main()
        super().closeEvent(event)

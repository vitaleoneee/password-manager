from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit

from handlers import handle_main_save_password
from styles import BUTTON_STYLE, INPUT_STYLE
from utils import generate_password


class MainWindow(QWidget):
    def __init__(self, db, dispatcher):
        super().__init__()
        self.setWindowTitle('Password Manager')
        self.setWindowIcon(QIcon('icons/icon.png'))
        self.resize(500, 150)
        self.dispatcher = dispatcher
        self.db = db

        self.button = QPushButton("List of passwords")
        self.button.setStyleSheet(BUTTON_STYLE)
        self.button.clicked.connect(self.dispatcher.show_password_list)

        self.label_new_password = QLabel('Fill in the fields to save')
        self.label_new_password.setAlignment(Qt.AlignCenter)

        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Enter website or name")
        self.input_name.setStyleSheet(INPUT_STYLE)

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Enter password")
        self.input_password.setStyleSheet(INPUT_STYLE)

        self.button_generate = QPushButton("Generate a secure password")
        self.button_generate.setStyleSheet(BUTTON_STYLE)
        self.button_generate.clicked.connect(lambda: generate_password(self.input_password))

        self.button_save = QPushButton("Save new password")
        self.button_save.setStyleSheet(BUTTON_STYLE)
        self.button_save.clicked.connect(
            lambda: handle_main_save_password(self, self.db, self.input_name.text(), self.input_password.text()))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label_new_password)
        self.layout.addWidget(self.input_name)
        self.layout.addWidget(self.input_password)
        self.layout.addWidget(self.button_generate)
        self.layout.addWidget(self.button_save)
        self.layout.addStretch()
        self.setLayout(self.layout)

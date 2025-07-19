from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit

from styles import BUTTON_STYLE, INPUT_STYLE


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Password Manager')
        self.setWindowIcon(QIcon('media/icon.png'))
        self.resize(500, 260)

        self.button = QPushButton("List of passwords")
        self.button.setStyleSheet(BUTTON_STYLE)

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

        self.button_save = QPushButton("Save new password")
        self.button_save.setStyleSheet(BUTTON_STYLE)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label_new_password)
        self.layout.addWidget(self.input_name)
        self.layout.addWidget(self.input_password)
        self.layout.addWidget(self.button_generate)
        self.layout.addWidget(self.button_save)
        self.layout.addStretch()
        self.setLayout(self.layout)

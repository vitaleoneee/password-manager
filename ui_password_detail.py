from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel

from handlers import handle_change_password
from styles import BUTTON_STYLE


class PasswordDetailWindow(QWidget):
    def __init__(self, parent_window, db, dispatcher, change_title, change_password):
        super().__init__()
        self.setWindowTitle("Password Detail")
        self.setWindowIcon(QIcon("media/icon.png"))
        self.resize(400, 180)
        self.parent_window = parent_window
        self.db = db
        self.dispatcher = dispatcher
        self.change_title = change_title
        self.change_password = change_password

        self.label_change_password = QLabel('Please change the data in the fields below')
        self.label_change_password.setAlignment(Qt.AlignCenter)

        self.change_input_name = QLineEdit()
        self.change_input_name.setText(self.change_title)
        self.old_title = self.change_input_name.text()

        self.change_password_name = QLineEdit()
        self.change_password_name.setText(self.change_password)

        self.change_button_save = QPushButton("Save changes")
        self.change_button_save.setStyleSheet(BUTTON_STYLE)
        self.change_button_save.clicked.connect(
            lambda: handle_change_password(self, self.db, self.old_title, self.change_input_name.text(),
                                           self.change_password_name.text(), self.dispatcher))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_change_password)
        self.layout.addWidget(self.change_input_name)
        self.layout.addWidget(self.change_password_name)
        self.layout.addWidget(self.change_button_save)

        self.layout.addStretch()
        self.setLayout(self.layout)

    def closeEvent(self, event):
        self.dispatcher.show_password_list()
        super().closeEvent(event)

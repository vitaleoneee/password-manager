from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout


class PasswordListWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Password list")
        self.setWindowIcon(QIcon("media/icon.png"))
        self.resize(500, 260)

        self.test_button = QPushButton("Test")
        self.sec_button = QPushButton("second")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.test_button)
        self.layout.addWidget(self.sec_button)
        self.layout.addStretch()
        self.setLayout(self.layout)

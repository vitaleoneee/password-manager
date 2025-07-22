from ui_main import MainWindow
from ui_password_list import PasswordListWindow


class WindowDispatcher:
    def __init__(self, db):
        self.db = db
        self.main_window = MainWindow(db, self)

    def show_main(self):
        self.main_window.show()

    def show_password_list(self):
        self.password_list_window = PasswordListWindow(self.db, self)
        self.password_list_window.show()
        self.main_window.hide()

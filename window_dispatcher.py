from ui_main import MainWindow
from ui_password_detail import PasswordDetailWindow
from ui_passwords_list import PasswordListWindow


class WindowDispatcher:
    def __init__(self, db):
        self.db = db
        self.main_window = MainWindow(db, self)
        self.password_list_window = None

    def show_main(self):
        self.main_window.show()
        if self.password_list_window:
            self.password_list_window.close()

    def show_password_list(self):
        if not self.password_list_window or not self.password_list_window.isVisible():
            self.password_list_window = PasswordListWindow(self.db, self)
        else:
            self.password_list_window.refresh_passwords_table()
        self.password_list_window.show()
        self.main_window.hide()

    def show_password_details(self, parent_window, change_title, change_password):
        self.password_detail_window = PasswordDetailWindow(parent_window, self.db, self, change_title, change_password)
        self.password_detail_window.show()

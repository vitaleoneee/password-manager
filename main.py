import sys
from PySide6.QtWidgets import QApplication

from database import Database
from ui_main import MainWindow

if __name__ == '__main__':
    db = Database()
    app = QApplication(sys.argv)
    window = MainWindow(db)
    window.show()
    sys.exit(app.exec_())

import sys
from PySide6.QtWidgets import QApplication

from database import Database
from window_dispatcher import WindowDispatcher

if __name__ == '__main__':
    db = Database()
    app = QApplication(sys.argv)
    window = WindowDispatcher(db)
    window.show_main()
    sys.exit(app.exec_())

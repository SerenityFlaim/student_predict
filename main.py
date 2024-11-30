import sys

from PySide6.QtWidgets import QApplication

from app_windows import StudentPredict, DataWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = StudentPredict()
    mw.show()

    sys.exit(app.exec())
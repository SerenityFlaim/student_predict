import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox

from main_window import Ui_MainWindow
from settings_dialog import Ui_Settings
from student_dialog import Ui_Student_data

class StudentPredict(QMainWindow):
    def __init__(self):
        super(StudentPredict, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class Settings(QDialog):
    def __init__(self):
        super(Settings, self).__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

class StudentData(QDialog):
    def __init__(self):
        super(StudentData, self).__init__()
        self.ui = Ui_Student_data()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = StudentPredict()
    s = Settings()
    sd = StudentData()
    mw.show()
    s.show()
    sd.show()

    sys.exit(app.exec())
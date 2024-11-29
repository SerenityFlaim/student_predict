from main_window import Ui_MainWindow
from settings_dialog import Ui_Settings
from student_dialog import Ui_Student_data

from PySide6.QtWidgets import QMainWindow, QDialog

class StudentPredict(QMainWindow):
    def __init__(self):
        super(StudentPredict, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.add_data_btn.clicked.connect(self.open_student_data_window)
        self.ui.settings_btn.clicked.connect(self.open_settings_window)

    def open_student_data_window(self):
        self.new_window = QDialog()
        self.ui_window = Ui_Student_data()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

    def open_settings_window(self):
        self.new_window = QDialog()
        self.ui_window = Ui_Settings()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()


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
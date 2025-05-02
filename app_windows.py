import os
from ui_compiled.main_window import Ui_MainWindow
from ui_compiled.settings_dialog import Ui_Settings
from ui_compiled.student_dialog import Ui_Student_data

from PySide6.QtWidgets import QMainWindow, QDialog, QDialogButtonBox
from PySide6.QtGui import QPixmap

from models.student_data import StudentData
from models.neural_model import NeuralModel
from models.error_handler import ErrorHandler

class StudentPredict(QMainWindow):
    def __init__(self):
        super(StudentPredict, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.data_window = None
        self.settings_window = None

        self.ui.add_data_btn.clicked.connect(self.open_student_data_window)
        self.ui.settings_btn.clicked.connect(self.open_settings_window)
        self.ui.predict_btn.clicked.connect(self.get_predicted_value)
        self.ui.features_btn.clicked.connect(self.show_plot)

    def open_student_data_window(self):
        self.data_window = DataWindow()
        self.data_window.show()

    def open_settings_window(self):
        self.settings_window = Settings()
        self.settings_window.show()

    def get_predicted_value(self):
        if self.data_window and self.settings_window:
            try:
                print("GET DATA")
                print(self.data_window.get_data())
                if (not self.data_window.get_data()):
                    raise ValueError
                student_data = StudentData(self.data_window.get_data())
                model = NeuralModel(self.settings_window.get_data())
                print(model.predict_value(student_data.data))
                self.ui.result_tbx.setText(str(model.predict_value(student_data.data)).replace('[', '').replace(']', ''))
            except ValueError:
                ErrorHandler.create_error("Данные о студенте не были введены.")
        else:
            ErrorHandler.create_error("Окна данных и настроек должны быть запущены перед прогнозом.")

    def show_plot(self):
        if self.settings_window:
            plot_file = NeuralModel(self.settings_window.get_data()).plot_file

            if self.ui.plot_lbl.pixmap().isNull():
                self.ui.plot_lbl.setPixmap(QPixmap(plot_file))
            else:
                self.ui.plot_lbl.clear()


class Settings(QDialog):
    def __init__(self):
        super(Settings, self).__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.data = ""
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).clicked.connect(self.read_data)

    def read_data(self):
        self.data = self.ui.model_cbx.currentText()
        print(self.data)

    def get_data(self):
        return self.data

class DataWindow(QDialog):
    def __init__(self):
        super(DataWindow, self).__init__()
        self.ui = Ui_Student_data()
        self.ui.setupUi(self)
        self.data = []
        self.er_handler = ErrorHandler()
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).clicked.connect(self.read_data)

    
    def read_data(self):
        result = []
        try:
            result.append(self.ui.gender_cbx.currentText())
            result.append(self.er_handler.check_positive(self.ui.hours_tbx.text(), "Значение количества часов должно быть положительным."))
            result.append(self.ui.prof_cbx.currentText())
            print(self.ui.prof_cbx.currentText())
            print(str(self.ui.prof_cbx.currentText()).encode('utf-8').decode('utf-8'))
            print(self.ui.prof_cbx.currentData())
            print(type(self.ui.prof_cbx.currentText()))
            result.append(self.ui.job_cbx.currentText())
            result.append(self.ui.activity_cbx.currentText())
            result.append(self.er_handler.check_positive_integer(self.ui.skips_tbx.text(), "Значение количества пропусков должно быть целым положительным."))
            self.data = result
            print(result)
        except ValueError:
            self.er_handler.msg_box.exec()
            self.data = []

    def get_data(self):
        return self.data
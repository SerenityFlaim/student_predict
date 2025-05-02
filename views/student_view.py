from ui_compiled.student_dialog import Ui_Student_data
from PySide6.QtWidgets import QDialog, QDialogButtonBox

class StudentView(QDialog):
    def __init__(self):
        super(StudentView, self).__init__()
        self.ui = Ui_Student_data()
        self.ui.setupUi(self)
        self.presenter = None

    def set_presenter(self, presenter):
        self.presenter = presenter
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).clicked.connect(self.presenter.on_ok)

    def get_inputs(self):
        return [
            self.ui.gender_cbx.currentText(),
            self.ui.hours_tbx.text(),
            self.ui.prof_cbx.currentText(),
            self.ui.job_cbx.currentText(),
            self.ui.activity_cbx.currentText(),
            self.ui.skips_tbx.text()
        ]
    
    def close_view(self):
        self.close()
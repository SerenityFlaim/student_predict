from models.student_data import StudentData
from models.error_handler import ErrorHandler

class StudentPresenter:
    def __init__(self, view):
        self.view = view
        self.view.set_presenter(self)
        self.data = None

    def show_view(self):
        self.view.show()

    def on_ok(self):
        raw = self.view.get_inputs()
        try:
            sd = StudentData(raw)
            self.data = sd.data
            self.view.close_view()
        except ValueError as e:
            ErrorHandler.create_error(str(e))
            self.data = None
from PySide6.QtGui import QPixmap
from models.neural_model import NeuralModel
from models.error_handler import ErrorHandler

class PredictController:
    def __init__(self, view, student_controller, settings_controller):
        self.view = view
        self.view.set_controller(self)
        self.student_controller = student_controller
        self.settings_controller = settings_controller
        self.plot_visible = False

    def show_view(self):
        self.view.show()

    def open_student_window(self):
        self.student_controller.show_view()

    def open_settings_window(self):
        self.settings_controller.show_view()

    def on_predict(self):
        if self.student_controller.data is None or self.student_controller.data.empty or not self.settings_controller.model_name:
            ErrorHandler.create_error("Сначала введите данные и выберите настройки.")
            return
        data = self.student_controller.data
        model = NeuralModel(self.settings_controller.model_name)
        result = model.predict_value(data)
        self.view.display_result(str(result).strip('[]'))

    def on_toggle_plot(self):
        if not self.settings_controller.model_name:
            return
        model = NeuralModel(self.settings_controller.model_name)
        pixmap = QPixmap(model.plot_file)
        if not self.plot_visible:
            self.view.show_plot(pixmap)
        else:
            self.view.clear_plot()
        self.plot_visible = not self.plot_visible
from PySide6.QtGui import QPixmap
from models.neural_model import NeuralModel
from models.error_handler import ErrorHandler

class PredictPresenter:
    def __init__(self, view, student_presenter, settings_presenter):
        self.view = view
        self.view.set_presenter(self)
        self.student_presenter = student_presenter
        self.settings_presenter = settings_presenter
        self.plot_visible = False

    def open_student_window(self):
        self.student_presenter.show_view()

    def open_settings_window(self):
        self.settings_presenter.show_view()

    def on_predict(self):
        if self.student_presenter.data is None or self.student_presenter.data.empty or not self.settings_presenter.model_name:
            ErrorHandler.create_error("Сначала введите данные и выберите настройки.")
            return
        data = self.student_presenter.data
        model = NeuralModel(self.settings_presenter.model_name)
        result = model.predict_value(data)
        self.view.display_result(str(result).strip('[]'))

    def on_toggle_plot(self):
        if not self.settings_presenter.model_name:
            return
        model = NeuralModel(self.settings_presenter.model_name)
        pixmap = QPixmap(model.plot_file)
        if not self.plot_visible:
            self.view.show_plot(pixmap)
        else:
            self.view.clear_plot()
        self.plot_visible = not self.plot_visible
from ui_compiled.predict import Ui_PredictWindow
from PySide6.QtWidgets import QMainWindow

class PredictView(QMainWindow):
        def __init__(self):
            super(PredictView, self).__init__()
            self.ui = Ui_PredictWindow()
            self.ui.setupUi(self)
            self.controller = None

        def set_controller(self, controller):
            self.controller = controller

            self.ui.add_data_btn.clicked.connect(self.controller.open_student_window)
            self.ui.settings_btn.clicked.connect(controller.open_settings_window)
            self.ui.predict_btn.clicked.connect(self.controller.on_predict)
            self.ui.features_btn.clicked.connect(self.controller.on_toggle_plot)

        def display_result(self, text: str):
             self.ui.result_tbx.setText(text)

        def show_plot(self, pixmap):
             self.ui.plot_lbl.setPixmap(pixmap)

        def clear_plot(self):
             self.ui.plot_lbl.clear()

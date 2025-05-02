from ui_compiled.main_window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

class PredictView(QMainWindow):
        def __init__(self):
            super(PredictView, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.presenter = None

        def set_presenter(self, presenter):
            self.presenter = presenter

            self.ui.add_data_btn.clicked.connect(self.presenter.open_student_window)
            self.ui.settings_btn.clicked.connect(presenter.open_settings_window)
            self.ui.predict_btn.clicked.connect(self.presenter.on_predict)
            self.ui.features_btn.clicked.connect(self.presenter.on_toggle_plot)

        def display_result(self, text: str):
             self.ui.result_tbx.setText(text)

        def show_plot(self, pixmap):
             self.ui.plot_lbl.setPixmap(pixmap)

        def clear_plot(self):
             self.ui.plot_lbl.clear()

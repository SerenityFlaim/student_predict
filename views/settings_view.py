from ui_compiled.settings_dialog import Ui_Settings
from PySide6.QtWidgets import QDialog, QDialogButtonBox

class SettingsView(QDialog):
    def __init__(self):
        super(SettingsView, self).__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.controller = None
        self.setWindowTitle("Настройки Модели")

    def set_controller(self, controller):
        self.controller = controller
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).clicked.connect(self.controller.on_ok)

    def get_selection(self):
        return self.ui.model_cbx.currentText()
    
    def close_view(self):
        self.close()
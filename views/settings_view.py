from ui_compiled.settings_dialog import Ui_Settings
from PySide6.QtWidgets import QDialog, QDialogButtonBox

class SettingsView(QDialog):
    def __init__(self):
        super(SettingsView, self).__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.presenter = None

    def set_presenter(self, presenter):
        self.presenter = presenter
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).clicked.connect(self.presenter.on_ok)

    def get_selection(self):
        return self.ui.model_cbx.currentText()
    
    def close_view(self):
        self.close()
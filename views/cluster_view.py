from ui_compiled.cluster import Ui_ClusterWindow
from PySide6.QtWidgets import QDialog

class ClusterView(QDialog):
    def __init__(self):
        super(ClusterView, self).__init__()
        self.ui = Ui_ClusterWindow()
        self.ui.setupUi(self)
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

        self.ui.importDataButton.clicked.connect(self.controller.on_import_data)
        # self.ui.enterDataButton.clicked.connect(self.controller.enter_data)
        self.ui.analyzeButton.clicked.connect(self.controller.on_analyze)
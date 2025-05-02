from ui_compiled.cluster_results import Ui_ClusterResultsWindow
from PySide6.QtWidgets import QDialog

class ClusterResultsView(QDialog):
    def __init__(self):
        super(ClusterResultsView, self).__init__()
        self.ui = Ui_ClusterResultsWindow()
        self.ui.setupUi(self)
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller
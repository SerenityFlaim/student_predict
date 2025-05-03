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

    def set_plot(self, pixmap):
        print("Pixmap size:", pixmap.size())
        self.ui.elbow_lbl.setPixmap(pixmap)
        self.ui.elbow_lbl.setScaledContents(True)
from ui_compiled.cluster_results import Ui_ClusterResultsWindow
from PySide6.QtWidgets import (
    QDialog, QWidget, QVBoxLayout,
    QHeaderView
    )

class ClusterResultsView(QDialog):
    def __init__(self):
        super(ClusterResultsView, self).__init__()
        self.ui = Ui_ClusterResultsWindow()
        self.ui.setupUi(self)
        self.controller = None
        self.setWindowTitle("Результаты")

        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)

    def set_controller(self, controller):
        self.controller = controller

        self.ui.fileButton.clicked.connect(self.controller.download_results)
        self.ui.clusterScatterButton.clicked.connect(self.controller.on_show_scatter)


    def set_plot(self, pixmap):
        print("Pixmap size:", pixmap.size())
        self.ui.elbow_lbl.setPixmap(pixmap)
        self.ui.elbow_lbl.setScaledContents(True)

    def set_centroids(self, table_model):
        self.ui.centersView.setModel(table_model)
        self.ui.centersView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def set_stats(self, table_model):
        self.ui.clusterStatsView.setModel(table_model)
        self.ui.clusterStatsView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
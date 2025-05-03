from ui_compiled.cluster import Ui_ClusterWindow
from PySide6.QtWidgets import (
    QDialog, QWidget, QVBoxLayout,
    QHeaderView, QCheckBox
    )
from PySide6.QtCore import Qt

class ClusterView(QDialog):
    def __init__(self):
        super(ClusterView, self).__init__()
        self.ui = Ui_ClusterWindow()
        self.ui.setupUi(self)
        self.controller = None
        self.selected_columns = []
        self.ui.metricFeatures_scrollArea.setWidgetResizable(True)

        #should be in ui_compiled?
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)

    def set_controller(self, controller):
        self.controller = controller

        self.ui.importDataButton.clicked.connect(self.controller.on_import_data)
        # self.ui.enterDataButton.clicked.connect(self.controller.enter_data)
        self.ui.analyzeButton.clicked.connect(self.controller.on_analyze)

    def set_table(self, table_model):
        self.ui.dataView.setModel(table_model)
        self.ui.dataView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    def set_metric_panel(self, numeric_columns):
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        for column in numeric_columns:
            checkbox = QCheckBox(column)
            checkbox.stateChanged.connect(self.update_selection)
            self.scroll_layout.addWidget(checkbox)
        self.ui.metricFeatures_scrollArea.setWidget(self.scroll_content)

    def update_selection(self, state):
        checkbox = self.sender()
        column_name = checkbox.text()
        if state == Qt.Checked:
            if column_name not in self.selected_columns:
                self.selected_columns.append(column_name)
        else:
            if column_name in self.selected_columns:
                self.selected_columns.remove(column_name)
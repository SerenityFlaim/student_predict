from ui_compiled.main_menu import Ui_MenuWindow
from PySide6.QtWidgets import QMainWindow

class MenuView(QMainWindow):
    def __init__(self):
        super(MenuView, self).__init__()
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self)
        self.controller = None
        self.setWindowTitle("Основное Меню")

    def set_controller(self, controller):
        self.controller = controller

        self.ui.predictWindowButton.clicked.connect(self.controller.open_predict_window)
        self.ui.clusterWindowButton.clicked.connect(self.controller.open_cluster_window)
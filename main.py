from PySide6.QtWidgets import QApplication
from views.menu_view import MenuView
from views.cluster_view import ClusterView
from views.cluster_results_view import ClusterResultsView
from views.predict_view import PredictView
from views.settings_view import SettingsView
from views.student_view import StudentView
from controllers.menu_controller import MenuController
from controllers.cluster_controller import ClusterController
from controllers.cluster_results_controller import ClusterResultsController
from controllers.predict_controller import PredictController
from controllers.settings_controller import SettingsController
from controllers.student_controller import StudentController

if __name__ == '__main__':
    app = QApplication([])
    menu_view = MenuView()
    cluster_view = ClusterView()
    cluster_results_view = ClusterResultsView()
    predict_view = PredictView()
    settings_view = SettingsView()
    student_view = StudentView()

    settings_contr = SettingsController(settings_view)
    student_contr = StudentController(student_view)
    predict_contr = PredictController(predict_view, student_contr, settings_contr)
    cluster_results_contr = ClusterResultsController(cluster_results_view)
    cluster_contr = ClusterController(cluster_view, cluster_results_contr)
    menu_contr = MenuController(menu_view, predict_contr, cluster_contr)

    menu_view.show()
    app.exec()

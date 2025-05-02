from PySide6.QtWidgets import QApplication
from views.predict_view import PredictView
from views.settings_view import SettingsView
from views.student_view import StudentView
from presenters.predict_presenter import PredictPresenter
from presenters.settings_presenter import SettingsPresenter
from presenters.student_presenter import StudentPresenter

if __name__ == '__main__':
    app = QApplication([])
    main_view = PredictView()
    settings_view = SettingsView()
    student_view = StudentView()

    settings_pres = SettingsPresenter(settings_view)
    student_pres = StudentPresenter(student_view)
    main_pres = PredictPresenter(main_view, student_pres, settings_pres)

    main_view.show()
    app.exec()

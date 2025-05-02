class SettingsController:
    def __init__(self, view):
        self.view = view
        self.view.set_controller(self)
        self.model_name = None

    def show_view(self):
        self.view.show()

    def on_ok(self):
        self.model_name = self.view.get_selection()
        self.view.close_view()
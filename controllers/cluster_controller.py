

class ClusterController:
    def __init__(self, view, results_controller):
        self.view = view
        self.view.set_controller(self)
        self.results_controller = results_controller

    def show_view(self):
        self.view.show()

    def on_analyze(self):
        self.results_controller.show_view()
class ClusterResultsController:
    def __init__(self, view):
        self.view = view
        self.view.set_controller(self)
        self.plot_visible = None

    def show_view(self):
        self.view.show()
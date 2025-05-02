class MenuController:
    def __init__(self, view, predict_controller, cluster_controller):
        self.view = view
        self.view.set_controller(self)
        self.predict_controller = predict_controller
        self.cluster_controller = cluster_controller

    def open_predict_window(self):
        self.predict_controller.show_view()

    def open_cluster_window(self):
        self.cluster_controller.show_view()
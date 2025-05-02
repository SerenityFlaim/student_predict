from models.file_processor import FileProcessor

class ClusterController:
    def __init__(self, view, results_controller):
        self.view = view
        self.view.set_controller(self)
        self.results_controller = results_controller

    def show_view(self):
        self.view.show()

    def on_import_data(self):
        fp = FileProcessor()
        fp.select_csv_file()
        df = fp.csv_to_dataframe()
        print(df)

    def on_analyze(self):
        self.results_controller.show_view()
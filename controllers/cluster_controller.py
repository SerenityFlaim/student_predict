from models.file_processor import FileProcessor
from models.pandas_model import PandasModel

class ClusterController:
    def __init__(self, view, results_controller):
        self.view = view
        self.view.set_controller(self)
        self.results_controller = results_controller
        self.table_model = None

    def show_view(self):
        self.view.show()

    def on_import_data(self):
        fp = FileProcessor()
        fp.select_csv_file()
        df = fp.csv_to_dataframe()
        self.load_df(df)
        numeric_columns = df.select_dtypes(include=['number']).columns
        self.view.set_metric_panel(numeric_columns)
        print(df)

    def load_df(self, df):
        self.table_model = PandasModel(df)
        self.view.set_table(self.table_model)

    def on_analyze(self):
        self.results_controller.show_view()
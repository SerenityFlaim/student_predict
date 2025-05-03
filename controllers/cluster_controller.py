from models.file_processor import FileProcessor
from models.pandas_model import PandasModel
from models.cluster_strategy import ClusterKMeansStrategy, ClusterDBSCANStrategy
from models.error_handler import ErrorHandler
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import Qt
import pandas as pd

class ClusterController:
    def __init__(self, view, results_controller):
        self.view = view
        self.view.set_controller(self)
        self.results_controller = results_controller
        self.table_model = None
        self.strategy = None

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

    def on_enter_data(self, rows=50, cols=12):
        empty_df = pd.DataFrame( #12 50 12
            [[""]*12 for _ in range(50)],
            columns=[f"Column_{i+1}" for i in range(12)]
        )
        self.load_df(empty_df)
        self.view.set_metric_panel([])

    def set_strategy(self, cluster_strategy):
        self.strategy = cluster_strategy

    def transform_dataframe(self, df, selected_cols):
        existing_cols = [col for col in selected_cols if col in df.columns]
        df_filtered = df[existing_cols].copy()

        mask = ~df_filtered.applymap(lambda x: isinstance(x, str) and x.strip() == "").any(axis=1)
        df_cleaned = df_filtered[mask]

        return df_cleaned


    def on_analyze(self):
        if self.view.ui.radioKMeans.isChecked():
            self.set_strategy(ClusterKMeansStrategy())
        elif self.view.ui.radioDBSCAN.isChecked():
            self.set_strategy(ClusterDBSCANStrategy())
        else:
            ErrorHandler.create_error("Метод кластеризации не был выбран.")

        n_clusters = int(self.view.ui.numClusters_tbx.text())
        data_frame = self.table_model.get_updated_data()
        selected_cols = self.view.selected_columns
        print(selected_cols)
        df_transformed = self.transform_dataframe(data_frame, selected_cols)
        print(df_transformed)

        self.strategy.cluster(df_transformed, n_clusters)
        result = self.strategy.get_labels()
        print("RESULT")
        print(result)
        print("CENTERS")
        print(self.strategy.get_centroids())
        

        self.results_controller.show_view()

    def handle_paste(self):
        try:
            current_index = self.view.ui.dataView.currentIndex()
            if not current_index.isValid():
                return False
                
            clipboard = QGuiApplication.clipboard()
            text = clipboard.text()
            
            if not text:
                return False
                
            rows = [row.split('\t') for row in text.split('\n') if row]
            pasted_data = pd.DataFrame(rows)
            
            if current_index.row() == 0:
                new_headers = []
                for c in range(min(pasted_data.shape[1], self.table_model.columnCount())):
                    header = str(pasted_data.iloc[0, c])
                    new_headers.append(header)
                    self.table_model.setHeaderData(c, Qt.Horizontal, header)
                
                self.table_model._data = self.table_model._data.infer_objects()
                start_row = 1
            else:
                start_row = 0
                
            for r in range(start_row, pasted_data.shape[0]):
                for c in range(pasted_data.shape[1]):
                    target_row = current_index.row() + r - (start_row if start_row else 0)
                    target_col = current_index.column() + c
                    
                    if (target_row < self.table_model.rowCount() and 
                        target_col < self.table_model.columnCount()):
                        index = self.table_model.index(target_row, target_col)
                        self.table_model.setData(index, pasted_data.iloc[r, c])
            
            numeric_cols = []
            for col in self.table_model._data.columns:
                try:
                    converted = pd.to_numeric(self.table_model._data[col], errors='raise')
                    num_numeric = len(converted.dropna())
                    if num_numeric >= 3:
                        numeric_cols.append(col)
                        self.table_model._data[col] = converted
                    else:
                        self.table_model._data[col] = self.table_model._data[col].astype(object)
                except:
                    continue

            numeric_cols = self.table_model._data.select_dtypes(include='number').columns
            self.view.set_metric_panel(numeric_cols)

            df = self.table_model._data
            df.fillna("", inplace=True)
            
            self.table_model._data = df
            self.table_model.layoutChanged.emit()

            return True
        
        except Exception as e:
            print(f"Paste error: {e}")
            return False
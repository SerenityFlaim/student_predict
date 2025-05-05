from PySide6.QtGui import QPixmap
from models.plotter import Plotter
from io import BytesIO
import matplotlib.pyplot as plt
from models.pandas_model import PandasModel
from models.file_processor import FileProcessor
from models.error_handler import ErrorHandler
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

class ClusterResultsController:
    def __init__(self, view):
        self.view = view
        self.view.set_controller(self)
        self.plot_visible = False
        self.result_df = None

    def show_view(self):
        self.view.show()

    def set_plot_visible(self, flag: bool):
        self.plot_visible = flag

    def configure_results(self, df, labels, centroids=None):
        if self.plot_visible:
            plotter = Plotter()
            plotter.plot_elbow_method(df)
            figure = plotter.get_figure()

            buf = BytesIO()
            figure.savefig(buf, format='png', dpi=300)
            buf.seek(0)
            
            pixmap = QPixmap()
            pixmap.loadFromData(buf.getvalue(), 'PNG')
            self.view.set_plot(pixmap)
            plt.close(plotter.current_figure)

            centroid_df = pd.DataFrame(centroids)
            self.load_df(centroid_df, self.view.set_centroids)
        
        self.add_cluster_column(df, labels)
        stats_df = self.calculate_cluster_statistics(self.result_df)
        self.load_df(stats_df, self.view.set_stats)

    def load_df(self, df, view_method):
        table_model = PandasModel(df)
        view_method(table_model)

    def add_cluster_column(self, data_frame, labels):
        df_with_clusters = data_frame.copy()
        df_with_clusters["Cluster"] = labels
        self.result_df = df_with_clusters

    def download_results(self):
        fp = FileProcessor()
        dest_path = fp.select_res_dest()
        print(dest_path)
        save_path = f"{dest_path}/clustered_data.csv"
        self.result_df.to_csv(save_path, index=False)

    def calculate_cluster_statistics(self, df):
        stats = df["Cluster"].value_counts(dropna=False).sort_index()
        result = {}

        valid_total = 0

        for cluster_id, count in stats.items():
            if pd.isna(cluster_id):
                result['Missing'] = count
            else:
                result[int(cluster_id)] = count
                valid_total += count

        result['Valid'] = valid_total
        if 'Missing' not in result:
            result['Missing'] = 0

        stats_df = pd.DataFrame.from_dict(result, orient='index', columns=["Cases"])
        return stats_df

    def on_show_scatter(self):
        if len(self.result_df.columns) > 3:
            ErrorHandler.create_error("Для Scatter Plot необходимо только 2 признака.")
        else:
            pl = Plotter()
            print(self.result_df.columns[0])
            print(self.result_df.columns[1])
            pl.plot_scatter_clusters(self.result_df, self.result_df.columns[0], self.result_df.columns[1])
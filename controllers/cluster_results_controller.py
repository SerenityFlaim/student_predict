from PySide6.QtGui import QPixmap
from models.plotter import Plotter
from io import BytesIO
import matplotlib.pyplot as plt
from models.pandas_model import PandasModel
from models.file_processor import FileProcessor
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
            self.load_df(centroid_df)
        
        self.add_cluster_column(df, labels)

    def load_df(self, df):
        table_model = PandasModel(df)
        self.view.set_centroids(table_model)

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
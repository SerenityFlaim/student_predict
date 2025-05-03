from PySide6.QtGui import QPixmap
from models.plotter import Plotter
from io import BytesIO
import matplotlib.pyplot as plt
from models.pandas_model import PandasModel
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

class ClusterResultsController:
    def __init__(self, view):
        self.view = view
        self.view.set_controller(self)
        self.plot_visible = False

    def show_view(self):
        self.view.show()

    def set_plot_visible(self, flag: bool):
        self.plot_visible = flag

    def configure_results(self, df, centroids=None):
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

    def load_df(self, df):
        table_model = PandasModel(df)
        self.view.set_centroids(table_model)

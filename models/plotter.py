import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class Plotter():
    def __init__(self):
        self.current_figure = None

    def plot_elbow_method(self, data_frame, max_k=10):
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data_frame)

        inertias = []
        for k in range(1, max_k + 1):
            model = KMeans(n_clusters=k, random_state=42)
            model.fit(scaled_data)
            inertias.append(model.inertia_)

        rgb_color = (0/255, 204/255, 255/255)

        self.current_figure, ax = plt.subplots(figsize=(8, 5))
        ax.plot(range(1, max_k+1), inertias, marker='o', color=rgb_color)
        ax.set(
            title='Метод Локтя',
            xlabel='Кол-во кластеров (k)',
            ylabel='Сумма квадратов расстояний'
        )
        ax.set_xticks(range(1, max_k+1))
        ax.grid(True)

    def plot_scatter_clusters(self, df, x_col, y_col):
        current_figure, ax = plt.subplots(figsize=(8, 6))
        if 'Cluster' in df.columns:
            scatter = ax.scatter(df[x_col], df[y_col], c=df['Cluster'], cmap='viridis', s=50)
            legend = ax.legend(*scatter.legend_elements(), title="Cluster")
            ax.add_artist(legend)
        else:
            ax.scatter(df[x_col], df[y_col], color='gray', s=50)

        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title('Кластеризация: {} vs {}'.format(x_col, y_col))
        ax.grid(True)
        current_figure.show()
    
    def get_figure(self):
        return self.current_figure

    def show(self):
        if self.current_figure:
            self.current_figure.show()

    def save(self, filename, dpi=300):
        if self.current_figure:
            self.current_figure.savefig(filename, dpi=dpi, bbox_inches='tight')
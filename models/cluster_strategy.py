from abc import ABC, abstractmethod
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
import pandas as pd

class ClusterStrategyInterface(ABC):
    @abstractmethod
    def cluster(self, data_frame: pd.DataFrame, n_clusters: int):
        pass

    @abstractmethod
    def get_labels(self):
        pass


class ClusterKMeansStrategy(ClusterStrategyInterface):
    def __init__(self):
        self.model = None
        self.labels_ = None
        self.scaler = StandardScaler()
        self.cluster_centers_ = None
    
    def cluster(self, data_frame: pd.DataFrame, n_clusters: int = 3):
        scaled_data = self.scaler.fit_transform(data_frame)
        self.model = KMeans(n_clusters=n_clusters, random_state=42)
        self.labels_ = self.model.fit_predict(scaled_data)
        self.cluster_centers_ = self.model.cluster_centers_

    def get_labels(self):
        return self.labels_
    
    def get_centroids(self):
        return self.scaler.inverse_transform(self.cluster_centers_)
        
class ClusterDBSCANStrategy(ClusterStrategyInterface):
    def __init__(self, eps: float = 0.05, min_samples: int = 3):
        self.eps = eps
        self.min_samples = min_samples
        self.model = None
        self.labels_ = None
        self.scaler = StandardScaler()

    def cluster(self, data_frame: pd.DataFrame, n_clusters: int = None):
        scaled_data = self.scaler.fit_transform(data_frame)
        self.model = DBSCAN(eps=self.eps, min_samples=self.min_samples)
        self.labels_ = self.model.fit_predict(scaled_data)

    def get_labels(self):
        return self.labels_
    
    def get_centroids(self):
        return None
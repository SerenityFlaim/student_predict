from keras._tf_keras.keras.models import load_model 
from keras._tf_keras.keras.losses import MeanSquaredError
from xgboost import XGBRegressor



class NeuralModel():
    def __init__(self, model_name):
        self.model = self.create_model(model_name)
        print(self.model)

    def predict_value(self, dataframe):
        return self.model.predict(dataframe)

    def create_model(self, model_name):
        if (model_name == "Sequential"):
            return SequentialModel().model
        elif (model_name == "XGB"):
            return XgbModel().model
        else:
            return None

class SequentialModel():
    def __init__(self):
        self.model = load_model("network_models/sequential_model.h5", custom_objects={'mse': MeanSquaredError()})

class XgbModel():
    def __init__(self):
        self.model = XGBRegressor()
        self.model.load_model("network_models/xgb_model.bin")
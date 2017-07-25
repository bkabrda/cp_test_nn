class NNWithScaler:
    def __init__(self, network, scaler):
        self.network = network
        self.scaler = scaler

    def predict(self, X):
        X = self.scaler.transform(X)
        return self.network.predict(X)

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

class NNWithScaler:
    def __init__(self):
        self.network = MLPClassifier(hidden_layer_sizes=(500, 500))
        self.scaler = StandardScaler()

    def predict(self, X):
        X = self.scaler.transform(X)
        return self.network.predict(X)

    def train(self, data):
        X, y = [], []
        X = data['dataset']
        y = data['results']

        self.scaler.fit(X)
        X = self.scaler.transform(X)
        self.network.fit(X, y)

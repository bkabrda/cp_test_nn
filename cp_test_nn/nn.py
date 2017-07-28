import logging

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

logger = logging.getLogger(__name__)

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

        logger.info('Training neural network with dataset of %d samples', len(X))
        logger.debug('Scaling features')
        self.scaler.fit(X)
        X = self.scaler.transform(X)
        logger.debug('Fitting neural network to dataset')
        self.network.fit(X, y)
        logger.info('Neural network was successfuly trained')

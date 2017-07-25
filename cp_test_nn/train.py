import json

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

from cp_test_nn.nn import NNWithScaler

def train(dataset_file):
    X, y = [], []
    with open(dataset_file) as f:
        loaded = json.load(f)
    X = loaded['dataset']
    y = loaded['results']

    clf = MLPClassifier(hidden_layer_sizes=(200, 200))
    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)
    clf.fit(X, y)
    return NNWithScaler(clf, scaler)

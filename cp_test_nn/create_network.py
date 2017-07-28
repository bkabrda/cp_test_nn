import logging

from cp_test_nn import process
from cp_test_nn.dataset import create_dataset
from cp_test_nn.nn import NNWithScaler

logger = logging.getLogger(__name__)

def create_network(input, tokens):
    data = create_dataset(process.failures(input), tokens)
    nn = NNWithScaler()
    nn.train(data)
    return nn

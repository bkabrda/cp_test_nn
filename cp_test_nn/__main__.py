import sys

from cp_test_nn.predict import test_cv_success_rate
from cp_test_nn.create_network import create_network

network = create_network(sys.argv[1])

if len(sys.argv) > 2:
    test_cv_success_rate(network, sys.argv[2])

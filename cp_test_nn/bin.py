import argparse

from cp_test_nn.create_network import create_network
from cp_test_nn.predict import test_cv_success_rate
from cp_test_nn.nn import NNWithScaler

def main():
    parser = argparse.ArgumentParser(prog='cp_test_nn')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--trainingset', help='Path to training set of data')
    group.add_argument('-l', '--load', help='Load serialized neural network from given file')
    parser.add_argument('-c', '--cvset', help='Path to cross validation set of data')
    parser.add_argument('-s', '--serialize', help='Serialize trained neural network to given file')
    args = parser.parse_args()

    if args.load:
        network = NNWithScaler.load(args.load)
    else:
        network = create_network(args.trainingset)

    if args.serialize:
        network.serialize(args.serialize)

    if args.cvset:
        test_cv_success_rate(network, args.cvset)

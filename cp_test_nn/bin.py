import argparse
import pickle

from cp_test_nn import process
from cp_test_nn.tokenizer import create_token_dict
from cp_test_nn.create_network import create_network
from cp_test_nn.predict import test_cv_success_rate

def main():
    parser = argparse.ArgumentParser(prog='cp_test_nn')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--trainingset', help='Path to training set of data')
    group.add_argument('-l', '--load', help='Load serialized neural network from given file')
    parser.add_argument('-c', '--cvset', help='Path to cross validation set of data')
    parser.add_argument('-s', '--serialize', help='Serialize trained neural network to given file')
    args = parser.parse_args()

    if args.load:
        with open(args.load, 'rb') as f:
            (tokens, network) = pickle.load(f)
    else:
        tokens = create_token_dict(process.failures(args.trainingset))
        network = create_network(args.trainingset, tokens)

    if args.serialize:
        with open(args.serialize, 'wb') as f:
            pickle.dump((tokens, network), f)

    if args.cvset:
        test_cv_success_rate(network, tokens, args.cvset)

import argparse
import logging
import pickle

from cp_test_nn import logging_setup
from cp_test_nn import process
from cp_test_nn.tokenizer import create_token_dict
from cp_test_nn.create_network import create_network
from cp_test_nn.predict import predict

def probability(f):
    f = float(f)
    if f < 0.5 or f > 1.0:
        raise argparse.ArgumentTypeError('{} is not a number between 0.5 and 1.0'.format(f))
    return f


def main():
    parser = argparse.ArgumentParser(prog='cp_test_nn')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--trainingset', help='Path to training set of data')
    group.add_argument('-l', '--load', help='Load serialized neural network from given file')
    parser.add_argument('-p', '--predict', help='Path to prediction or cross validation set of data')
    parser.add_argument('-s', '--serialize', help='Serialize trained neural network to given file')
    parser.add_argument('-r', '--threshold', help='Probability threshold used to consider neural '
                        'network result safe to use. Number between 0.5 and 1.0',
                        type=probability)
    parser.add_argument('-q', '--quiet', help='Disable all logging output', action='store_true')
    parser.add_argument('-v', '--verbose', help='Provide verbose logging output',
                        action='store_true')
    args = parser.parse_args()

    if not args.quiet:
        logging_setup(logging.DEBUG if args.verbose else logging.INFO)

    if args.load:
        with open(args.load, 'rb') as f:
            (tokens, network) = pickle.load(f)
    else:
        tokens = create_token_dict(process.failures(args.trainingset))
        network = create_network(args.trainingset, tokens)

    if args.serialize:
        with open(args.serialize, 'wb') as f:
            pickle.dump((tokens, network), f)

    if args.predict:
        kwargs = {}
        if args.threshold is not None:
            kwargs['prob_thresh'] = args.threshold
        predict(network, tokens, args.predict, **kwargs)

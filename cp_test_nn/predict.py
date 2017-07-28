import logging
import sys

from cp_test_nn import process
from cp_test_nn.dataset import create_dataset

logger = logging.getLogger(__name__)


def predict(nn, tokens, cv_file):
    logger.info('Predicting results')
    data = create_dataset(process.failures(cv_file), tokens)
    X = data['dataset']
    y = data['results']

    # Statistics that get triggered when we have result data
    successes = 0
    false_negatives = 0
    false_positives = 0
    total_count = 0

    for i, item in enumerate(X):
        pred = nn.predict([item])[0]
        sys.stdout.write("{0} {1} {2} {3} {4}\n".format(
            pred and "FLAKE  " or "NOT    ",
            data["items"][i]["pull"],
            data["items"][i]["test"],
            data["items"][i]["context"],
            data["items"][i].get("url", "")
        ))
        # TODO: Use the probability prediction to print data about how sure we are this is a flake
        sys.stderr.write("  {0}\n  {1}\n".format(repr(nn.predict([item])), repr(nn.predict_proba([item]))))
        if y[i] >= 0:
            logger.debug('Predicted item %d to be %d => %s', i + 1, pred,
                         'correct' if pred == y[i] else 'wrong')
            total_count += 1
            if pred == y[i]:
                successes += 1
            elif pred == 1:
                false_positives += 1
            else:
                false_negatives += 1

    # Statistics
    if total_count:
        sys.stderr.write('Success rate: {0}\n'.format(successes / total_count))
        sys.stderr.write('False positives: {0}\n'.format(false_positives / total_count))
        sys.stderr.write('False negatives: {0}\n'.format(false_negatives / total_count))

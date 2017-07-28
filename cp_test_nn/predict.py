import logging

from cp_test_nn import process
from cp_test_nn.dataset import create_dataset

logger = logging.getLogger(__name__)


def test_cv_success_rate(nn, tokens, cv_file):
    logger.info('Testing success rate on cross-validation set')
    data = create_dataset(process.failures(cv_file), tokens)
    X = data['dataset']
    y = data['results']

    successes = 0
    false_negatives = 0
    false_positives = 0
    total_count = len(X)
    for i, item in enumerate(X):
        pred = nn.predict([item])
        logger.debug('Predicted item %d to be %d => %s', i + 1, pred[0],
                     'correct' if pred == [y[i]] else 'wrong')
        if pred == [y[i]]:
            successes += 1
        elif pred == [1]:
            false_positives += 1
        else:
            false_negatives += 1
    print('Success rate: ', successes/total_count)
    print('False positives: ', false_positives/total_count)
    print('False negatives: ', false_negatives/total_count)

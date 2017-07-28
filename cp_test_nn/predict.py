import logging
import sys

from cp_test_nn import process
from cp_test_nn.dataset import create_dataset

logger = logging.getLogger(__name__)

PREDICT_PROB_THRESHOLD = 0.75


def predict(nn, tokens, cv_file, prob_thresh=PREDICT_PROB_THRESHOLD):
    logger.info('Predicting results')
    data = create_dataset(process.failures(cv_file), tokens)
    X = data['dataset']
    y = data['results']

    # Statistics that get triggered when we have result data
    successes = 0
    false_negatives = 0
    false_positives = 0
    unsure = 0
    total_count = 0

    for i, item in enumerate(X):
        pred_proba = nn.predict_proba([item])[0]
        # we only assign 0 or 1 to pred if one of the probabilities is bigger than prob_thresh
        pred = None
        pred_text = "UNSURE "
        if max(pred_proba) >= prob_thresh:
            pred = int(pred_proba[1] >= pred_proba[0])
            pred_text = "FLAKE  " if pred == 1 else "NOT    "

        sys.stdout.write("{pred} {flake_proba:.6f} {p} {pull} {test} {context} {url}\n".format(
            pred=pred_text,
            flake_proba=pred_proba[1],
            p=nn.predict([item])[0],
            pull=data["items"][i]["pull"],
            test=data["items"][i]["test"],
            context=data["items"][i]["context"],
            url=data["items"][i].get("url", "")
        ))

        if y[i] >= 0:
            logger.debug('Predicted item %d to be %d => %s', i + 1, pred_text.strip(),
                         'correct' if pred == y[i] else 'wrong')
            total_count += 1
            if pred == y[i]:
                successes += 1
            elif pred == 1:
                false_positives += 1
            elif pred == 0:
                false_negatives += 1
            else:
                unsure += 1

    # Statistics
    if total_count:
        sys.stderr.write('Success rate: {0}\n'.format(successes / total_count))
        sys.stderr.write('False positives: {0}\n'.format(false_positives / total_count))
        sys.stderr.write('False negatives: {0}\n'.format(false_negatives / total_count))
        sys.stderr.write('Unsure: {0}\n'.format(unsure / total_count))

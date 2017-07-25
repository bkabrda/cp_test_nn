import json

from cp_test_nn.process import process
from cp_test_nn.dataset import create_dataset
from cp_test_nn.util import TOKEN_DICT_FILE, FAILS_CV_FILE, DATASET_CV_FILE

def test_cv_success_rate(nn, cv_file):
    process(cv_file, FAILS_CV_FILE)
    create_dataset(FAILS_CV_FILE, TOKEN_DICT_FILE, DATASET_CV_FILE)
    X, y = [], []
    with open(DATASET_CV_FILE) as f:
        cv = json.load(f)
        X = cv['dataset']
        y = cv['results']

    successes = 0
    false_negatives = 0
    false_positives = 0
    total_count = len(X)
    for i, item in enumerate(X):
        pred = nn.predict([item])
        if pred == [y[i]]:
            successes += 1
        elif pred == [1]:
            false_positives += 1
        else:
            false_negatives += 1
    print('Success rate: ', successes/total_count)
    print('False positives: ', false_positives/total_count)
    print('False negatives: ', false_negatives/total_count)

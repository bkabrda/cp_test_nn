import re

FAILS_FILE = 'fails'
TOKEN_DICT_FILE = 'tokens'
DATASET_FILE = 'dataset'

FAILS_CV_FILE = 'fails_cv'
DATASET_CV_FILE = 'dataset_cv'

num_re = re.compile(r'^\d+(\.\d+)?$')
split_re = re.compile(r'[^a-zA-Z0-9/\'\\:._-]')

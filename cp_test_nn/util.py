import re

FAILS_FILE = 'fails'
TOKEN_DICT_FILE = 'tokens'
DATASET_FILE = 'dataset'

FAILS_CV_FILE = 'fails_cv'
DATASET_CV_FILE = 'dataset_cv'

SPECIAL_TOKEN_PREFIX = 'SpecialToken:'
NUM_TOKEN = SPECIAL_TOKEN_PREFIX + 'Number'
UUID_TOKEN = SPECIAL_TOKEN_PREFIX + 'UUID'

num_re = re.compile(r'^\d+(\.\d+)?$')
uuid_re = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.I)
split_re = re.compile(r'[^a-zA-Z0-9/\'\\:._-]')

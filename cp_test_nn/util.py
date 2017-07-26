import re

FAILS_FILE = 'fails'
TOKEN_DICT_FILE = 'tokens'
DATASET_FILE = 'dataset'

FAILS_CV_FILE = 'fails_cv'
DATASET_CV_FILE = 'dataset_cv'

SPECIAL_TOKEN_PREFIX = 'SpecialToken:'
NUM_TOKEN = SPECIAL_TOKEN_PREFIX + 'Number'
UUID_TOKEN = SPECIAL_TOKEN_PREFIX + 'UUID'
WS_CERTS_TOKEN = SPECIAL_TOKEN_PREFIX + 'WSCerts'

num_re = re.compile(r'^\d+(\.\d+)?$')
uuid_re = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.I)
ws_certs_re = re.compile(r'^/etc/cockpit/ws-certs.d/0-self-signed.cert:[\w/]+$')
split_re = re.compile(r'[^a-zA-Z0-9/\'\\:._-]')

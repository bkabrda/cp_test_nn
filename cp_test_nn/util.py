import re

FAILS_FILE = 'fails'
TOKEN_DICT_FILE = 'tokens'
DATASET_FILE = 'dataset'

FAILS_CV_FILE = 'fails_cv'
DATASET_CV_FILE = 'dataset_cv'

SPECIAL_TOKEN_PREFIX = 'SpecialToken:'
NUM_TOKEN = SPECIAL_TOKEN_PREFIX + 'Number'
PERCENT_TOKEN = SPECIAL_TOKEN_PREFIX + 'Percent'
TIME_TOKEN = SPECIAL_TOKEN_PREFIX + 'Time'
UUID_TOKEN = SPECIAL_TOKEN_PREFIX + 'UUID'
WS_CERTS_TOKEN = SPECIAL_TOKEN_PREFIX + 'WSCerts'

num_re = re.compile(r'^\d+(\.\d+)?$')
percent_re = re.compile(r'^\d+(\.\d+)?%$')
uuid_re = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.I)
ws_certs_re = re.compile(r'^/etc/cockpit/ws-certs.d/0-self-signed.cert:[\w/\+]+$')
time_re = re.compile(r'\d\d:\d\d:\d\d')
split_re = re.compile(r'[\s]')
py_exception_re = re.compile(r'(Traceback \(most recent call last\):\n( .*\n)+([^\n]+))',
                             re.MULTILINE)

token_regexes = {
    NUM_TOKEN: num_re,
    PERCENT_TOKEN: percent_re,
    TIME_TOKEN: time_re,
    UUID_TOKEN: uuid_re,
    WS_CERTS_TOKEN: ws_certs_re,
}

#!/usr/bin/python3
import collections
import json
import re

import json_lines

from cp_test_nn.util import (num_re, uuid_re, split_re,
                             UUID_TOKEN, NUM_TOKEN)

def unify_token(t):
    if len(t) < 4:
        return None
    elif len(set(t)) == 1:
        # omit stuf like "--------------------------"
        return None
    elif num_re.match(t):
        return NUM_TOKEN
    elif uuid_re.match(t):
        return UUID_TOKEN

    return t

token_dict = collections.defaultdict(int)

def tokenize_log(log):
    split = split_re.split(log)
    result = []
    for i in split:
        unified = unify_token(i)
        if unified is not None:
            result.append(unified)
    return result

def create_token_dict(fails_file, token_dict_file):
    with json_lines.open(fails_file) as f:
        for item in f:
            for t in tokenize_log(item['log']):
                token_dict[t] += 1

    with open(token_dict_file, 'w') as f:
        json.dump(token_dict, f)

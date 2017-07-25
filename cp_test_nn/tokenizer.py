#!/usr/bin/python3
import collections
import json
import re

import json_lines

from cp_test_nn.util import num_re, split_re

def ignored_token(t):
    if len(t) < 4:
        return True
    if num_re.match(t):
        return True

token_dict = collections.defaultdict(int)

def create_token_dict(fails_file, token_dict_file):
    with json_lines.open(fails_file) as f:
        for item in f:
            split = split_re.split(item['log'])
            for s in split:
                if not ignored_token(s):
                    token_dict[s] += 1

    with open(token_dict_file, 'w') as f:
        json.dump(token_dict, f)

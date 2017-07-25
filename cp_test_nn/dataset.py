#!/usr/bin/python3
import json
import operator
import sys

import json_lines

from cp_test_nn.util import split_re

TOP_TOKENS = 500

def get_top_tokens(tokens_file, top_tokens):
    with open(tokens_file) as f:
        tokens = json.load(f)

    usetokens = []
    for token, count in sorted(tokens.items(), key=operator.itemgetter(1), reverse=True):
        usetokens.append(token)
        if len(usetokens) == top_tokens:
            break

    return usetokens

def create_dataset(fails_file, tokens_file, dataset_file):
    tokens = get_top_tokens(tokens_file, TOP_TOKENS)
    results = []

    i = 0
    with json_lines.open(fails_file) as f, open(dataset_file, 'w') as d:
        d.write('{"dataset": [\n')
        for item in f:
            if i > 0:
                d.write(',\n')
            sys.stderr.write('{i}\n'.format(i=i))
            i += 1
            tokenized_log = split_re.split(item['log'])
            features_item = []
            for token in tokens:
                features_item.append(tokenized_log.count(token))
            d.write(str(features_item))
            results.append(int(item['head']))
        d.write('],\n')
        d.write(' "results": ')
        d.write(str(results))
        d.write('}')

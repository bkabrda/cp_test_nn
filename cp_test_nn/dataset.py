#!/usr/bin/python3
import json
import operator
import sys

import json_lines

from cp_test_nn.tokenizer import tokenize_log

TOP_TOKENS = 9000

def load_token_data(tokens_file, top_tokens):
    with open(tokens_file) as f:
        loaded = json.load(f)

    tokens = loaded.get('tokens', {})

    usetokens = []
    for token, count in sorted(tokens.items(), key=operator.itemgetter(1), reverse=True):
        usetokens.append(token)
        if len(usetokens) == top_tokens:
            break

    loaded['tokens'] = usetokens
    return loaded

def create_dataset(fails_file, tokens_file, dataset_file):
    token_data = load_token_data(tokens_file, TOP_TOKENS)
    results = []

    i = 0
    with json_lines.open(fails_file) as f, open(dataset_file, 'w') as d:
        d.write('{"dataset": [\n')
        for item in f:
            if i > 0:
                d.write(',\n')
            sys.stderr.write('{i}\n'.format(i=i))
            i += 1
            tokenized_log = tokenize_log(item['log'])
            features_item = []
            # firstly output features for contexts
            for context in token_data['contexts']:
                features_item.append(int(item['context'] == context))
            for test in token_data['tests']:
                features_item.append(int(item['test'] == test))
            # secondly output features for tokens
            for token in token_data['tokens']:
                features_item.append(tokenized_log.count(token))
            d.write(str(features_item))
            results.append(int(item['head']))
        d.write('],\n')
        d.write(' "results": ')
        d.write(str(results))
        d.write('}')

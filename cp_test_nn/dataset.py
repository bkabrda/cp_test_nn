#!/usr/bin/python3
import operator
import sys

from cp_test_nn.tokenizer import tokenize_log

TOP_TOKENS = 9000

def filter_token_data(loaded, top_tokens):
    tokens = loaded.get('tokens', {})

    usetokens = []
    for token, count in sorted(tokens.items(), key=operator.itemgetter(1), reverse=True):
        usetokens.append(token)
        if len(usetokens) == top_tokens:
            break

    return {
        'tokens': usetokens,
        'contexts': loaded['contexts'],
        'tests': loaded['tests']
    }

def create_dataset(items, tokens):
    token_data = filter_token_data(tokens, TOP_TOKENS)
    results = []
    dataset = []

    i = 0
    for item in items:
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
        dataset.append(features_item)
        results.append(int(item['head']))

    # Debugging code
    # with open('dataset', 'wb') as f:
    #     json.dump({ "dataset": dataset, "results": results }, f)

    return {
        "dataset": dataset,
        "results": results
    }

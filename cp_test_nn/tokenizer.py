#!/usr/bin/python3
import collections

from cp_test_nn.util import token_regexes, split_re, py_exception_re

def unify_token(t):
    if len(t) < 4:
        return None
    elif len(set(t)) == 1:
        # omit stuf like "--------------------------"
        return None
    else:
        for name, regex in token_regexes.items():
            if regex.match(t):
                return name

    return t


def tokenize_log(log):
    py_exceptions = py_exception_re.findall(log)
    log = py_exception_re.sub('', log)
    result = [e[0] for e in py_exceptions]

    split = split_re.split(log)
    for i in split:
        unified = unify_token(i)
        if unified is not None:
            result.append(unified)
    return result


def create_token_dict(items):
    # TODO: rename from "tokenizer" and "create_token_dict", since we're now
    #  adding not only tokens, but also contexts
    token_dict = collections.defaultdict(int)
    contexts = set()
    tests = set()

    for item in items:
        for t in tokenize_log(item['log']):
            token_dict[t] += 1
        contexts.add(item['context'])
        tests.add(item['test'])

    tokens = {
        'tokens': token_dict,
        'contexts': sorted(contexts),
        'tests': sorted(tests)
    }

    # Debugging code
    # with open('tokens', 'wb') as f:
    #     json.dump(tokens, f)

    return tokens

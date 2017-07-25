#!/usr/bin/python3
import json

import json_lines

def process(input_file, fails_file):
    with json_lines.open(input_file) as i, open(fails_file, 'w') as o:
        for item in i:
            if item['status'] == 'failure':
                json.dump(item, o)
                o.write('\n')

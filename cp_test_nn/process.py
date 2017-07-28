#!/usr/bin/python3
import json
import logging

logger = logging.getLogger(__name__)


def failures(input_file):
    logger.debug('Searching input file %s for failures', input_file)
    with open(input_file) as f:
        while True:
            line = f.readline()
            if not line:
                break
            if "failure" in line:
                item = json.loads(line)
                if item['status'] == 'failure':
                    yield item

# -*- coding: utf-8 -*-
import configparser
import time
import sys
import os

# Path initialization
with open('path.config', 'r', encoding='utf-8') as f:
    PATHS = [path.replace('\n', '') for path in f]

def main():
    query = sys.argv[1]
    results = search(query)

    if len(results) == 0:
        print('Did not find {}'.format(query))
    elif len(results) > 1:
        for index, path in enumerate(results):
            print('[{}] {}'.format(index, path))
        menu(results[int(input('Select: '))])
    else:
        menu(results[0])

def menu(path):
    os.system("start cd {}".format(path))

def search(query):
    results = []

    for path in PATHS:
        for subdir, rootdir, _ in os.walk(path):
            if query.lower() in [rd.lower() for rd in rootdir]:
                results.append('{}\\{}'.format(subdir, query))
    return results

if __name__ == '__main__':
    main()

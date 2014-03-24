#!/usr/bin/env python

import argparse
import getpass
import socket
import sys

import requests

from diggy.framework_guesser import FrameworkGuesser
from diggy.miner import Miner


class App(object):

    def __init__(self):
        return

    def run(self, urls):
        for url in urls:
            print('#' * 72)
            print('URL: %s' % url)
            print('IP Address: %s' % Miner.get_ip(url))
            try:
                rsp = requests.get(url)
            except Exception:
                print('ERROR retrieving %s' % url)
                continue
            
            print('***********')
            print('* Headers *')
            print('***********')
            print('x-generator: %s' % rsp.headers.get('x-generator'))
            print('x-served-by: %s' % rsp.headers.get('x-served-by'))

            print('*****************')
            print('* Inferred info *')
            print('*****************')
            print('Framework: %s' % FrameworkGuesser.guess_framework(rsp))


if __name__ == '__main__':

    program_desc = 'Visit URL(s) and get info'

    usage = '''
  %(prog)s <url>
  %(prog)s -f <filename>

  options: [-h|--help]
'''

    parser = argparse.ArgumentParser(description=program_desc, usage=usage)

    parser.add_argument('-f', action='store_true', help='URLs are coming from a file if present')
    parser.add_argument('data', type=str, help='URL or file that contains URLs')

    args = parser.parse_args()

    urls = []

    if args.f:
        with open(args.data, 'r') as f:
            for line in f:
                urls.append(line.strip())
    else:
        urls.append(args.data)

    app = App()
    app.run(urls)

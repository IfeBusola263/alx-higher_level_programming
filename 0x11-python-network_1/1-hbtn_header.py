#!/usr/bin/python3
"""
This module implements a request to print the variable of the response
"""

import urllib.request
from sys import argv

with urllib.request.urlopen(argv[1]) as response:
    print(response.headers['X-Request-Id'])

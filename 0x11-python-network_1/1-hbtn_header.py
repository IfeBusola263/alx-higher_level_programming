#!/usr/bin/python3
"""
This module implements a request to print the variable of the response
"""

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers['X-Request-Id'])

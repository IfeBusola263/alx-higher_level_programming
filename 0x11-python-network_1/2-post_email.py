#!/usr/bin/python3
"""
This module send a post request to a URL passed as argument
"""

import urllib.request
import sys

post = urllib.request.Request(sys.argv[1], sys.argv[2].encode('ascii'))

with urllib.request.urlopen(post) as response:
    print(response)

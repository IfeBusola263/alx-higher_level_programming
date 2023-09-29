#!/usr/bin/python3
"""
This module implements a request to print a header variable
of the response
"""

if __name__ == '__main__':
    import urllib.request
    import sys


    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])

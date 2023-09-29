#!/usr/bin/python3
"""
This module prints the X-Request-Id content of the header
for a request response from a url
"""
if __name__ == '__main__':
    import requests
    import sys

    res = requests.get(sys.argv[1])
    if 'X-Request-Id' in res.headers:
        print(res.headers['X-Request-Id'])

#!/usr/bin/python3
"""
This module sends a request to a URL and displays the body
It also manages the HTTPError exception
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')

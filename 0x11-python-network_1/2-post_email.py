#!/usr/bin/python3
"""
This module send a post request to a URL passed as argument
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data)
    post = urllib.request.Request(sys.argv[1], data.encode('ascii'))

    with urllib.request.urlopen(post) as response:
        print(response.read().decode('utf-8'))

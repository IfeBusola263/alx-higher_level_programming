#!/usr/bin/python3
"""
This module send a request and displays the body
it also handles the error
"""
if __name__ == '__main__':
    import requests
    import sys

    res = requests.get(sys.argv[1])
    if res.status_code == requests.codes.ok:
        print(res.text)
    else:
        print('Error code: {}'.format(res.status_code))

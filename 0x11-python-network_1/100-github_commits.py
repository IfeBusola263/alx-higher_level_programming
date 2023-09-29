#!/usr/bin/python3
"""
This module prints the last ten commits by a user, given
the repo name and user name
"""
if __name__ == '__main__':
    import sys
    import requests

    res = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[1], sys.argv[2]))

    result = res.json()

    for i in range(10):
        name = result[i]["commit"]
        name = name["author"]
        print(f'{result[i]["sha"]}: {name["name"]}')

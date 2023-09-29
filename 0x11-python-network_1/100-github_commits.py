#!/usr/bin/python3
"""
This module prints the last ten commits by a user, given
the repo name and user name
"""
if __name__ == '__main__':
    import sys
    import requests

    res = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1]))

    result = res.json()

    i = 0

    for info in result:
        if i == 9:
            break
        name = info["commit"]
        name = name["author"]
        print(f'{info["sha"]}: {name["name"]}')

    # for i in range(10):
    #     name = result[i]["commit"]
    #     name = name["author"]
    #     print(f'{result[i]["sha"]}: {name["name"]}')

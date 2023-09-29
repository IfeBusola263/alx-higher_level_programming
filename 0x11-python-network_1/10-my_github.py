#!/usr/bin/python3
"""
This script displays your user_id on github
"""
if __name__ == '__main__':
    import requests
    import sys

    resp = requests.get('https://api.github.com/user',
                        auth=(sys.argv[1], sys.argv[2]))

    try:
        result = resp.json()
        if result:
            if 'id' in result:
                print(result['id'])
            else:
                print('None')
    except requests.exceptions.JSONDecodeError as e:
        print('None')

#!/usr/bin/python3
"""
This module sends a post request to url
"""
if __name__ == '__main__':
    import sys
    import requests

    num_of_args = len(sys.argv) - 1

    if num_of_args == 0:
        data = {'q': ""}
    else:
        data = {'q': sys.argv[1]}

    res = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        result = res.json()
        if result:
            print('[{}] {}'.format(result['id'], result['name']))
        else:
            print('No result')

    except requests.exceptions.JSONDecodeError as e:
        print('Not a valid JSON')

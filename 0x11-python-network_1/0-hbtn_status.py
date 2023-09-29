#!/usr/bin/python3
"""
This module uses the urllib.request package to make an http request
"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        msg = res.msg
        form = res.read()
        print('Body response:')
        # print('\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'.format(
        #     type(form), form, msg))
        print(f'\t- type: {type(form)}')
        print(f'\t- content: {form}')
        print(f'\t- utf8 content: {form.decode("utf-8")}')

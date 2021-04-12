#!/usr/bin/python

import requests
from sys import argv

print("please fill the empty fields")
print("if you face problem with tor, make sure you have your tor running. and in case change the port")

cookies = {
    '__cfduid': '',
    'csrftoken': '',
    'sessionid': '',
    'cf_use_ob': '0',
}

user_agent = ""
x_csrftoken = ""


def tor_session():
    session = requests.session()
    session.proxies = {
       'http': 'socks5://127.0.0.1:9050',
       'https': 'socks5://127.0.0.1:9050'
    }
    return session

print("use tor?\n(type yes or press enter: )", end="")
if input() == "yes":
    session = tor_session()
else:
    session = requests.session()

if argv[1] == "code":
    while True:
        code = input("code:").replace("#", "")
        if not str.isnumeric(code):
            print("that wasn't a code! (exiting)")
            exit(1)
        headers = {
            'User-Agent': user_agent,
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': f'https://nhentai.net/g/{code}/',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': x_csrftoken,
            'Origin': 'https://nhentai.net',
            'DNT': '1',
            'Connection': 'keep-alive',
            'TE': 'Trailers',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        response = session.post(f'https://nhentai.net/api/gallery/{code}/favorite', headers=headers, cookies=cookies)
        print(code + ':', response.text)
    
else:
    cfile = input("file:")
    with open(cfile, 'r') as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        for code in content:
            code = code.replace("#", "")
            headers = {
                'User-Agent': user_agent,
                'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.5',
                'Referer': f'https://nhentai.net/g/{code}/',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': x_csrftoken,
                'Origin': 'https://nhentai.net',
                'DNT': '1',
                'Connection': 'keep-alive',
                'TE': 'Trailers',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
            }
            response = session.post(f'https://nhentai.net/api/gallery/{code}/favorite', headers=headers, cookies=cookies)
            print(code + ':', response.text)

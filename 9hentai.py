#!/usr/bin/python

import requests

print("please replace blank fields, from request headers")

code_file = input("code_file:")
with open(code_file, 'r') as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    for code in content:
        headers = {
            'authority': '9hentai.ru',
            'accept': 'application/json, text/plain, */*',
            'dnt': '1',
            'x-xsrf-token': "",
            'x-csrf-token': "",
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': "",
            'content-type': 'application/json;charset=UTF-8',
            'sec-gpc': '1',
            'origin': 'https://9hentai.ru',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://9hentai.ru/g/{}/'.format(code),
            'accept-language': 'en-US,en;q=0.9',
            'cookie': '',
        }

        data = '{"id":' + code +'}'

        response = requests.post('https://9hentai.ru/api/user/onFap', headers=headers, data=data)
        print(response.text)
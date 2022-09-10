import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def is_bitlink(token, url):
    parts_of_link = urlparse(url)
    bitlink = f'{parts_of_link.netloc}{parts_of_link.path}'
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    return response.ok


def count_clicks(token, bitlink):
    headers = {'Authorization': f'Bearer {token}'}
    parts_of_link = urlparse(bitlink)
    bitlink = f'{parts_of_link.netloc}{parts_of_link.path}'
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    params = {'bitlink': bitlink}
    response = requests.get(bitly_url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']

def get_link():
    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='Ссылка или битлинк')
    args = parser.parse_args()
    return args.link

def shorten_link(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    bitly_url = 'https://api-ssl.bitly.com/v4/shorten'
    payload = {'long_url': url}
    response = requests.post(bitly_url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['link']


def main():
    load_dotenv()
    url = get_link()
    api_token = os.getenv('API_BITLY_TOKEN')
    try:
        if is_bitlink(api_token, url):
            print(count_clicks(api_token, url))
        else:
            bitlink = shorten_link(api_token, url)
            print(bitlink)
    except requests.exceptions.HTTPError:
        print('Неправильная ссылка или токен')


if __name__ == '__main__':
    main()

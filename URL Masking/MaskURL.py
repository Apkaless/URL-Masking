import requests
import random
from bs4 import BeautifulSoup
from colorama import Fore, init
import re
import os
from time import sleep
from urllib.parse import urlparse

init(convert=True)
version = '1'
github_url = 'https://github.com/apkaless'
instagram = 'https://instagram.com/apkaless'
region = 'IRAQ'
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
white = Fore.WHITE
cyan = Fore.CYAN
lw = Fore.LIGHTWHITE_EX
black = Fore.BLACK
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
lc = Fore.LIGHTCYAN_EX
lib = Fore.LIGHTBLACK_EX
res = Fore.RESET



def validate_url(url):
    url_format = re.compile(r'https?://(www.)?[a-zA-Z0-9-]+\.+[a-zA-Z0-9]+')

    if not re.match(url_format, url):
        raise ValueError('\nInvalid URL format. Please provide a valid web URL.\n')


def validate_custom_domain(custom_domain):
    domain_format = re.compile(r'[a-zA-Z0-9-]+\.+[a-zA-Z0-9]+')

    if not re.match(domain_format, custom_domain):
        raise ValueError('\nInvalid custom domain. Please provide a valid domain name.\n')


def validate_keyword(keyword):
    length = 15

    if not isinstance(keyword, str):

        raise TypeError('\nInput must be a string.\n')

    elif ' ' in keyword:
        raise TypeError('\nKeyword Must Not Contain Spaces, Replace Spaces With "-".\n')

    elif len(keyword) > length:
        raise ValueError('\nInput string exceeds the maximum allowed length.\n')

    return True

def extract_url(html_content: str):

    soup = BeautifulSoup(html_content, 'lxml')

    div = soup.find('div', attrs={'id': 'app'})
    
    return div.a.text

def short_url(web_url):

    data = {
        'url':f'{web_url}',
        'shorturl':''
    }

    headers = {

        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'

    }

    res = requests.post('https://da.gd/', data=data, headers=headers)
    shorted_url = extract_url(res.text)

    return shorted_url

def mask_url(custom_domain, keyword, url):
    parsd_url = urlparse(short_url(url))

    masked_url = f'{parsd_url.scheme}://{custom_domain}-{keyword}@{parsd_url.netloc}{parsd_url.path}'

    return masked_url


def print_banner():
    os.system('cls')
    print(rf'''{cyan}



 █████╗ ██████╗ ██╗  ██╗ █████╗ ██╗     ███████╗███████╗███████╗
██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██║     ██╔════╝██╔════╝██╔════╝
███████║██████╔╝█████╔╝ ███████║██║     █████╗  ███████╗███████╗
██╔══██║██╔═══╝ ██╔═██╗ ██╔══██║██║     ██╔══╝  ╚════██║╚════██║
██║  ██║██║     ██║  ██╗██║  ██║███████╗███████╗███████║███████║
╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝
                                                                

{green}Version     : {lc}{version}
{green}Github      : {lc}{github_url}
{green}Instagram   : {lc}{instagram}
{green}Region      : {lc}{region}        

''')


def main():

    while True:
            print_banner()
            try:
                url = input(f'{cyan}\n↳ URL To Mask {cyan}→{white}  ')
                validate_url(url)
                break
            except Exception as e:
                print(red + str(e))
                sleep(2)
                continue
    while True:
        try:
            custom_domain = input(f'{cyan}\n↳ Custom Domain {green}(ex: google.com) {cyan}→{white}  ')
            validate_custom_domain(custom_domain)
            break
        except Exception as e:
            print(red + str(e))
            sleep(2)
            continue

    while True:

        try:

            keyword = input(f'{cyan}\n↳ Phish Keyword {green}(ex: login, free, anything) {cyan}→{white} ')
            validate_keyword(keyword)
            break
        except Exception as e:
            print(red + str(e))
            sleep(2)
            continue

    masked_url = mask_url(custom_domain, keyword, url)
    print(f'\n{green}[~] Original URL →{cyan} {url}')
    print(f'\n{green}[~] Masked URL →{cyan} {masked_url}')
    input('\n\n')

if __name__ == '__main__':
    main()
from urllib.parse import urlparse
from colorama import Fore, init
from time import sleep
import pyshorteners
import re
import os

init(convert=True)
version = '1'
github_url =  'https://github.com/apkaless'
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
pyshort = pyshorteners.Shortener()

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

def short_url(web_url):

    return pyshort.dagd.short(web_url)



def mask_url(custom_domain, keyword, url):
    
    parsd_url = urlparse(short_url(url))

    masked_url = f'{parsd_url.scheme}://{custom_domain}-{keyword}@{parsd_url.netloc}{parsd_url.path}'

    return masked_url
    


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
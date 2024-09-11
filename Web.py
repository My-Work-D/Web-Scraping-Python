

#import requered libs
#01-pip install requests
#import beautifulsoup
#pip install beautifulsoup4
from bs4 import BeautifulSoup

import requests

# define veriable string
url = 'https://example.com/'

# pring the scripte
response =requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(response.text)
    # set print data to array
    tags = soup.find_all(['h1','p'])
    for tag in tags:
        print(tag.text.strip())
    # print(soup.h1.string)
    # print(soup.p.string)
    # print(soup.a.string)
else:
    print("erro")

    # print(response.status_code)
    # print(response.text)




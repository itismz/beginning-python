# coding: utf-8

import requests
from bs4 import BeautifulSoup

def main(pagenum):
    URL = 'https://www.taptap.com/category/e12?page={}'.format(pagenum)
    
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')

    content = soup.find_all(class_="taptap-app-item")
    with open('page{}.txt'.format(pagenum), 'w') as f:
        for num in range(len(content)):
            content[num] = content[num].text.replace('\n', ' ').lstrip()
            f.write(content[num])
            f.write('\n')


if __name__ == '__main__':
    try:
        for pagenum in range(1, 16):
            print('正在采集第{}页...'.format(pagenum))
            main(pagenum)
            print('succeeded\n')
    except Exception as e:
        raise e
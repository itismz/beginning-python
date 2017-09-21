# coding: utf-8

URL_douban_YourName = 'https://movie.douban.com/subject/26683290/comments?start={}&limit=20&sort=new_score&status=P'

import requests
from bs4 import BeautifulSoup as bs
import jieba
import numpy
import re

def getCommentsById(pageNum):
    eachCommentList = []
    URL_douban_YourName2 = URL_douban_YourName.format((pageNum-1)*20+1)
    web = requests.get(URL_douban_YourName2).text
    soup = bs(web, 'html.parser')
    content = soup.find_all('div', class_='comment')
    for item in content:
        if item.find_all('p')[0].string:
            eachCommentList.append(item.find_all('p')[0].string)
    return eachCommentList


if __name__ == '__main__':
    
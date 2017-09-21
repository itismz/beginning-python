# coding: utf-8

URL_douban_YourName = 'https://movie.douban.com/subject/26683290/comments?start={}&limit=20&sort=new_score&status=P'

import requests
from bs4 import BeautifulSoup as bs
import jieba
import numpy
import re

def Login(username='18565079017', password='19930603'):
    REQUEST_URL = 'https://accounts.douban.com/login'
    HEADERS = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '129',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    data = {
            'ck': 'YGNO',
            'source': 'main',
            'redir': 'https://www.douban.com',
            'form_email': username,
            'form_password': password,
            'remember': 'on',
            'login': r'登录'
            }
    login = requests.Session()
    login.post(url=REQUEST_URL, data=data)
    # print(login)
    return login.cookies

def getCommentsById(pageNum):
    eachCommentList = []
    URL_douban_YourName2 = URL_douban_YourName.format((pageNum-1)*20+1)
    web = requests.get(URL_douban_YourName2, cookies=Login()).text
    soup = bs(web, 'html.parser')
    content = soup.find_all('div', class_='comment')
    for item in content:
        # if not item.find_all('p')[0].string is None:
        eachCommentList.append(item.find_all('p')[0].string.strip())
    return eachCommentList


if __name__ == '__main__':
    login = Login()
    contentList = []
    for page in range(1, 11):
    #     print(page)
        comment = getCommentsById(page) # 前10页
        # comment = getCommentsById(11) # 前10页
        contentList.append(comment)
        for item in comment:
            print('{}: {}\n'.format(comment.index(item)+1, item))
    print(contentList)
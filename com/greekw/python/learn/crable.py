# -*- conding:utf-8 -*-
# !/usr/bin/python3
''''
# 爬取网站：

工具：requests,urllib2
lxml：
# 使用
x=get(url,heads)
x.text
x.content

xpath使用
// 定位父节点
/text():
/@attr():
帅选节点
/div(id)

# 新闻网爬虫：https://www.chinanews.com/scroll-news/news1.html

# 分页栏爬：

# 豆瓣：https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4

# mysql-connector/mysql-db

'''

import requests
from lxml import etree
res = requests.get()
res.content.decode("gbk")
bookhtml = '''
'''

doc = etree.fromstring(bookhtml)

for eachbook in doc.xpath('//dl/dd'):
    bookname = eachbook.xpath('a/text()')[0]
    bookurl = eachbook.xpath('a/@href')[0]
    print(bookurl,bookname)


if __name__=='__main__':
    pass


# 部署
'''
nginx+uwsgi
nginx+gunicorn
nginx+tornado
apache+nginx

'''



''''
深度学习：

'''
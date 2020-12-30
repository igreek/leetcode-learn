# -*- conding:utf-8 -*-
# !/usr/bin/python3
'''
创建连接
创建游标
执行
关闭连接
'''
#from mysql import connector
from faker import Factory

# conn = connector.connect('host=',port=3306,username='root',password='root',charset='')
# conn.autocommit =True
# cursor = conn.cursor()
# sql = ''
# cursor.execute(sql)
# conn.close()


factory = Factory.create()
res =[(factory.name(),factory.address(),factory.email()) for i in range(10)]
print(res)

# mysqldb使用,相比mysql-connecot 更安全
'''

'''

# sqlalchemy使用:https://www.cnblogs.com/wj-1314/p/10627828.html
'''
-表映射到类
-行映射到对象
-列映射到属性
# 开发流程
- 创建连接
- 创建映射
- 初始化映射实例
- 创建会话
- 持久化对象
    

'''
#import MySQLdb

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
create_engine('',echo=True)
declarative_base()

# python 操作mongodb

'''
mongodbvue
'''

# python 多线程和多进程
'''
thread模块
threading模块
多进程模块
multiprocessing.Process
# 多进程通信
multiprocessing.Queue

'''
import threading
from django import *

class A(threading.Thread):
    def run(self):
        while True:
            print('thread')
            time.sleep(2)

if __name__=='__main__':
    mt = [A() for i in range(4)]
    for t in mt:
        t.start()

import time
class B(threading.Thread):
    def run(self):
        while True:
            print('thread')
            time.sleep(2)

if __name__=='__main__':
    mt = [B() for i in range(4)]
    for t in mt:
        t.start()
    for t in mt:
        t.join()

# 生产者和消费者   multiprocessing.Queue
try:
    pass
except:
    pass
# 企业级scrapy使用 。需要lxml,zope.interface,Twisted,pywin32,pyOpenSSL
'''
scrapy使用方式
- 交互式
scrapy shell ''
- 创建项目
scrapy startproject ''
- 创建Spider
scrapy  genspider ''
- 运行爬虫
scrapy crawl spidername
'''
from scrapy import cmdline
cmdline.execute('')

# 豆瓣实战


# diango实战
'''
python web框架
diango
web.py,tornado
flask

orm框架
模板引擎
URL路由
MVC

'''


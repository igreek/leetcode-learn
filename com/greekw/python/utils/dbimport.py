#!/usr/bin/python
#coding=utf-8
# -*- coding=utf-8 -*-
import json
import pymysql
# 读取review数据，并写入数据库
# 导入数据库成功，总共4736897条记录
def prem(db):
  cursor = db.cursor()
  cursor.execute("SELECT VERSION()")
  data = cursor.fetchone()
  print("Database version : %s " % data) # 结果表明已经连接成功
  cursor.execute("DROP TABLE IF EXISTS review") # 习惯性
  sql = """CREATE TABLE review (
       code VARCHAR(100),
       city VARCHAR(100),
       province VARCHAR(200),
       Pcode VARCHAR(10000) NOT NULL
       )"""
  cursor.execute(sql) # 根据需要创建一个表格

def reviewdata_insert(db):
  with open('E:/db.json', encoding='utf-8') as f:
    i = 0
    while True:
      i += 1
      print(u'正在载入第%s行......' % i)
      try:
        lines = f.read() #
        line_list = eval(lines)# 使用逐行读取的方法
        for review_text in line_list:
            # review_text = json.loads(lines) # 解析每一行数据
            result = []
            result.append((review_text['code'], review_text['city'],review_text['province'],review_text['Pcode']))
            print(result,":",review_text)
            inesrt_re = "insert into review(code, city, province,Pcode) values (%s, %s, %s, %s)"
            cursor = db.cursor()
            cursor.executemany(inesrt_re, result)
            db.commit()
            break;
      except Exception as e:
        db.rollback()
        print(str(e))
        break
if __name__ == "__main__": # 起到一个初始化或者调用函数的作用
  db = pymysql.connect("local", "crs", "crs", "crs", charset='utf8mb4')
  cursor = db.cursor()
  prem(db)
  reviewdata_insert(db)
  cursor.close()
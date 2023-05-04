#!/usr/bin/python
#coding=utf-8
import json
# import http.client
#import urllib.parse
import hashlib
import time
# data=json.dumps({
#   "bizType":"B005",
#   "serviceName":"TianXing",
#   "methodName":"getIdCardVerifyData",
#   "params":{
#     "idCard":"370103197607017176",
#     "name":"骆凉倩"
#   }
# })
# print(data)

def post(url, data):
    # md5sign= hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    # timestamp=time.time();
    # print(md5sign+","+timestamp)
    # headers = {"Content-type": "application/json","Content-md5":md5sign,"Content-timestamp":timestamp}
    # conn=http.client.HTTPConnection("10.0.4.149","8082")
    # conn.request("/crs/applyCredit",data,headers)
    # response = conn.getresponse()
    # print(response.status, response.reason)
    # data = response.read().decode('utf-8')
    # print(data)
    # conn.close()
    return data

def main():
    posturl = "http://www.xiami.com/member/login"
    data = {'email':'myemail', 'password':'mypass', 'autologin':'1', 'submit':'登 录', 'type':''}
    print( post(posturl, data))

if __name__ == '__main__':
    main()
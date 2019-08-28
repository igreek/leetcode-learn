__author__ = 'greekw'
# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
  python 寻找幸运数
  Python特殊语法：filter、map、reduce、lambda
  http://www.cnblogs.com/longdouhzt/archive/2012/05/19/2508844.html
'''
class Solution(object):
    def isHappy(self,n):
        lookup,n=set(),str(n)
        while True:
            n=str(sum(map(lambda x:x*x,map(int,n))))
            if '1'==n:return True
            if n in lookup:return False
            lookup.add(n)

if __name__=="__main__":
    s= Solution()
    print(s.isHappy(19))
    print(range(2,9))
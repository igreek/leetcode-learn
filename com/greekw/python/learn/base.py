# -*- conding:utf-8 -*-
# !/usr/bin/python3

import keyword;
# 单行注释，输出python的保留字
print(keyword.kwlist);
'''
1.第一个python程序，base.py
2.行的缩进
3.多行语句
4.数字类型（Number）
5.字符串


'''

# 行缩进
if True:
    print ('true')
else:
    print ('false')


#多行语句

total = 'item_one' + \
        'item_one' + \
        'item_one'
total2=['item_one','item_two','item_three']


# 字符串
word= '字符串'
sen= "字符串2"
pagram='''
kyi
jfiegua
'''

line=r'this is a line with \n'
print (line)

print ('hello'+'word')

print (line*2)


# input输入

input("\n\n按下 enter 键后退出。")

# 同一行显示多条

#import sys;x='hello';sys.stdout.print(x+'\n')

# 导入sys模块
import  sys
print('================Python import mode==========================')
print('命令行参数')
for x in sys.argv:
    print(x)
print('\n python的路径：',sys.path)

# 导入sys模块的中的arg，path成员

from sys import argv,path
print('+++++++++++pyhton from import++++++++++++++')
print('\n python的路径：',path)

# 参考教材：
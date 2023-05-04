__author__ = 'greek'
# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
 leetcode 读写文件
'''

class ReadAndWrite:
    def readAndWrite(self,path1,path2):
        with open(path1,'rt') as f:
            for line in f:
                print(line)
                with open(path2,'rt') as f2:
                    for table in f2:
                        #print(table)
                        vaildSql=line.replace('$TABLE',table)
                        print(vaildSql)


if __name__=="__main__":

    rw=ReadAndWrite();
    path1='d:/source.txt';
    path2='d:/table.txt';
    rw.readAndWrite(path1,path2)

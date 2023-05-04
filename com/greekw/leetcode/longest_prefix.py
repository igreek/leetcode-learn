__author__ = 'greek'
# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
  公共的最长前缀
'''
class Solution():
    def longestCommonPrefix(self,strs):
        if not strs:
            return ""
        res=''
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if(i>=len(strs[j]) or strs[j][i] != strs[0][i]):
                    return res
            res += strs[0][i]
        return res

if __name__ == "__main__":
    s=Solution();
    print(s.longestCommonPrefix(["hello", "heaven", "heavy"]))
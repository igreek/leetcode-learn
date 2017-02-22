__author__ = 'greek'
# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
  基础运算器
'''
class Solution(object):
    def calculate(self,s):
        stackOp=[]
        stackNum=[]
        res=''
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                res+=s[i]
                if i==0 or not s[i-1].isdigit():
                    stackNum.append(int(res[::-1]))
                    res=''
            elif s[i]==')'or s[i] == '*' or s[i] == '/':
                stackOp.append(s[i])
            elif s[i]=='+' or s[i]=='-':
                while stackOp and (stackOp[-1]=='*' or stackOp[-1]=='/'):
                    self.compute(stackNum, stackOp)
                stackOp.append(s[i])
            elif s[i]==')':
                while stackOp[-1]!=')':
                    self.compute(stackNum, stackOp)
                stackOp.pop()
        while stackOp:
            self.compute(stackNum, stackOp)
        return  stackNum[-1]

    def compute(self, stackNum, stackOp):
        left, right = stackNum.pop(), stackNum.pop()
        op = stackOp.pop()
        if op == '+':
            stackNum.append(left + right)
        elif op == '-':
            stackNum.append(left - right)
        elif op == '*':
            stackNum.append(left * right)
        elif op == '/':
            stackNum.append(left / right)

if __name__ == "__main__":
    s=Solution()
    param="3+2*2+2/4"
    print(len(param))
    print(reversed(range(len(param))))
    print(s.calculate(param))

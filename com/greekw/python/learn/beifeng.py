# -*- conding:utf-8 -*-
# !/usr/bin/python3
import time
# 列表
x = range(1,10)
y = range(11,20)
z = range(1,20)
print(z[-1:-10:-1])
# 列表常用操作:append,enumerate,reverse,sorted,len,
for(index,value) in enumerate(z):
    print(index,value)

# 列表解析，[expr,for iter,in iterable]

k = range(-10,10)
result=[]
for i in k:
    if i<10:
        result.append(i**2)
    else:
        result.append(i)
print(result)
result2 = [i**2 for i in k if i<0]
print(result2)

#filter ,map
#filter(fun,list):根据fun(x)的结果为T,F对列表元素进行过滤操作
#map(fun,list):用于fun(x)作用的每个元素得到一个新的结果列表

def a(x):
    if x>0:
        return True
    else:
        return False
x = range(-10,10)
print(filter(a,x))

# 生成器表达式
#(expr for iter in iterable[if condition])
#生成器生成的不是结果，是对象。不能用索引和append
f = open('d:/nginx-1.conf')
start = time.clock()
lines = [t.split(',') for t in f]
end = time.clock()
print(end-start)


start1 = time.clock()
lines2 = (t.split(',') for t in f)
end1 = time.clock()
print(end1-start1)
print(type(lines),type(lines2))


# 元组,元组内容器的元素可修改，单独的不能修改
x = (1,'hello',True)
print(x[1])

# 字符串 支持join,加法和乘法操作，不能修改
a = 'hello world'
b = 'learn python'
print(a+b)
print(a*2)
#print(' '.join(x))
#字符串 中文处理
#x = input(u"请输入名字：".encode('gbk'))
#print(x)

#s = input("请输入内容：")
#f = open('d:/data/1.txt','w')
#f.write(s)
#f.close()

# 字典
# 无序，k-v结构，key的值不变，value可变。{'key':'value'}
# items()/keys()/values()/get()/setDefault()/update()
x={'name':'张三','age':20}
y=dict(name='张三',age=20)
print(x,y)
print(x['name'])
print('name1' in x)
print(x.get('namw1','not exist'))
for i in x:
    print(i,x[i])

for k,v in x.items():
    print(k,'=',v)



# 集合
# 无序，元素不可变，不支持切片，索引，元素不重复
# set 可变集合 # frozenset:不可变集合
# 集合运算：|，& ^ - |=
# 集合操作：add()/discard()/remove()/update()/difference_update()
x = set(range(1,10))
y = set(range(7,20))
print(x|y)
print(x&y)
print(x-y)
print(x^y)
z=list(x)
print(z)

# 函数式编程
# 函数参数没有类型，不支持重载，多个同名函数，后一个会覆盖前一个def func(x,y,z=v,*args,**kars)
# 函数任意数量参数 *和**
# 一个函数可以多个返回值，可以多个变量接收，可以打包为一个tuple
# 函数作用域;LEGB原则
# 函数也是对象，可以给对象增加属性
def funA(x,y,z,*args,**kwargs):
    print(x,y,z,args,kwargs)

funA(1,2,3,4,5,6,a='hello',b=True)
k=[7,8,9]
funA(*k)

x=range(1,5)
print('x=',id(x))
def funB(a):
    print('a=',id(a))
    a[1] =0
#print(funB(x))
funB(list(x))
print(x)

x=10
def fun():
    '''
    @auth:
    :return:
    '''
    # x=12
    # print(x)
    global x
    x+=10
fun()
print(x)
print(fun.__doc__)

# 函数嵌套和闭包
def funC(x):
    y=100
    def innerFun(z):
        return x*y+z
    return innerFun
a10=funC(10)
print(a10(29))

# 装饰器
# 不带参数的装饰器，带参数的装饰器
# @decorator def f():pass
# 区别：

def log(func):
    def wrapper(*args,**kwargs):
        print('-'*40)
        res=func(*args,**kwargs)
        print('calling:',func.__name__,args,kwargs)
        return res
    return wrapper

@log
def f(x,y):
    return x+y

print(f(10,20))


# 迭代器
# 实现__iter__,__next__
# itertools:排列/组合、笛卡尔积
import itertools
x =range(1,10)
citer=itertools.combinations(x,3)
for i in  citer:
    print(i)
y=['a','b','c']
z=range(1,4)
ziter=itertools.product(y,z)
for k in ziter:
    print(k)

# 生成器
# 生成器生成迭代器，生成器函数yield
def incr(n=1):
    while True:
        yield n
        n+=1
a = incr()
print(a.__next__())

#
import os
def getFileList(rootDir):
    for path,dirlist,filelist in os.walk(rootDir):
        for filename in filelist:
            if filename.endswith('csv'):
                yield os.path.join(path,filename)

def openFiles(filelist):
    for filename in filelist:
        yield (filename,open(filename))
def grep(filelist,pattern):
    for (filename,fh) in filelist:
        for line in fh:
            if pattern in line:
                yield (line,value)

filelist=getFileList('')
files=openFiles(filelist)
lines=grep(files,'2020-12-29')

for (filename,line) in lines:
    print('-'*60)


# 经典类和新式类
# 封装，继承、多态

# 新式类：__new__ super
# 区分方式：type(classname)

class A():
    pass
class B(object):
    pass

# 类的属性和方法
# 类属性和实例属性
# 公有属性和私有属性
class C(object):
    nation='china'
    def __init__(self,name):
        self.name=name
    def msg(self):
        print(self.name)


c = C('zhangsan')
c.msg()
print(C.nation)
print(c.__dict__)


class Person(object):
    nation='china'
    def __init__(self,id,name):
        self.__id=id
        self.__name=name
        self.__age=None
    def getID(self):
        return self.__id
    def setID(self,id):
        self.__id=id
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    @name.deleter
    def name(self):
        del self.__name

p = Person(1,'lisi')
print(p.getID())
print(p.name)

# 描述符
# 代码重用，

# 方法
# 实例方法：
# 类方法：@classmethod
# 静态方法 @staticmethod
# 特殊方法 python内置方法

class Chinese(object):
    def __init__(self,id,name):
        self.__name=name
        self.__id=id

    @staticmethod
    def getID(id,name):
        pass
    @classmethod
    def getPopertyBysibling(cls,sibling):
        print(sibling)
        return cls(20,'wangwu')
    def __str__(self):
        return 'ID={0},NAME={1}'.format(self.__id,self.__name)

class BJ(Chinese):
    pass

c = Chinese.getID(10,'lisisi')
c2 = Chinese.getPopertyBysibling('MAMA')
print(c,c2)

bj = BJ.getPopertyBysibling('北京')


# 特殊方法：
# 构造函数，析构函数： __new__ __init__ __del__
# 四则运算 __add__ __sub__ __div__
# 比较运算 __lt__ __gt__ __cmp__
# __str__ __contains__ __bool__


# 继承
# 目的：代码复用，多态
# 多重继承， 经典类：深度优先； 新式类：广度优先

class A(object):
    def __init__(self):
        print('parent A')
class B(A):
    def __init__(self):
        A.__init__(self)
        super(B,self).__init__()
        print('sub B')
class C(A):
    def __init__(self):
        A.__init__(self)
        super(C,self).__init__()
        print('sub C')
class D(B,C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print('sub D')

d = D()

import inspect
print(inspect.getmro(D))

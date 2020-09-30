# -*- coding: utf-8 -*-
'''hello_world'''
print("hello")
print("-"*20)
'''
标准数据类型->基本数据类型->数字->integer
                               ->float
                               ->bool
                               ->complex
                        ->字符串->string
            ->复合数据类型->list
                         ->tuple
                         ->set
                         ->dictionary
'''

a=999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 #整数没有取值范围限制
b=True #或者=False
f=1.23 #也可以写成科学计数法1.2323e-2，浮点数精度未知
c=1.021+0.12356j #实部和虚部都是float类型
print(a,b,f,c)

a=int(5.3201016)
f=float("123.032145265e-2") #Convert a string or number to a floating point number, if possible.
c=complex(1.2,10.22) #Create a complex number from a real part and an optional imaginary part. This is equivalent to (real + imag*1j) where imag defaults to 0.
print(a,f,c)
print("-"*20)

#算数运算符
a=0xff #16进制
a=0o77 #8进制
print(1+1) #加法
print(2-1) #减法
print(2*2) #乘法
print(1/3) #除法，得到一个浮点数
print(1//3) #除法，舍去小数部分，得到一个整数
print(17%3) #取余
print(2**(1+2j)) #乘方
#混合计算时会把整数自动转换为浮点数
print("-"*20)

#比较运算符,应该只有整型，浮点型可以参与比较运算
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print("-"*20)

#赋值运算符
a=126
print(a)
a+=2;print(a) #a=a+2
# a=+2 #=+不知道有什么功能，类似的还有=-,=*,=/等
a-=2;print(a)
a*=2;print(a)
a/=3;print(a)
a%2;print(a)
a//2;print(a)
a**=2;print(a)
print("-"*20)

#位运算符
a=0b0011_1100
b=0b0000_1101
print(bin(a&b)) #与
print(bin(a|b)) #或
print(bin(~a))  #非
print(bin(a^b)) #异或
print(bin(a<<2))#左移2位
print(bin(a>>2))#右移2位
print("-"*20)

#逻辑运算符
print(True and False)
print(True or False)
print(not True)
#除了布尔型可以参与运算整型，浮点型，复数也可以参与运算
print(13 and -23) #返回绝对值大的那个
print(-1 or -232)  #返回绝对值小的那个
print(not 0+0j)   #是零返回true,不是返回false
print("-"*20)

#其它运算符
list0 = [1,2,3]
print(2 in list0)
print(4 not in list0)
list1=list0
print(list0 is list1)
list1=[1,2,3]
print(list0 is not list1)
print(list0==list1)

#字符串运算
str="hello world"
print(str+"!")                  #字符串拼接
print(str*10) #
print(str[1],str[-1]) #字符串索引
print(str[0:5],str[6:]) #引用字符串中的一段
print("hello" in str)
print("penghao" not in str)
print('''
#include <stdio.h>
      
int main(){
    printf("hello");
    return 0;
}
      ''') #多行字符串
print("-"*20)

#列表
list1=[1,2,3,"hello"]
print(list1)
list1[-1]=4;print(list1) #修改列表中的数据
del list1[-1];print(list1) #删除列表中最后一个元素
list1+=[4,5,6];print(list1) #把两个列表拼到一起
print([list1,["he","ll","o"]]) #嵌套列表

#元组与列表类似，不同之处在于元组的元素不能修改
tup0=(1,2,3) #小括号生命元组
print(tup0)
print("-"*20)

#字典
'''
    字典可以存储任意类型对象。字典的每个键值对用冒号 : 分割，每个对之间用逗号
分割，整个字典包括在花括号 {} 中。
    键必须是唯一的，但值则不必。
    字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，
但键必须是不可变的，字符串，数字，和元组都可以充当键
    d = {key1 : value1, key2 : value2 }
'''
dict0 = {'股票代码': 'bili', '公司名': "BILIBILI", '市值': 14.13e9}
print(dict0)
print(dict0["股票代码"]) #引用字典中的元素
dict0["市值"]=0;print(dict0); #修改字典中的元素
print("-"*20)

#集合
'''
    集合（set）是一个无序的不重复元素序列。可以使用大括号 { } 或者 set() 函数
创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个
空字典。
    parame = {value01,value02,...}或者set(value)。
'''
set0={1,2,3,4,5,6,7,8,9,10}
set1={1,3,5,7,9}
set2={2,4,6,8,10}
set3={2,3,5,7}
#集合之间有几种运算
print(set1 & set3) #交
print(set1 | set2) #并
print(set0 - set1) #差集运算
print(set1 ^ set3) #不同时包含在两集合中的元素,等价于(set1 | set3) - (set1 & set3)
print("-"*20)

#分支语句
#if语句
if True:
    print("It is True")
#if-else语句
if True:
    print("It is True")
else:
    print("It is False")
#if-elseif-else语句
if a==1:
    print(1)
elif a==2:
    print(2)
elif a==3:
    print(3)
else:
    print("啥也不是")
print("-"*20)

#循环语句
'''
while循环，句型是：
while 条件:
    语句...
'''
#例子
a=0
while a<10:
    print(a)
    a+=1
print("-"*20)
'''
python里还有一种while-else循环,句型是：
while 条件:
    语句...
else:
    语句...
'''

'''
for-else循环，不用else时不写else语句就行了，句型是：
for 变量 in 序列：
    语句...
else:
    语句...
'''
#例子
for i in range(10):
    print(i)
print("-"*20)
for i in range(0,10,2):#range(起始数，最大数，步长)
    print(i)
    
#函数
def fun0(): #定义一个空函数，什么也不做
    pass

def fun1(arg): #传参和返回值
    return arg

def fun2(a=0): #可选参数，指定参数的默认值
    return a

def fun3(arg0,*args): #变长参数，变长的部分是一个列表
    print(arg0,args)
    
def fun4(arg0,**args): #变长的部分是一个字典
    print(arg0,args)

def fun5(a,*,b): #暂时不知道这样的传参方法有什么用处
    return a+b

fun0()
fun1("hello")
fun2()
fun3(1,2,3,4,5)
# fun4("股票代码和它的名称","BILI"="哔哩哔哩"}) #fun4不知道怎么调用
print(fun5(1,b=1))
#fun5(1,1) #这样调会出错

#lambda的句型：a = lambda arg0,arg1,...,argn : do somthing
from math import sin
sin_wave = lambda A,ω,t,φ : A*sin(ω*t+φ)
print(sin_wave(10,1,3.1416/2,0))
print("-"*20)

#类
class cla0: #最简单的类——一个空类
    pass

class  cla1:
    a=0 #类属性
    def fun(self): #自定义的类方法
        pass

class cla2:
    def __init__(self): #构造方法
        pass
    #不能定义多个构造方法
    # def __init__(self,arg0):
    #     pass
    #类被释放的时候会执行
    def __del__(self):
        pass
    
#继承类时的句型：class 类名(父类名):
#python中可以继承多个类，句型是class 类名(父类1名，...,父类n名):
class cla3(int):   
    def int(self,x): #重写了父类的int(x)方法
        return 0
        
class cla4:
    __sec_attribute = 0 #定义一个私有变量
    def __sec_fun(self): #定义一个私有方法
        pass

'''
类的一些专有函数：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方
用法示例：
'''
class cla5:
    def __len__(self):
        return 0
    def __add__(self,another):
        return 2
print(len(cla5()),cla5()+cla5()) #将会输出0和2

import is_prime
print(is_prime.is_prime(1203))
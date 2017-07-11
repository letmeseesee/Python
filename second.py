#Created by yhwang on 2017/7/1.
import math

def test(x):
    '''First function'''
    return math.sqrt(x)

def args_test(a,b,c,d,e):
    pass

def text1(x,*args,**kwargs):
    pass
#关键参数不能写在位置参数前面,同时要满足一一对应的关系
args_test(1,2,3,d=3,e=4)
#还是要满足一一对应的关系位置不能出错


#复杂的数据类型是可以在函数内部修改全局变量的,只有字符串和整数不能修改
name = 'yhwang'
name1 = [1,2]
def change_name():
    print(name)
    name1[0] = 3
    #name = 'yhwang1'

change_name()

print(name,name1)

#装饰器--->本质是一个函数,用来装饰其他函数,为其他函数添加额外功能
#装饰器原则:1.不能修改被装饰的函数的源代码
#         2.不能修改被装饰的函数的调用方式
#实现装饰器的知识储备
#         1.函数是变量 2.高阶函数 3.函数嵌套
#           2+3=>装饰器
import time

#一个装饰器
def timer(func):
    def wapper(*args,**kwargs):
        func()
        print(123)
    return wapper

@timer
def test_d():
    time.sleep(3)

#怎么解决参数的问题???
def mydeco(func):
    def deco(*args,**kwargs):#在这里加上参数-->同时解决了多个函数参数个数不同的问题
        print("In deco")
        res = func(*args,**kwargs)#如果function有结果的话
        return res
    return deco()

#装饰器带参数的情况---->封装最深的情况
def deepdeco(type):
    print(type)
    def mydeco(func):
        def deco(*args, **kwargs):  # 在这里加上参数-->同时解决了多个函数参数个数不同的问题
            print("In deco")
            res = func(*args, **kwargs)  # 如果function有结果的话
            return res

        return deco()
    return mydeco
#用户限制验证装饰器功能
def auth(func):
    def deco(*args,**kwargs):
        #登录验证
        #可以加上从终端输入
        func(*args,**kwargs)
@deepdeco(type=1)
def test_deep():
    print(123)
test_d()


#生成器就是一边循环一边计算的意思
#-----------------生成式----------------
print("-----------------生成式----------------")
a = [x for x in range(10) if x<5]
b = (x for x in range(100000000))#生成器只有在调用时才会生成相应的数据
print(b)
print(b.__next__)
print(b.__next__())

#写一个生成器---->带yield就行
def fib(max):
    a=0
    b=1
    n=0
    while n<max:
        a,b = b,a+b
        n = n+1
        yield b

for i in fib(10):
    print(i)

f = fib(10)
print(f.__next__())
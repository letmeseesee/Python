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
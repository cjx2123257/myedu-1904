from day001 import base_type
# 变量赋值
def cd1():
    a = 12
    b = 13
    c = a + b
    print (c)
# 查询类型
def cd2():
    a = 12
    b = '13'
    print (type(a))
    print (type(b))
# 更改类型
def cd3():
    a = 12
    print (type(a))
    print (type(str(a)))
    a = str(a)
    print (type(a))
def  cd4():
    a = 12
    b = '13'
    c = a + int(b)
    c1= str(a)+b
    print (c)
    print (c1)
    print ('%s%s'%(a,b))
    d = '休息休息'
    e = '反反复复'
    f = d + e
    print (f)
def cd5(num1,num2):
    print(num1)
    print(num2)
    print(num1+num2)
    return num1+num2

if __name__=='__main__':
    cd1()
    cd2()
    cd3()
    cd4()
    cd51 = cd5(20, 30)
    cd52 = cd4()
    print(cd51)
    print(cd52)
from day001 import base_type
base_type.cjx_int()
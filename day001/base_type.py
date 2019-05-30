def cjx_int():
    aint = 5
    print(type(aint))
def cjx2_str():
    c = '6'
    print(type(c))
if __name__ == '__main__':
    print('Hello,World')
    aint = 5
    print(type(aint))
    c = '6'
    print(type(c))

height = 1.75
weight = 70
bmi = (weight/(height*2))
if bmi < 18:
    print ('过轻')
elif bmi < 25:
    print ('正常')
elif bmi < 28:
    print ('过重')
elif bmi < 32:
    print ('肥胖')
else:
    print ('严重肥胖')

def test1():
    print ('test1')
def test2():
    print ('test2')
def test3():
    print ('test3')
if __name__ == '__main__':
    test3()
    test1()
    test2()

def zhuanhuan():
    b = 123
    print (type(b))
    b = str(b)
    print (type(b))
def zhuanhuan2():
    b= '123'
    print (type(b))
    b = int(b)
    print (type(b))
def lianjie():
    a = 123
    b = '哈哈哈'
    c = '嘻嘻嘻'
    print(b + c)
    print(str(a) + b + c)
    print('%s%s' % (a, b))
    print ('a=%s b=%s'%(a,b))
def add(num1,num2):
    print (num1)
    print (num2)
    print (num1+num2)
    return num1+num2
if __name__=='__main__':
    print (2+3)
    float = 1.2
    print (type(float))
    zhuanhuan()
    zhuanhuan2()
    lianjie()
    a = lianjie()
    b = add(5,10)
    print ('--------------')
    print (a)
    print (type(b))
    print (b)





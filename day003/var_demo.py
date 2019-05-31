#声明一个全局变量
agyrj= '果芽'

def v1():
    #可以使用全局变量
    print(agyrj)
    #创建一个局部变量
    b  = '软件'

def v3():
    global agyrj
    agyrj = '世界'
    print(agyrj)

if __name__ == '__main__':
    v1()

    v3()
import os
if __name__ == '__main__':
    pwd = os.getcwd()            #获取当前目录
    print (pwd)
    a = os.path.abspath('..')    # 获取上一级目录
    print (a)
    b = os.path.abspath('..\..')  # 获取上上级目录
    print (b)


def assert_int():
    try:
        assert 3 > 2
    except:
        print ('断言失败了')
    try:
        assert 2 > 3
    except:
        print ('断言失败了')
def assert_str():
    a = '果芽软件'
    b = '果芽软件学院学生张三李四王五'
    try:
        assert a in b
        assert '果芽'== '果芽'
    except:
        print ('错误')
    try :
        assert a not in b
    except:
        print ('错误')

if __name__ == '__main__':
    assert_int()
    assert_str()

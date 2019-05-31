def if_demo1():
    a =  55 > 66
    if a :
        print ('a 是 True')
    else :
        print ('a 是 Flous')
def elif_demo2():
    a = 6
    # = 是赋值  == 是判断是否相等
    if a == 1 :
        print ('a是1')
    elif a == 2 :
        print ('a是2')
    elif a == 3 :
        print ('a是3')
    elif a == 4 :
        print ('a是4')
    else :
        print ('a不是1,2,3,4')
    b = 66
def jisuan():
    a = 10
    b = 3
    print (a+b)
    print (a-b)
    print (a/b)
    print (a*b)
    print (a%b)
def duibi():
    a = 1
    b = 2
    c = 3
    # 比较符 完成后 会返回一个bool  只有 True 和 Fluse , < >  <= >= = !=
    print (a > b)
    print (a < b)
    print (a = c)
    print (a != c)

def deng(a):
    a = 10
    a += 1  # 自增
    print(a)
    a -= 1  # 自减
    print(a)
def for_demo3():
    for i in range(5):
        print ('果芽软件')
        print (i)
def for_demo4():
    for i in range (5,19,2):
         print (i)

    for b in range (17,8,-2):
        print (b)
def for_demo5():
    blist= [1,2,3,4,5,6,7]
    for i in blist:
        print (i)

    for i in range(len(blist)):
        print (blist[i])
def forfor_demo6():
    for i in range(5):
        print ('Hello,world')
        for j in range(2):
            print('你好,世界',end='')
        print('\n')
        # end = '**' 让print以 ** 结尾换行, \n 换行符    print 默认以换行符结尾
def break_continue():
    for i in range (5):
        print (i)
        if i == 3 :
            break
    for j in range (5):
        if j == 3 :
            continue
        print (j)




if __name__ == '__main__':

    # if_demo1()
    # elif_demo2()n
    # for_demo3()
    # for_demo4()
    # for_demo5()
    # forfor_demo6()
    break_continue()


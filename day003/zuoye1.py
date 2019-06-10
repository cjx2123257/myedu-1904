# 求 1到50之间的奇数和
# 打印九九乘法表
# 求两个数之间的偶数和
def zy1():
    sum = 0
    for x in range(1,51):
        if x % 2 == 1:
            sum = sum + x
    print(sum)
def zy2():
    for m in range(1,10):
        for n in range(1,10):
            if m>=n:
              print ('%sx%s=%s'%(m,n,m*n),end=' ')
        print('')
def zy2_1():
    for m in range(1,10):
        for n in range(1,m+1):
            print ('%sx%s=%s'%(m,n,m*n),end=' ')
        print('')
def zy3():
    x = 4
    y = 7
    sum = 0
    if x <= y :
        for i in range(x,y+1):
            if i%2 == 0:
                sum = sum + i
    else:
        for i in range(y,x+1):
            if i%2 == 0:
                sum = sum + i
    print (sum)

def zy4():
    for i in range(1,1001):
        if i%4==1 and i%5==4 and i%6==3 and i%7==5 and i%8==1 and i%9==0:
            print (i)
def zy5():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s x %s = %s'%(j,i,j*i),end='   ')
        print(' ')


if __name__ == '__main__':
    zy1()
    zy2()
    zy2_1()
    zy3()
    zy4()
    zy5()

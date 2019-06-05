#冒泡排序
# 外循环 len - 1       因为 两两比较,比如有10个数 我需要比较 9次
# 内循环 len - i - 1   因为 两两比较,比如有10个数,我刚开始需要比较 9次,之后需要比较8次 每一轮少一次,因为每轮都有一个数都会放到后面
def paixu():
    alist = [1,6,8,9,4,2,3,5,7]
    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            if alist[j]<=alist[j+1]:
                continue
            px = alist[j]
            alist[j]=alist[j+1]
            alist[j+1]=px
    print(alist)
def paixun2():
    alist2= [11,23,10,96,89,14,25,81,94,17,92,88,74]
    for i in range(len(alist2)-1):
        for j in range(len(alist2)-i-1):
            if alist2[j] > alist2[j+1]:
                px2=alist2[j]
                alist2[j]=alist2[j+1]
                alist2[j+1]=px2
    print(alist2)


if __name__ == '__main__':
    paixu()
    paixun2()



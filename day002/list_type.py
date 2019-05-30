
alist = ['果芽软件','2019.05.30','11:41要吃饭了','好饿啊',2,3,5,9]
def  list1():
    # 取第一个
    print(alist[0])
    # 取1到2个
    print (alist[1:3])
    # 取倒数第三个
    print (alist[-3])
    # 从第四个取到最后
    print (alist[3:])
    # 前面不填从第一个取值,取到第四个
    print (alist[:3])
    # 倒着取值
    print (alist[::-1])
    # 取倒数三个数值
    print (alist[:4:-1])
blist = ['果芽软件','2019.05.30','11:41要吃饭了','好饿啊',2,3,5,9]
def  list2pop():
    #调用删除方法,不填参数默认删除最后一个
    blist.pop()
    print (blist)
    #删除第五个
    blist.pop(4)
    print (blist)
def  list3add():
    clist = [1,2,3,4,]
    # 默认增加在末尾
    clist.append(5)
    clist.append('5')
    print (clist)
    #合并两个list中的元素
    dlist = [6,7,8]
    #append 把第二个当做一个元素添加
    clist.append(dlist)
    print (dlist)
    # extend 把第二个中每一个元素都独立添加
    clist.extend(dlist)
    print (clist)
def list4update():
    #更改第四个数值
    elist = [1,2,3,4,5,6]
    elist[3] = '崔'
    print (elist)
    #更改第三个数值为200
    elist[2] = 200
    print (elist)
def list5order_by():
    flist = [1,2,13,6,9,7]
    #从小到大排列
    flist.sort()
    print (flist)
    #从大到小排列
    flist.sort(reverse=True)
    print (flist)
def list6distinct():
    glist = [1,1,22,22,3,6,5,5,5]
    #去重
    glist = list(set(glist))
    print (glist)
    #获取索引长度
    print (len(glist))

#题目题: 新建一个list变量,里面有五个元素,访问索引2,切片访问索引1到4,删除索引3,添加两个元素,第0位元素改成字符5,获取索引长度
def zuoye530():
    listzy530 = [3,'果芽',33,'软件',333]
    print (listzy530[1])
    print (listzy530[0:4])
    listzy530.pop(2)
    print (listzy530)
    listzy530.append(33)
    listzy530.append('作业')
    # listzy5302 = [3, 333]
    # listzy530.extend(listzy5302)
    print (listzy530)
    listzy530[0] = '5'
    print (listzy530)
    print (len(listzy530))


if __name__ == '__main__':
    # list1()
    # list2pop()
    # list3add()
    # list4update()
    # list5order_by()
    # list6distinct()
    zuoye530()
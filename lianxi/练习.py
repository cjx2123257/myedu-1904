#题目题: 新建一个list变量,里面有五个元素,访问索引2,切片访问索引1到4,删除索引3,添加两个元素,第0位元素改成字符5,获取索引长度
list1 = [1,2,3,'作','业']
def zuoye1():
    print (list1[1])
    print (list1[0:4])
    print (list1)
    list1.pop(2)
    print (list1)
    list1.append('不会')
    list1.append('123')
    print (list1)
    list1[1] = '36'
    print (list1)
    print(len(list1))
# 题: 新建一个字典变量,里面有两个键值对,访问一个值,删除一个键值对,添加一个键值对,更改任意一个值,再新建一个字典,将两个合并
def zuoye2():
    dist1 = {'12':'23','作':'业'}
    print(dist1['12'])
    dist1.pop('12')
    print (dist1)
    dist1['guoya'] = '果芽'
    print(dist1)
    dist1['作'] = 'zuo'
    print(dist1)
    dist2 = {'wei':'微','xin':'信'}
    #第一种合并
    dist1.update(dist2)
    print(dist1)
    #第二种合并
    dist3 = {'taobao':'淘宝','tianmao':'天猫'}
    dist4 = dict(dist1, **dist3)
    print(dist4)


if __name__ == '__main__':
    zuoye1()
    zuoye2()





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
# 题: 新建一个字典变量,里面有两个键值对,访问一个值,删除一个键值对,添加一个键值对,更改任意一个值,再新建一个字典,将两个合并

def zuoye530_2():
    zydist1 = {'guoya':'果芽','ruanjian':'软件'}
    print (zydist1['guoya'])
    zydist1.pop('ruanjian')
    print (zydist1)
    zydist1['xueyuan'] = '学院'
    print  (zydist1)
    zydist1['xueyuan'] = '学习'
    print (zydist1)
    #第一种
    zydist2 = {'tonghuashun': '同花顺', 'dazhihui': '大智慧'}
    zydist1.update(zydist2)
    print (zydist1)
    # 第二种
    zydist3 = {'jwyhal':'九尾妖狐阿狸','hbss':'寒冰射手'}
    hb1 = dict(zydist1, **zydist3)
    print (hb1)


if __name__ == '__main__':
    zuoye530_2()

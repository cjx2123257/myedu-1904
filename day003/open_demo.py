

def open_write():
    write1 = open('cjx.test', 'w+')
    # w+ 写入是覆盖
    for i in range(6):
        write1.write('123,321\n')
def open_wrinte2():
    write1 = open('cjx.test','a+')
    #a+ 写入是追加
    for i in range (6):
        write1.write('456\n')
def open_read():
    read1 = open('cjx.test', 'r+')
    # line 只读取一行
    print(read1.readline())
    #lines 读取所有数据 以list显示
    print(read1.readlines())
if __name__ == '__main__':
    open_read()

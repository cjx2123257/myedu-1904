

class guoya(object):

    def __init__(self,xingming,kecheng,riqi,shijian):
        self.xingming = xingming
        self.kecheng = kecheng
        self.riqi = riqi
        self.shijian = shijian
    def riqi1(self):
        print (self.xingming +'guoya')
    def info(self):
        print ('学校名称%s,学习课程%s,开课日期%s,学习时长%s'%(self.xingming,self.kecheng,self.riqi,self.shijian))

class guoya2(guoya):
    def __init__(self,xingming,kecheng,riqi,shijian,job):
        self.xingming = xingming
        self.kecheng = kecheng
        self.riqi = riqi
        self.shijian = shijian
        self.job = job 

    def riqi2(self):
        print (self.riqi+'2019.05.05')
        print('%s,%s,%s,%s,%s'%(self.xingming,self.kecheng,self.riqi,self.shijian,self.job))


if __name__ == '__main__':
    gy = guoya('果芽软件', '软件测试', '2019.05.05', '两个月')

    gy.info()
    gy.riqi1()
    gy2 = guoya2('果芽', '测试', '05.05', '月','学生')
    gy2.riqi2()



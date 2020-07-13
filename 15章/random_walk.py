'''这是随机漫步数的类   random_walk.py'''
from  random  import choice#导入随机库中的choice类

class RandomWalk():#定义一个随机类

    def __init__(self,num_points=5001):#给定3个属性，一个伟有默认值得随机次数
        self.num_points = num_points
        self.x_value = [0]#初始化X坐标
        self.y_value = [0]#初始化y坐标

    def get_setp(self):#定义一个随机获取数值得方法

        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return  step

    def fill_walk(self):#定义一个在坐标上行走得方法

        while len(self.x_value) < self.num_points:#给个循环，判断X坐标得值是否小于随机得次数

            x_step = self.get_setp()
            y_step = self.get_setp()

            if x_step and y_step == 0:#拒绝原地踏步
                continue

            next_x = self.x_value[-1] + x_step#下一次x得值=最后一次得次加一个随机数
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)#把值写入列表
            self.y_value.append(next_y)





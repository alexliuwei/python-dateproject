'''15-3'''
import matplotlib.pyplot as plt
from  random_walk import RandomWalk

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

rw = RandomWalk(50)

rw.fill_walk()
plt.plot(rw.x_value,rw.y_value,linewidth=2)
plt.title('随机漫步折线图')
plt.show()
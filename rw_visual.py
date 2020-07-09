import matplotlib.pyplot as plt
from  random_walk import RandomWalk

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

rw = RandomWalk()
polt_number = list(range(rw.num_points))


rw.fill_walk()
plt.title('随机漫步数',fontsize=23)
plt.scatter(rw.x_value,rw.y_value,c=polt_number,cmap=plt.cm.Blues,edgecolor='none',s=8)
plt.savefig(str(polt_number[0]) + '-' + str(polt_number[-1]) + '的随机漫步数图' + '.png')
plt.show()


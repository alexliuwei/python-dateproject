import matplotlib.pyplot as plt
from  random_walk import RandomWalk

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

rw = RandomWalk(50001)
polt_number = list(range(rw.num_points))


rw.fill_walk()
plt.figure(dpi=128, figsize=(10, 6))
plt.title('随机漫步数',fontsize=23)
plt.scatter(rw.x_value,rw.y_value,c=polt_number,cmap=plt.cm.Blues,edgecolor='none',s=8)
plt.scatter(rw.x_value[0],rw.y_value[0],c='green',edgecolor='none',s=50)
plt.scatter(rw.x_value[-1],rw.y_value[-1],c='red',edgecolor='none',s=50)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.savefig(str(polt_number[0]) + '-' + str(polt_number[-1]) + '的随机漫步数图' + '.png')
plt.show()



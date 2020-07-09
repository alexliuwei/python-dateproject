import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

x_value = list(range(1,5001))
y_value = list(x**3 for x in x_value)

plt.title('计算立方数',fontsize=24)
plt.xlabel('数值',fontsize=24)
plt.ylabel('立方数值',fontsize=24)

plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues)#给图标指定颜色映射
plt.tick_params(axis='both', which='major', labelsize=14)#设置镌刻大小
plt.axis([0,5000,0,120000000000])#取值范围要求提供四个值： x 和 y 坐标轴的最小值和最大值

plt.savefig('1to5000的立方数.png')
plt.show()
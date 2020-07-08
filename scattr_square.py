import  matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
#plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x_values = list(range(1,1001))#生成1-1000的数字列表
y_values = [x**2 for x in x_values]# for循环遍历1-1000然后再计算平方值

plt.scatter(x_values,y_values,s=40)#把变量给scatter方法，这个方法是绘制点
plt.title('点测试',fontsize=25)
plt.xlabel('X数值',fontsize=14)
plt.ylabel('y数值',fontsize=24)

plt.tick_params(axis='both', which='major', labelsize=14)
#plt.axis([0,1100,0,1100000])
plt.axis([0, 1000, 0, 1000000])#取值范围要求提供四个值： x 和 y 坐标轴的最小值和最大值
plt.show()
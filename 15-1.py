'''15-1'''
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签


x_valye = list(range(1,5001))
y_value = list(x**3 for x in x_valye)

plt.title('计算立方数',fontsize='25')
plt.xlabel('数值',fontsize='25')
plt.ylabel('平方数',fontsize='25')
plt.plot(x_valye,y_value,c='red')#绘制折现图
plt.tick_params(axis='both', labelsize=14)

plt.show()


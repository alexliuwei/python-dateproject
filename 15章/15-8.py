import pygal
from die import Die

die = Die()

rollnumber = [die.roll()+die.roll()+die.roll() for i in range(1000)]
sum_sumber = range(3,die.num_sizes*3+1)
shownumber = [rollnumber.count(x)  for x in sum_sumber]

hitp = pygal.Bar()

hitp.x_labels = sum_sumber
hitp.add('三个骰子运行10000次的',shownumber)
hitp.x_title = '三个骰子之和'
hitp.y_title = '出现的次数'
hitp.render_to_file('d63.svg')
import pygal
from  die import Die

die = Die()
sum_nuber = range(1,die.num_sizes*die.num_sizes+1)

roll_number = [die.roll()*die.roll() for i  in range(10000)]
show_number = [roll_number.count(x) for x in sum_nuber]

hipt = pygal.Bar()
'''
hipt.add('D6*D6',show_number)
hipt.x_labels = sum_nuber
hipt.x_title = '2个1-6的数字相乘'
hipt.y_title = '出现次数'
hipt.render_to_file('d6d6d6d.svg')
'''
notshownumber = []
for y in range(1,36):
    if y not in roll_number:
        notshownumber.append(y)

print(notshownumber)
print(show_number)


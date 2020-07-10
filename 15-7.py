import  pygal
from  die import  Die

die = Die(8)
rollnumber = [die.roll() + die.roll()  for i in range(100000)]

cfnumber = [ i  for i in range(2,die.num_sizes*2+1) ]
number = [rollnumber.count(i) for i in range(2,die.num_sizes*2+1)]

hipt = pygal.Bar()
hipt.add('D8+d8',number)
hipt.x_labels = list(range(2,die.num_sizes*2+1))
hipt.render_to_file('d8+d8.svg')
import pygal
from  die import Die

'''d多几次'''


die1 = Die()
die2 = Die()

results = [die1.roll()+die2.roll() for i in range(1000)]
'''
print(results)
for i in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)
'''
max_result = die1.num_sizes + die2.num_sizes
frequencies = [results.count(i)  for i in range(2,max_result+1)]
'''
for value in range(2,max_result+1):
    frequencie = results.count(value)
    frequencies.append(frequencie)
'''

hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = list(range(2,13))
hist.x_title =  'Result'
hist.y_title = "Frequency of Result"

hist.add('d6+d6',frequencies,classmethod='blue')
hist.render_to_file('die_visual.svg')
import pygal
from  die import Die

die6 = Die()
die10 = Die(10)

results = []

for result in  range(50000):
    resumt = die6.roll() + die10.roll()
    results.append(resumt)

renumber = []

maxnumber = die6.num_sizes + die10.num_sizes + 1

for i in  range(2,maxnumber):
    a = results.count(i)
    renumber.append(a)


print(renumber)
hist = pygal.Bar()

hist.x_labels = list(range(2,17))
hist.add('d6+d10',renumber)
hist.render_to_file('d6+d10.svg')


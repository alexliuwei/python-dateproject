import json
from country_codes import get_w_j
import  pygal.maps.world
from pygal.style import RotateStyle
cc_population = {}
file_name = 'population_data.json'

with open(file_name) as f:
    pop_date = json.load(f)

    for pop_dict in pop_date:
        if pop_dict['Year'] == '2010':
            citty_name =  pop_dict['Country Name']
            varls = int(float(pop_dict['Value']))
            code = get_w_j(citty_name)
            if code:
                cc_population[code] = varls

cc_pop1,cc_pop2,cc_pop3 = {},{},{}

for cc , pop in cc_population.items():
    if  pop < 10000000 :
        cc_pop1[cc] = pop
    elif pop < 1000000000 :
        cc_pop2[cc] = pop
    else:
        cc_pop3[cc] = pop

wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.add('pop< 10000000 ', cc_pop1)
wm.add('pop < 1000000000', cc_pop2)
wm.add('pop >1000000000', cc_pop3)
wm.render_to_file('2014.svg')
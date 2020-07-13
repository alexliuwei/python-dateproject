import json
from matplotlib import pyplot as plt
import pygal


file_name = 'gdp_json.json'
Country_code,gdp_value = [],[]

with open(file_name) as f:
    reaid = json.load(f)

    for gdp_dict in reaid:
        if gdp_dict['Year'] == 2005 :
            #Country_name = gdp_dict['Country Name']
            Country_code.append(gdp_dict['Country Code'])
            gdp_value.append(gdp_dict['Value'])



fig = plt.figure(dpi=128, figsize=(10, 6))
title = "Daily 2005 all Country GDP "
plt.plot(Country_code[0:25], gdp_value[0:25], c='blue', alpha=0.5)
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.savefig('2005gdp.png')
plt.show()
#
# hist = pygal.Bar()
# hist.add('Daily 2005 all Country GDP',gdp_value[0:25])
# hist.x_labels = Country_code[0:25]
# hist.render_to_file('2005gdp.svg')
# print(len(gdp_value))
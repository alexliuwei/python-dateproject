import requests
import pygal
from pygal.style import LightColorizedStyle as LCS ,LightenStyle as ls

url = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(url)#
print('statuscode:' + str(r.status_code))

reques_dict = r.json()
print('total_count:' + str(reques_dict['total_count']))

name , stargazers = [],[]

reque_dicts = reques_dict['items']

for i  in reque_dicts:
    name.append(i['name'])
    stargazers.append(i['stargazers_count'])

my_style = ls('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = name

chart.add('',stargazers)
chart.render_to_file('api.svg')
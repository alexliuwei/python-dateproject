import json

file_name = 'population_data.json'

with open(file_name) as f:
    pop_date = json.load(f)

    for pop_dict in pop_date:
        print(pop_dict)
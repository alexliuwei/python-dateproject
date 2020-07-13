import json

file_name = 'gdp_json.json'

with open(file_name) as f:
    reaid = json.load(f)

    for gdp_dict in reaid:
        if gdp_dict['Year'] == 2005 :
            #Country_name = gdp_dict['Country Name']
            Country_code = gdp_dict['Country Code']
            gdp_value = gdp_dict['Value']

            print(Country_code  + str(gdp_value))
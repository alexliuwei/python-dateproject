import requests

jul_ual = 'https://github.com/alexliuwei/python-dateproject/blob/master/16%E7%AB%A0/population_data.json'
req = requests.get(jul_ual)

with open('btc_close.json','w',encoding='utf-8') as f:
    f.write(req.text)
file_requests = req.json()
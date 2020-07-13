import  requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('status code:',r.status_code)

response_dict = r.json()

print(response_dict.keys())
print('Total reostisdj:' ,response_dict['total_count'])
repo_dict = response_dict['items']

print(len(repo_dict))

repsd_dict = repo_dict[0]
for key in repsd_dict.keys():
    print(key)
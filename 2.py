file_name = '1.txt'

with open(file_name,'r',encoding='utf8') as file_object:
    for i in  file_object:
        print(i.replace('$tbr=="',''))
        a = i.replace('$tbr=="','')
        print(a.replace('"||' , ' '))
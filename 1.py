file_name = '1.txt'
file2_name = '3.txt'
try:
    with open(file_name,'r',encoding='utf8') as file_object:
        for i in file_object:
            with open(file2_name,'a',encoding='utf8') as file2_objiet:
                file2_objiet.write('$tbr=="' + i.rstrip() + '"' + '||')
except FileNotFoundError:
        print('aaa')
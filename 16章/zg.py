import csv


zhiwu = {}
fz_name,zz_name  = [],[]
zhengzhi_name = ['主任','副主任（主持工作）','科长','党支部书记、所长','副所长（主持党政工作）','所长','院长','党支部书记、院长','副院长（主持党政工作）','党支部书记、主任']
file_name = 'zg.csv'

with open(file_name,encoding='utf-8') as f:
    readr = csv.reader(f)
    row_now = next(readr)

    for  i in readr:
        zhiwu[i[1]] = i[0]
    print(zhiwu)


#print(zhiwu)
for xm,zw in zhiwu.items():
    if zw in zhengzhi_name:
       zz_name.append(xm)
    else:
        fz_name.append(xm)
print(fz_name)
print(zz_name)
#
# file_name = '3.txt'
# with open(file_name,'a') as file_object:
#     for name in  zz_name:
#         file_object.write('$tbr=="' + name.rstrip() + '"' + '||')
#     file_object.write('\n')
#     for name2 in  fz_name:
#         file_object.write('$tbr=="' + name2.rstrip() + '"' + '||')
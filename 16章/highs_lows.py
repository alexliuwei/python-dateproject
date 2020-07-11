import csv
from matplotlib import pyplot as plt
from  datetime import datetime


filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    readr = csv.reader(f)
    header_row = next(readr)
    # print(header_row)

# for index,column_header in enumerate(header_row):
#     print(index,column_header)

    date_time,hihhs = [],[]
    for time in readr:
        c_time = datetime.strptime(time[0],'%Y-%m-%d')
        date_time.append(c_time)
        hihhs.append(int(time[1]))

#fig = plt.figure(dpi=128,figsize=(10,6))
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(date_time,hihhs,c='red')
plt.title('daily high temperatures , july 2014 ',fontsize =24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.savefig('ihhs.png')
plt.show()
